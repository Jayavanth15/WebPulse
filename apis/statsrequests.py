from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from models.statsrequests import StatsRequests
from schemas.statsrequests import StatsRequestsReq, StatsRequestsResponse
from models.website import Website
from base import SessionLocal
from auth.auth import decode_token
import os
import json
from datetime import datetime, timezone
from typing import Optional

router = APIRouter()

roles = ['Admin', 'admin']

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def time_stamp_range(date):
    s = date.split("-")
    date_new = datetime(int(s[2]), int(s[1]), int(s[0]), tzinfo=timezone.utc)  # March 6, 2025
    start_timestamp = int(date_new.timestamp())
    end_timestamp = start_timestamp + 86399
    return [(float)(start_timestamp), (float)(end_timestamp)]

def time_stamp(date):
    return date.timestamp()

def date_time(timestamp):
    dt = datetime.fromtimestamp(timestamp, timezone.utc)
    return dt.replace(tzinfo=None)

@router.get("/get_stats/", response_model=list[StatsRequestsResponse])
def get_stats(db: Session = Depends(get_db)):
    return db.query(StatsRequests).all()

@router.get("/get_stat/{request_id}", response_model=StatsRequestsResponse)
def get_stat(request_id : int, db : Session = Depends(get_db)):
    request = db.query(StatsRequests).filter(StatsRequests.request_id == request_id).first()
    return request

@router.get("/requests/{web_id}", response_model=list[StatsRequestsResponse])
def get_requests(web_id : int, start_date : Optional[str] = Query(None, description="dd-mm-yyyy"), end_date : Optional[str] = Query(None, description="dd-mm-yyyy"), db : Session = Depends(get_db)):
    check_stat = db.query(StatsRequests).filter(StatsRequests.web_id == web_id).all()
    if not check_stat:
        raise HTTPException(status_code=404, detail="Website load testing details are not available")
    start_timestamp = time_stamp_range(start_date)[0] if start_date else float(0)
    end_timestamp = time_stamp_range(end_date)[1] if end_date else datetime.now().timestamp()
    l = []
    for stat in check_stat:
        time = time_stamp(stat.start_time)
        if(time >= start_timestamp and time <= end_timestamp):
            l.append(stat)
    return l

@router.post("/add_stats/", response_model=list[StatsRequestsResponse])
def create_stat(web: StatsRequestsReq, db: Session = Depends(get_db), cred = Depends(decode_token)):
    if cred[0] in roles:
        web_exist = db.query(Website).filter(Website.web_id == web.web_id).first()
        if not web_exist:
            raise HTTPException(status_code=404, detail="Website not found")
        output = os.popen(f"locust -f scripts/locustfile.py -u {web.no_of_users} -r 1 -t 10s --host={web_exist.url} --web-host=127.0.0.1 --autostart --skip-log --json --autoquit 2").read()
        stats = json.loads(output)
        if stats :
            l = []
            if stats:
                for stat in stats:
                    stat["last_request_timestamp"] = date_time(stat["last_request_timestamp"])
                    stat["start_time"] = date_time(stat["start_time"])
                    stat["num_reqs_per_sec"] = {str(date_time(int(k))) : v for k, v in stat["num_reqs_per_sec"].items()}
                    stat["num_fail_per_sec"] = {str(date_time(int(k))) : v for k, v in stat["num_fail_per_sec"].items()}
                    new_stat = StatsRequests(
                        web_id=web_exist.web_id,  
                        request_name=stat["name"],  
                        request_method=stat["method"],  
                        last_request_time=stat["last_request_timestamp"],  
                        start_time=stat["start_time"],  
                        num_requests=stat["num_requests"],  
                        num_none_requests=stat["num_none_requests"],  
                        num_failures=stat["num_failures"],  
                        total_response_time=stat["total_response_time"],  
                        max_response_time=stat["max_response_time"],  
                        min_response_time=stat["min_response_time"],  
                        total_content_length=stat["total_content_length"],  
                        response_times=stat["response_times"],  
                        num_reqs_per_sec=stat["num_reqs_per_sec"],  
                        num_fail_per_sec=stat["num_fail_per_sec"]  
                    )
                    db.add(new_stat)
                    try:
                        db.commit()
                        db.refresh(new_stat)
                    except:
                        db.rollback()
                        raise HTTPException(status_code=400, detail="Error occured")
                        
                    l.append(new_stat)
            return l

    else:
        raise HTTPException(status_code=404, detail="This user doest have access")


@router.delete("/delete_stats/{user_id}", response_model=dict)
def delete_stat(request_id: int, db: Session = Depends(get_db), cred = Depends(decode_token)):
    if cred[0] in roles:
        stat = db.query(StatsRequests).filter(StatsRequests.request_id == request_id).first()
        if not stat:
            raise HTTPException(status_code=404, detail="User not found")
        db.delete(stat)
        db.commit()
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="This user doest have access")

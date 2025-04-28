import os
import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from base import SessionLocal
from models.webstats import WebStats
from schemas.webstats import WebStatsCreate, WebStatsResponse

#from logging.handlers import RotatingFileHandler

sender = os.getenv("email")
password = os.getenv("password")
receivers = ["koushik.m@eficens.com", "ayyappa.c@eficens.com"]



def send_email():
    body = "Hi Developers, your Website is down"
    msg = MIMEText(body)
    msg['Subject'] = "Reg, Downtime of the Project"
    msg['From'] = sender
    msg['To'] = ', '.join(receivers)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, receivers, msg.as_string())
    print("Message sent!")

def check_uptime(target_url):
    try:
        response = requests.get(target_url, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def check(website, id):
    if not check_uptime(website):
        db = SessionLocal()
        try:
            send_email()
        except Exception as e:
            print(e)
        new_stat = WebStats(cronjob_id = id, status = "InActive")
        db.add(new_stat)
        db.commit()
        db.refresh(new_stat)
        db.close()
        return True
    else:
        db = SessionLocal()
        new_stat = WebStats(cronjob_id = id, status = "Active")
        db.add(new_stat)
        db.commit()
        db.refresh(new_stat)
        db.close()
        return False

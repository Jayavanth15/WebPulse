from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from base import SessionLocal
from models.projectwebsite import ProjectWebsite
from schemas.projectwebsite import ProjectWebsiteCreate, ProjectWebsiteResponse
from auth.auth import decode_token

router = APIRouter()

roles = ["Admin", "admin"]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/get_project_website/", response_model=list[ProjectWebsiteResponse])
def get_prowebs(db: Session = Depends(get_db)):
    return db.query(ProjectWebsite).all()

@router.post("/create_project_website/", response_model=ProjectWebsiteResponse)
def create_proweb(proweb: ProjectWebsiteCreate, db: Session = Depends(get_db), cred = Depends(decode_token)):
    if cred[0] in roles:
        exist_proweb = db.query(ProjectWebsite).filter(ProjectWebsite.project_id == proweb.project_id, ProjectWebsite.web_id == proweb.web_id).first()
        if exist_proweb:
            raise HTTPException(status_code=400, detail="user id and organization id already exists")
        new_proweb = ProjectWebsite(project_id=proweb.project_id, web_id = proweb.web_id)
        db.add(new_proweb)
        db.commit()
        db.refresh(new_proweb)
        return new_proweb
    else:
        raise HTTPException(status_code=404, detail="This user doest have access")


@router.put("/update_project_website/{id}", response_model=ProjectWebsiteResponse)
def update_proweb(id: int, proweb: ProjectWebsiteCreate, db: Session = Depends(get_db), cred = Depends(decode_token)):
    if cred[0] in roles:
        existing_proweb = db.query(ProjectWebsite).filter(ProjectWebsite.proweb_id == id).first()
        if not existing_proweb:
            raise HTTPException(status_code=404, detail="Project/Website not found")
        
        exist_proweb = db.query(ProjectWebsite).filter(ProjectWebsite.project_id == proweb.project_id, ProjectWebsite.web_id == proweb.web_id).first()
        if exist_proweb:
            raise HTTPException(status_code=400, detail="project id and website id already exists")
        
        existing_proweb.project_id = proweb.project_id
        existing_proweb.web_id = proweb.web_id
        db.commit()
        db.refresh(existing_proweb)
        return existing_proweb
    else:
        raise HTTPException(status_code=404, detail="This user doest have access")


@router.delete("/delete_project_website/{id}", response_model=dict)
def delete_proweb(id: int, db: Session = Depends(get_db), cred = Depends(decode_token)):
    if cred[0] in roles:
        proweb = db.query(ProjectWebsite).filter(ProjectWebsite.proweb_id == id).first()
        if not proweb:
            raise HTTPException(status_code=404, detail="Project/Website not found")
        db.delete(proweb)
        db.commit()
        return {"message": "Project Website deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="This user doest have access")

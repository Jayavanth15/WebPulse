from pydantic import BaseModel

class ProjectCreate(BaseModel):
    org_id : int
    project_name : str

class ProjectRespose(BaseModel):
    project_id : int
    org_id : int
    project_name : str
    createdBy : int
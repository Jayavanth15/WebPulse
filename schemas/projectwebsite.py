from pydantic import BaseModel

class ProjectWebsiteCreate(BaseModel):
    project_id : int
    web_id : int

class ProjectWebsiteResponse(BaseModel):
    proweb_id : int
    project_id : int
    web_id : int
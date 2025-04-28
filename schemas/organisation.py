from pydantic import BaseModel

class OrgCreate(BaseModel):
    org_name : str
    org_address : str

class OrgResponse(BaseModel):
    org_id : int
    org_name : str
    org_address : str
    createdBy : int
from pydantic import BaseModel

class UserOrgCreate(BaseModel):
    user_id : int
    org_id : int

class UserOrgResponse(BaseModel):
    userorg_id : int
    user_id : int
    org_id : int
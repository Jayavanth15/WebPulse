from pydantic import BaseModel
from typing import Optional

class WebCreate(BaseModel):
    url : Optional[str]
    description : Optional[str]
    interval : Optional[int]

class WebResponse(BaseModel):
    web_id : Optional[int]
    url : Optional[str]
    description : Optional[str]
    interval : Optional[int]
    createdBy : Optional[int]

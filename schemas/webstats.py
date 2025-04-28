from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WebStatsCreate(BaseModel):
    cronjob_id : Optional[int]
    status : Optional[str]

class WebStatsResponse(BaseModel):
    stat_id : Optional[int]
    cronjob_id : Optional[int]
    createdAt : Optional[datetime]
    status : Optional[str]

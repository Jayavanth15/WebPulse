from pydantic import BaseModel
from typing import Optional

class CronJobCreate(BaseModel):
    web_id : Optional[int]
    isExist : Optional[bool]

class CronJobResponse(BaseModel):
    cronjob_id : Optional[int]
    web_id : Optional[int]
    isExist : Optional[bool]
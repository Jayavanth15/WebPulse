from pydantic import BaseModel
from typing import Dict
from datetime import datetime

class StatsRequestsReq(BaseModel):
    web_id : int
    no_of_users : int

# class StatsRequestsCreate(BaseModel):
    
#     request_name: str
#     request_method: str
#     last_request_timestamp: float
#     start_time: float
#     num_requests: int
#     num_none_requests: int
#     num_failures: int
#     total_response_time: float
#     max_response_time: float
#     min_response_time: float
#     total_content_length: int
#     response_times: Dict[str, int]
#     num_reqs_per_sec: Dict[str, int]
#     num_fail_per_sec: Dict[str, int]

class StatsRequestsResponse(BaseModel):
    web_id : int
    request_id : int
    request_name: str
    request_method: str
    last_request_time: datetime
    start_time: datetime
    num_requests: int
    num_none_requests: int
    num_failures: int
    total_response_time: float
    max_response_time: float
    min_response_time: float
    total_content_length: int
    response_times: Dict[str, int]
    num_reqs_per_sec: Dict[str, int]
    num_fail_per_sec: Dict[str, int]
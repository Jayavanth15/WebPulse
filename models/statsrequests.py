from sqlalchemy import Column, Integer, Float, JSON, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from models.users import Base

class StatsRequests(Base):
    __tablename__ = "StatsRequests"
    
    request_id = Column(Integer, primary_key=True, autoincrement=True)
    web_id = Column(Integer, ForeignKey("Website.web_id"))
    request_name = Column(String(255), nullable=False)
    request_method = Column(String(255), nullable=False)
    last_request_time = Column(DateTime, default=func.now())
    start_time = Column(DateTime, default=func.now())
    num_requests = Column(Integer, nullable=False)
    num_none_requests = Column(Integer, nullable=False)
    num_failures = Column(Integer, nullable=False)
    total_response_time = Column(Float, nullable=False)
    max_response_time = Column(Float, nullable=False)
    min_response_time = Column(Float, nullable=False)
    total_content_length = Column(Integer, nullable=False)
    response_times = Column(JSON, nullable=False)
    num_reqs_per_sec = Column(JSON, nullable=False)
    num_fail_per_sec = Column(JSON, nullable=False)

    web2 = relationship("Website", back_populates="statsr")
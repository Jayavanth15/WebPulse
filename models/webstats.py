from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from models.users import Base

class WebStats(Base):
    __tablename__ = "WebStats"

    stat_id = Column(Integer, primary_key=True, autoincrement=True)
    cronjob_id = Column(Integer, ForeignKey("CronJob.cronjob_id"))
    status = Column(String(255), nullable=False)
    createdAt = Column(DateTime, default=func.now())

    cron = relationship("CronJob", back_populates="stat")
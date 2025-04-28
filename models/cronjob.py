from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.users import Base

class CronJob(Base):
    __tablename__ = "CronJob"

    cronjob_id = Column(Integer, primary_key=True, autoincrement=True)
    web_id = Column(Integer, ForeignKey("Website.web_id"))
    isExist = Column(Boolean, nullable=False)

    web1 = relationship("Website", back_populates="cron")
    stat = relationship("WebStats", back_populates="cron")
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.users import Base

class Website(Base):
    __tablename__ = "Website"

    web_id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(255), nullable=False)
    description  = Column(String(255), unique=True, nullable=False)
    interval = Column(Integer, nullable=False)
    createdBy = Column(Integer, ForeignKey("User.user_id"))

    user = relationship("User", back_populates="web")
    cron = relationship("CronJob", back_populates="web1")
    statsr = relationship("StatsRequests", back_populates="web2")
    proweb = relationship("ProjectWebsite", back_populates="web3")
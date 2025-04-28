from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.users import Base

class ProjectWebsite(Base):
    __tablename__ = "ProjectWebsite"

    proweb_id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("Project.project_id"))
    web_id = Column(Integer, ForeignKey("Website.web_id"))

    web3 = relationship("Website", back_populates="proweb")
    pro = relationship("Project", back_populates="proweb")
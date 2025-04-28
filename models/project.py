from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.users import Base

class Project(Base):
    __tablename__ = "Project"

    project_id = Column(Integer, primary_key=True, autoincrement=True)
    org_id = Column(Integer, ForeignKey("Organisation.org_id"))
    project_name = Column(String(255), nullable=False)
    createdBy = Column(Integer, ForeignKey("User.user_id"))
    
    user = relationship("User", back_populates="pro")
    proweb = relationship("ProjectWebsite", back_populates="pro")
    org = relationship("Organisation", back_populates="pro")
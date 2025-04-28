from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.users import Base

class Organisation(Base):
    __tablename__ = "Organisation"

    org_id = Column(Integer, primary_key=True, autoincrement=True)
    org_name = Column(String(255), nullable=False)
    org_address = Column(String(255), nullable=False)
    createdBy = Column(Integer, ForeignKey("User.user_id"))

    user = relationship("User", back_populates="org")
    userorg = relationship("UserOrganisation", back_populates="org")
    pro = relationship("Project", back_populates="org")
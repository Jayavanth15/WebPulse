from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.users import Base

class UserOrganisation(Base):
    __tablename__ = "UserOrganisation"

    userorg_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("User.user_id"))
    org_id = Column(Integer, ForeignKey("Organisation.org_id"))

    user = relationship("User", back_populates="userorg")
    org = relationship("Organisation", back_populates="userorg")
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "User"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)
    createdBy = Column(Integer, nullable=False)

    org = relationship("Organisation", back_populates="user")
    userorg = relationship("UserOrganisation", back_populates="user")
    web = relationship("Website", back_populates="user")
    pro = relationship("Project", back_populates="user")
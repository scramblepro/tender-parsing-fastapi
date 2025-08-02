from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tender(Base):
    __tablename__ = "tenders"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, unique=True, nullable=False)
    title = Column(Text, nullable=False)
    link = Column(String, nullable=False)
    price = Column(String, nullable=True)
    region = Column(String, nullable=True)
    customer = Column(String, nullable=True)
    deadline_date = Column(String, nullable=True)
    start_date = Column(String, nullable=True)

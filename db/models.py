import sqlalchemy
from sqlalchemy import Column, Integer, Boolean

from db.database_async import Base

metadata = sqlalchemy.MetaData()


class Report(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True, index=True)
    status = Column(Boolean, default=False)

    class Config:
        orm_mode = True

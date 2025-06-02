from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,MetaData,Float
from datetime import datetime
# Naming convention
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
meta = MetaData(naming_convention=convention)

Base = declarative_base(metadata=meta)
# vendor table
class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)
    specialty = Column(String)
    created_at = Column(DateTime, default=datetime.now)


# projects table
class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    start_date = Column(String, nullable=False)
    end_date = Column(String)
    budget = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

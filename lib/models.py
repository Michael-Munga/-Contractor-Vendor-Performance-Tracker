from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import Column,Integer,String,DateTime,MetaData,Float,Text,ForeignKey
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

    # one-to-many --> one vendor has many contracts
    contracts = relationship("Contract", back_populates="vendor")


# projects table
class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    start_date = Column(String, nullable=False)
    end_date = Column(String)
    budget = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    # one-to-many---->one project has many contracts
    contracts = relationship("Contract", back_populates="project")


# Contract table 
class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True)
    # foreign keys go to the many side of vendors and projects
    vendor_id = Column(Integer,ForeignKey("vendors.id"), nullable=False)
    project_id = Column(Integer,ForeignKey("projects.id"), nullable=False)
    contract_date = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    status = Column(String, nullable=False)  
    created_at = Column(DateTime, default=datetime.now)

    # relationships (many side in relation to vendors/projects --> one-to-many relationship with them)
    vendor = relationship("Vendor", back_populates="contracts")
    project = relationship("Project", back_populates="contracts")

    # one-to-many ---> one contract has many performance reviews
    reviews = relationship("PerformanceReview", back_populates="contract")


# perfomance review
class PerformanceReview(Base):
    __tablename__ = "performance_reviews"

    id = Column(Integer, primary_key=True)
    # foreign key goes to the many side of contracts
    contract_id = Column(Integer,ForeignKey("contracts.id"), nullable=False)
    review_date = Column(String, nullable=False)
    rating = Column(Float, nullable=False)  
    remarks = Column(Text)
    created_at = Column(DateTime, default=datetime.now)

    # relationship (many side in relation to contracts --> one-to-many with contracts)
    contract = relationship("Contract", back_populates="reviews")


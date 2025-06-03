from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# create a database connection
db_url = "sqlite:///db/store.db"
engine = create_engine(db_url, echo=False)
Session =sessionmaker(bind=engine)
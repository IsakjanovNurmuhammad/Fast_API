from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

SQL_URl = "sqlite:///./test.db"

engine = create_engine(SQL_URl)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///fraud.db",
                       connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True)
    ml_score = Column(Float)
    rule_score = Column(Float)
    final_score = Column(Float)
    decision = Column(String)

Base.metadata.create_all(engine)
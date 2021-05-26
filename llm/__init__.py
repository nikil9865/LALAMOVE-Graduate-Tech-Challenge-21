from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

__version__ = '0.1.0'

Base = declarative_base()
class Order(Base):
    __tablename__ = "orders"

    id = Column('id', Integer, primary_key=True)
    origin = Column('origin', String, unique=False)
    destination = Column('destination', String, unique=False)
    taken = Column('taken', Boolean, unique=False)

engine = create_engine('sqlite:///orders.db', echo=False)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

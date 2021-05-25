import typer
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
#
app = typer.Typer()

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

@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


@app.command("create_order")
def create_order(orgin: str, destination: str):
    """
    Create an order
    """
    order = Order()
    order.origin = orgin
    order.destination = destination
    order.taken = False

    session.add(order)
    session.commit()
    session.close()

@app.command("list_orders")
def list_orders():
    """
    List all orders that haven't been taken
    """

    orders = session.query(Order).all()
    for order in orders:
        typer.echo(order.id)
        typer.echo(order.origin)
        typer.echo(order.origin)

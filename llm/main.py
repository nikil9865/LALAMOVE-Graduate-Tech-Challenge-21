import typer
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

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
    Welcome to the LLM command line tool!
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

    session.refresh(order)
    typer.echo(order.id)

@app.command("list_orders")
def list_orders():
    """
    List all orders that haven't been taken
    """
    orders = session.query(Order).filter(Order.taken==False).all()
    for order in orders:
        typer.echo(str(order.id) + "," + order.origin + "," + order.destination)

@app.command("take_order")
def take_order(id: str):
    """
    Take order - based on ID
    """
    orderTaken = session.query(Order.taken).filter(Order.id == id).first()
    if orderTaken is None:
        typer.echo("order does not exist")
    else:
        if (orderTaken[0]):
            typer.echo("order already taken")
        else:
            session.query(Order).filter(Order.id == id).update({Order.taken: True})
    session.commit()

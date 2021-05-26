import typer
from llm import session, Order

app = typer.Typer()

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
    try:
        order = Order()
        order.origin = orgin
        order.destination = destination
        order.taken = False

        session.add(order)
        session.commit()

        session.refresh(order)
        typer.echo(order.id)
    except:
        session.rollback()
    finally:
        session.close()

@app.command("list_orders")
def list_orders():
    """
    List all orders that haven't been taken
    """
    try:
        orders = session.query(Order).filter(Order.taken==False).all()
        for order in orders:
            typer.echo(str(order.id) + "," + order.origin + "," + order.destination)
    finally:
        session.close()

@app.command("take_order")
def take_order(id: str):
    """
    Take order - based on ID
    """
    try:
        orderTaken = session.query(Order.taken).filter(Order.id == id).first()
        if orderTaken is None:
            typer.echo("order does not exist")
            raise typer.Exit(code=2)
        else:
            if (orderTaken[0]):
                typer.echo("order already taken")
                raise typer.Exit(code=1)
            else:
                session.query(Order).filter(Order.id == id).update({Order.taken: True})

        session.commit()
    except:
        session.rollback()
    finally:
        session.close()

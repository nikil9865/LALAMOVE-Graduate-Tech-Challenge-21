from llm import __version__
from typer.testing import CliRunner
from llm.main import app
from llm import session, Order

runner = CliRunner()

def test_llm():
    assert __version__ == '0.1.0'

    session.query(Order).delete()
    session.commit()

    result = runner.invoke(app, ["create_order", "Mong Kok", "Central"])
    assert result.exit_code == 0
    assert "1" in result.stdout

    result = runner.invoke(app, ["list_orders"])
    assert result.exit_code == 0
    assert "1,Mong Kok,Central" in result.stdout

    result = runner.invoke(app, ["create_order", "TST", "SSP"])
    assert result.exit_code == 0
    assert "2" in result.stdout

    result = runner.invoke(app, ["take_order", "1"])
    assert result.exit_code == 0
    assert "" in result.stdout

    result = runner.invoke(app, ["list_orders"])
    assert result.exit_code == 0
    assert "2,TST,SSP" in result.stdout

    result = runner.invoke(app, ["take_order", "1"])
    assert result.exit_code != 1
    assert "order already taken" in result.stdout

    result = runner.invoke(app, ["take_order", "42"])
    assert result.exit_code != 2
    assert "order does not exist" in result.stdout

    session.query(Order).delete()
    session.commit()
    session.close()

#python3 -m venv ./venv
#activate () {
#  . venv/bin/activate
#}
#activate

pip3 install poetry
pip3 install sqlalchemy

poetry install
llm load

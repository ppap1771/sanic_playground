from sanic import Sanic
from sanic.response import text
from sanic.config import Config

class new_config(Config):
    FOO = "someshit"

app = Sanic("__name__", Config=new_config())

app = Sanic('myapp')

app.config.DB_NAME = 'appdb'
app.config['DB_USER'] = 'appuser'

db_settings = {
    'DB_HOST': 'localhost',
    'DB_NAME': 'appdb',
    'DB_USER': 'appuser'
}
app.config.update(db_settings)

@app.get("/")
async def hello_world(request) -> object:
    """
    This is a sample function that returns "Hello, World!"
    :param request: request object
    :return: text saying hello world
    """
    return text("Hello, world.")

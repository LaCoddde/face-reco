from flask import Flask
from src.config import Config
from src.controllers import register_controllers

app = Flask(__name__)
app.config.from_object(Config)

register_controllers(app)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask_dotenv import DotEnv
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


class App:
    __db = None
    __app = None

    def __init__(self, app: Flask) -> None:
        App.__app = app
        CORS(App.__app)
        App.__init_db(app)

    @staticmethod
    def __init_db(app: Flask):
        App.__db = SQLAlchemy(app)

    @staticmethod
    def get_db() -> SQLAlchemy:
        return App.__db

    @staticmethod
    def get_app() -> Flask:
        return App.__app

    def start(self) -> 'App':
        self.__app.run(debug=App.get_config().get('DEBUG'),
                       port=App.get_config().get('PORT'),
                       host=App.get_config().get('HOST'))

        return self

    def load_config(self) -> 'App':
        env = DotEnv()
        env.init_app(App.get_app())

        return self

    @staticmethod
    def get_config():
        return App.get_app().config

    @staticmethod
    def is_production_env() -> bool:
        return App.get_config().get('APP_ENV') == 'production'

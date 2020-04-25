import abc

from flask_sqlalchemy import SQLAlchemy
from src.app_bundle.contracts.identifiable import Identifiable

db = SQLAlchemy()


class BaseModel(db.Model, Identifiable):
    __metaclass__ = abc.ABCMeta
    __abstract__ = True

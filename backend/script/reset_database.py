"""Reset Database"""

from ..entities.user_entity import  EntityBase
from ..database import engine

EntityBase.metadata.drop_all(engine)
EntityBase.metadata.create_all(engine)
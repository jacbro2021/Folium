"""Reset Database"""

from ..entities.entity_base import  EntityBase
from ..entities.user_entity import UserEntity
from ..entities.plant_entity import PlantEntity
from ..database import engine

EntityBase.metadata.drop_all(engine)
EntityBase.metadata.create_all(engine)
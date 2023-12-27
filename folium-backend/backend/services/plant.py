"""Plant service used by the plant api to perform actions on the plant table in the db."""

from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import Depends
from ..database import db_session

from ..models.plant import Plant
from ..entities.plant_entity import PlantEntity
from ..models.user import User
from ..entities.user_entity import UserEntity

from .exceptions import (UserNotFoundException,)

class PlantService:
    """Plant service to perform actions on the plant table."""

    def __init__(self,
                 session: Session = Depends(db_session)):
        self._session = session

    def get_all_user_plants(self, key: str) -> list[Plant]:
        """
        Retrieve all plants for a given user from the database
        
        Args:
            key: The key for the user.
            
        Returns:
            list[Plant]: The list of the users plant objects.

        Raises:
            UserNotFoundException: If a user is not found for the provided key.
        """

        # Check that a user exists for the given key.
        query = select(UserEntity).where(UserEntity.key == key)
        user_entity: UserEntity | None = self._session.scalar(query)

        # If the user does not exist then raise exception.
        if user_entity is None:
            raise UserNotFoundException()
        
        # Create list of plants and query db to retrieve entities.
        plants: list[Plant] = []
        plant_entities = self._session.query(PlantEntity).where(PlantEntity.owner_key == key)

        # Loop through retrieved entities and convert to plant models.
        for entity in plant_entities:
            plant = entity.to_model()
            plants.append(plant)

        # Return the list of plants for the user with the provided key.
        return plants

    def create_plant(plant: Plant) -> Plant:
        """
        Add a new plant to the database.
        
        Args:
            plant: The plant to add to the database.
            
        Returns:
            Plant: the plant that was successfully added to the database.
        """

    def remove_plant(plant: Plant) -> Plant:
        """
        Removes a plant from the database.
        
        Args: 
            plant: The plant to remove from the database.
            
        Returns:
            Plant: The plant that was successfully removed from the database.
        """

    def update_Plant(plant: Plant) -> Plant:
        """
        Updates a plant in the database.
        
        Args:
            plant: The updated version of the plant.
            
        Plant:
            Plant: The model representation of the plant that was updated in the database.
        """
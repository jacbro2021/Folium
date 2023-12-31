"""Plant service used by the plant api to perform actions on the plant table in the db."""

from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import Depends
from ..database import db_session

from ..models.plant import Plant
from ..entities.plant_entity import PlantEntity
from ..models.user import User
from ..entities.user_entity import UserEntity

from .exceptions import (UserNotFoundException,
                         PlantNotFoundException)

class PlantService:
    """Plant service to perform actions on the plant table."""

    def __init__(self,
                 session: Session = Depends(db_session)):
        self._session = session

    def __identify_user(self, key: str) -> None:
        """
        Helper method that checks that a user with the given key exists in the database.
        
        Args:
            key: the key of the user to search for.
            
        Raises:
            UserNotFoundException: If the user is not found."""
        
        # Check that a user exists for the given key.
        query = select(UserEntity).where(UserEntity.key == key)
        user_entity: UserEntity | None = self._session.scalar(query)

        # If the user does not exist then raise exception.
        if user_entity is None:
            raise UserNotFoundException()
        
    def __find_plant_entity(self, plant_id: int, owner_key: str) -> PlantEntity:
        """
        Helper method that either retrieves a plant from the database or raises an exception.
        
        Args:
            plant_id: The id of the plant to search for.
            owner_key: The key of the owner that owns the plant to search for.

        Returns:
            PlantEntity: The Entity representation of the retrieved plant.
        
        Raises:
            PlantNotFoundException: If the plant is not found in the database.
        """

         # Query the database to find the plant to be deleted.
        query = select(PlantEntity).where(PlantEntity.id == plant_id and PlantEntity.owner_key == owner_key)
        plant_entity: PlantEntity | None = self._session.scalar(query)

        # If not plant found, raise error. 
        if plant_entity == None:
            raise PlantNotFoundException()

    def get_all_user_plants(self, key: str) -> list[Plant]:
        """
        Retrieve all plants for a given user from the database.
        
        Args:
            key: The key for the user.
            
        Returns:
            list[Plant]: The list of the users plant objects.

        Raises:
            UserNotFoundException: If a user is not found for the provided key.
        """

        # Check that a user exists for the given key.
        self.__identify_user(key=key)
        
        # Create list of plants and query db to retrieve entities.
        plants: list[Plant] = []
        plant_entities = self._session.query(PlantEntity).where(PlantEntity.owner_key == key)

        # Loop through retrieved entities and convert to plant models.
        for entity in plant_entities:
            plant = entity.to_model()
            plants.append(plant)

        # Return the list of plants for the user with the provided key.
        return plants

    def create_plant(self, plant: Plant) -> Plant:
        """
        Add a new plant to the database.
        
        Args:
            plant: The plant to add to the database.
            
        Returns:
            Plant: the plant that was successfully added to the database.

        Raises:
            UserNotFoundException: If the plant's owner key does not belong to a user in the user table.
        """

        # Check that a user exists for the given key.
        self.__identify_user(key=plant.owner_key)
        
        # Add the plant to the db.
        plant_entity = PlantEntity.from_model(plant=plant)
        self._session.add(plant_entity)
        self._session.commit()

        return plant_entity.to_model()

    def remove_plant(self, plant: Plant) -> Plant:
        """
        Removes a plant from the database.
        
        Args: 
            plant: The plant to remove from the database.
            
        Returns:
            Plant: The plant that was successfully removed from the database.

        Raises:
            UserNotfoundException: If the user with the respective key is not found.
            PlantNotFoundException: If the plant with the given id is not found in the database.
        """

        # Query the database to find the owner of the plant.
        self.__identify_user(key=plant.owner_key)
        
        # Query the database to find the plant to be deleted.
        plant_entity = self.__find_plant_entity(plant)
        
        # Delete plant from database and return. 
        self._session.delete(plant_entity)
        self._session.commit()

        return plant_entity.to_model()

    def update_Plant(self, plant: Plant) -> Plant:
        """
        Updates a plant in the database.
        
        Args:
            plant: The updated version of the plant.
            
        Returns:
            Plant: The model representation of the plant that was updated in the database.

        Raises:
            UserNotfoundException: If the user with the respective key is not found.
            PlantNotFoundException: If the plant with the given id is not found in the database.
        """
        # Query the database to find the owner of the plant.
        self.__identify_user(plant.owner_key)
        
        # Query the database to find the plant to be deleted.
        plant_entity = self.__find_plant_entity(plant)
        
        # Update the plant entity and commit the changes.
        plant_entity.update(plant=plant)
        self._session.commit()

        return plant_entity.to_model()

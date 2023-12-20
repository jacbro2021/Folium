"""User Service to be used by the user api to perform actions on the user table."""

from fastapi import Depends
from ..database import db_session
from sqlalchemy.orm import Session
from sqlalchemy import select

from ..models.user import User
from ..entities.user_entity import UserEntity
from .exceptions import InvalidCredentialsUserException, DuplicateUserException, UserNotFoundException

import hashlib
from datetime import datetime

class UserService:
    """User service to perform actions on the user table"""

    def __init__(self,
                 session: Session = Depends(db_session)):
        self._session = session

    def create_user(self, first_name: str = "", last_name: str = "", email: str = "") -> str:
        """
        Creates a new user in the database
        
        Args:
            first name: The users first name.
            last name: The users last name.
            email: The users email.

        Returns:
            key: the key for the newly create user in the db.

        Raises:
            InvalidCredentialsException: If the input is improperly formatted or empty.
            DuplicateUserException: If the user is already in the database.
        """

        # Validate that the user has entered information for the name and email fields
        if first_name.strip() == "" or last_name.strip() == "" or email.strip == "":
            raise InvalidCredentialsUserException()
        
        query = select(UserEntity).where(UserEntity.email == email.strip())
        entity: UserEntity | None = self._session.scalar(query)
        
        # Check for duplicate user
        if entity:
            raise DuplicateUserException(entity=entity)
        
        # Create the date string
        date = datetime.now()
        date_string = date.strftime("%Y-%m-%d %H:%M:%S")

        # Create the key for the user
        hash_input: str = first_name.strip() + last_name.strip() + email.strip() + date_string.strip()
        encoded_string = hash_input.encode()
        key = hashlib.sha256(encoded_string).hexdigest()

        # Create the user model
        user = User(first_name=first_name.strip(),
                     last_name=last_name.strip(),
                       email= email.strip(),
                       created_at=date_string,
                       key=key)
        
        # Create the entity and add it to the database
        user_entity = UserEntity.from_model(user=user)
        self._session.add(user_entity)
        self._session.commit()

        # Return the new users key
        return key
    
    def get_user(self, key: str) -> User:
        """
        Retrieves a user from the database
        
        Args:
            key: the key of the user to be retrieved

        User:
            User: a user in the database

        Raises:
            UserNotFoundException: If the user is not in the database
        """
        
        # Get the user entity from the database.
        query = select(UserEntity).where(UserEntity.key == key)
        entity: UserEntity | None = self._session.scalar(query)

        if entity:
            # return the model representation of the user.
            return entity.to_model()
        else:
            raise UserNotFoundException()
        

    def update_user(self, key:str, user: User) -> User:
        """
        Updates a user in the database.

        Args:
            key: The key of the user to update.
            user: The updated user.

        Raises:
            UserNotFoundException: If the user is not found in the database.
        """

        # Get the entity to be updated from the database.
        query = select(UserEntity).where(UserEntity.key == key)
        entity: UserEntity | None = self._session.scalar(query)

        if entity:
            # Update the user and commit the changes to the database.
            entity.update(user=user)
            self._session.commit()

            return entity.to_model()
        else:
            raise UserNotFoundException()
        
    def delete_user(self, key: str) -> User:
        """
        Deletes a user from the database.
        
        Args: 
            key: the key for the user to be deleted.
            
        Returns:
            User: The deleted user.
            
        Raises: 
            UserNotFoundException: If the user is not found in the database.
        """

        # Get the entity to be deleted from the database.
        query = select(UserEntity).where(UserEntity.key == key)
        entity: UserEntity | None = self._session.scalar(query)

        if entity:
            # Delete the user from the database.
            self._session.delete(entity)
            self._session.commit()

            return entity.to_model()
        else:
            raise UserNotFoundException()
"""Class to hold all exceptions for the various services"""

from ..entities.user_entity import UserEntity
from ..models.plant import Plant

class DuplicateUserException(Exception):
    """Exception to be thrown when a new account is created with an email that is already being used for another user."""
    def __init__(self, entity: UserEntity):
        super().__init__(
            f"An account already exists with email {entity.email}."
        )

class InvalidCredentialsUserException(Exception):
    """Exception to be thrown when a user provides invalid credentials when creating a user"""
    def __init__(self, msg: str = "Invalid credentials. No whitespace allowed."):
        super().__init__(
            msg
        )

class UserNotFoundException(Exception):
    """Exception to be thrown when a key is passed for a user that is not in the database."""
    def __init__(self):
        super().__init__(
            "User not found."
        )

class PlantNotFoundException(Exception):
    """Exception to be thrown when the database is queried for a plant that does not exist."""
    def __init__(self, plant: Plant):
        super().__init__(
            f"Plant {plant.common_name} not found for owner with that key."
        )
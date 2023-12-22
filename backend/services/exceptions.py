"""Class to hold all exceptions for the various services"""

from ..entities.user_entity import UserEntity

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
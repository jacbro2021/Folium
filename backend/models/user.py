"""User model serves as the data object for representing users across application layers."""

from pydantic import BaseModel

class UserIdentity(BaseModel):
    """
    Pydantic model to represent how `User`s are identified in the system.

    This model is based on the `UserEntity` model, which defines the shape
    of the `User` database in the PostgreSQL database.
    """

    id: int | None = None


class User(UserIdentity, BaseModel):
    """
    Pydantic model to represent a registered `User`.

    This model is based on the `UserEntity` model, which defines the shape
    of the `User` database in the PostgreSQL database
    """

    first_name: str = ""
    last_name: str = ""
    email: str = ""
    password: str = ""
    created_at: str = ""
    key: str = ""
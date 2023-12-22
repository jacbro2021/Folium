"""Definition of SQLAlchemy backend table entity to represent users."""

from typing import Self
from .entity_base import EntityBase

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Date

from ..models.user import User

class UserEntity(EntityBase):
    """Serves as the database model schema defining the shape of the `User` table"""

    # Name for the user table in the db.
    __tablename__ = "user"

    # Column to store id's for each user
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Column to store the users first name
    first_name: Mapped[String] = mapped_column(String, nullable=False)
    # Column to store the users last name
    last_name: Mapped[String] = mapped_column(String, nullable=False)
    # Column to store the users email 
    email: Mapped[String] = mapped_column(String, nullable=False)
    # Column to store the users password
    password: Mapped[String] = mapped_column(String, nullable=False)
    # Column to store when the user was created
    created_at: Mapped[str] = mapped_column(String, nullable=False)
    # key for the user to access their own information
    key: Mapped[str] = mapped_column(String, nullable=False)
    
    @classmethod
    def from_model(cls, user: User) -> Self:
        """
        Creates a user_entity instance from a user model.

        Args: 
            User: the user model to create the entity from.

        Returns:
            Self: the not yet persisted entity.
        """
        return cls(
            id = user.id,
            first_name = user.first_name,
            last_name = user.last_name,
            email = user.email,
            password = user.password,
            created_at = user.created_at,
            key = user.key,
        )

    def to_model(self) -> User:
        """
        Converts Self to an instance of a user model.

        Returns:
            User: instance of a user model.
        """
        return User(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            password=self.password,
            created_at=self.created_at,
            key = self.key,
        )

    def update(self, user: User) -> None:
        """
        Updates self using the provided user model.

        Returns:
            None
        """
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.email = user.email
        self.password = user.password


"""API routes for the user module."""

from fastapi import APIRouter, Depends, HTTPException

from ..models.user import User
from ..services.user import UserService
from ..services.exceptions import (InvalidCredentialsUserException,
                                   DuplicateUserException,
                                   UserNotFoundException)

api = APIRouter(prefix="/user")
openapi_tags = {
    "name":"User",
    "description":"User table CRUD properties"   
}

@api.post("/create", tags=["User"])
def create_user(user: User,
                user_service: UserService = Depends(),
                ) -> User:
    """
    Creates a new user in the database
    
    Args:
        first name: The new users first name.
        last name: The new users last name.
        email: The new users email.

    Returns:
        key: The API key for the new user.

    Raises: 
        400: If the input credentials are improperly formatted or invalid.
        409: If the user is already in the database.
    """

    try:
        return user_service.create_user(user=user)
    except InvalidCredentialsUserException as e:
        raise HTTPException(status_code=400, detail=str(e))
    except DuplicateUserException as e:
        raise HTTPException(status_code=409, detail=str(e))
    
@api.post('/login', tags=["User"])
def login(email: str,
          password: str,
          user_service: UserService = Depends(),
        ) -> User:
    """
    Login a user.

    Args:
        email: The email of the user to be logged in.
        password: The password of the user to be logged in.

    Returns:
        User: The user to be logged in.

    Raises:
        404: If the user is not found.
    """

    try:
        return user_service.sign_in(email=email, password=password)
    except UserNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))

@api.get("/get/{key}", tags=["User"])
def get_user(key: str, 
             user_service: UserService = Depends(),) -> User:
    """
    Get the user model with a specified key.
    
    Args:
        key: The key for the user.
        
    Returns:
        User: The user in the database with the specified key.
        
    Raises: 
        404: if the user is not found.
    """
    
    try:
        user: User = user_service.get_user(key=key)
        return user
    except UserNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))

@api.put("/update", tags=["User"])
def get_user(key: str,
             user: User, 
             user_service: UserService = Depends(),) -> User:
    """
    Updates the user model with a specified key.
    
    Args:
        key: The key for the user to be updated.
        user: The user object which has the updated properties
        
    Returns:
        User: The user in the database with the specified key.
    
    Raises:
        404: If the user is not found.
    """
    
    try:
        return user_service.update_user(key=key, user=user)
    except UserNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))

@api.delete("/delete", tags=["User"])
def get_user(key: str, 
             user_service: UserService = Depends(),) -> User:
    """
    Get the user model with a specified key.
    
    Args:
        key: The key for the user.
        
    Returns:
        User: The user in the database with the specified key.
    
    Raises:
        404: If the user is not found.
    """
    
    try:
        return user_service.delete_user(key=key)
    except UserNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))


"""API routes for the plant module."""

from fastapi import Depends, HTTPException, APIRouter

from ..services.plant import PlantService
from ..services.exceptions import (UserBlankKeyException,
                                   UserNotFoundException,
                                   PlantBlankIdException,
                                   PlantNotFoundException,)

from ..models.plant import Plant

api = APIRouter(prefix="/plant")
openapi_tags = {
    "name":"Plant",
    "description":"Routes to interact with API plant functionality."   
}

@api.get("/get_user_plants")
def get_user_plants(key: str, 
                    plant_service: PlantService = Depends()) -> list[Plant]:
    """
    Get all of the plants that belong to a user.
    
    Args:
        key: The key of the user to retrieve plants for.
        
    Returns:
        list[Plant]: A list of the plants that belong to the user.

    Raises:
    
    """
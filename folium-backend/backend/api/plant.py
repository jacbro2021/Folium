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
    "description":"Routes to interact with Plant API functionality."   
}

@api.get("/get_user_plants", tags=["Plant"])
def get_user_plants(key: str, 
                    plant_service: PlantService = Depends()) -> list[Plant]:
    """
    Get all of the plants that belong to a user.
    
    Args:
        key: The key of the user to retrieve plants for.
        
    Returns:
        list[Plant]: A list of the plants that belong to the user.

    Raises:
        404: If the key does not match a user in the database.
        422: If the input key is an empty string.
    """

    try:
        return plant_service.get_all_user_plants(key=key)
    except UserNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except UserBlankKeyException as e:
        raise HTTPException(status_code=422, detail=str(e))
    
@api.post("/create_plant", tags=["Plant"])
def create_plant(plant: Plant,
                 plant_service: PlantService = Depends(),) -> Plant:
    """
    Create a new plant for a user in the database.
    
    Args:
        plant: The plant object to be added to the database.
        
    Returns:
        Plant: The newly created plant object.
        
    Raises:
        404: If the key does not match a user in the database.
        422: If the input key is an empty string.
    """

    try:
        return plant_service.create_plant(plant=plant)
    except UserNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except UserBlankKeyException as e:
        raise HTTPException(status_code=422, detail=str(e))
    
@api.put(path="/update_plant", tags=["Plant"])
def update_plant(plant: Plant,
                 plant_service: PlantService = Depends(),) -> Plant:
    """
    Updates and returns a plant that is already in the database.

    Args:
        plant: The plant to update in the database.
        
    Returns:
        Plant: The updated plant.
        
    Raises:
        404: If the key does not match a user in the database or the plant is not found in the database.
        422: If the input key or plant id is an empty string.
    """

    try:
        plant_service.update_Plant(plant=plant)
    except (UserNotFoundException, PlantNotFoundException) as e:
        raise HTTPException(status_code=404, detail=str(e))
    except (UserBlankKeyException, PlantBlankIdException) as e:
        raise HTTPException(status_code=422, detail=str(e))
    
@api.delete(path="/delete_plant", tags=["Plant"])
def delete_plant(plant: Plant,
                 plant_service: PlantService = Depends()) -> Plant:
    """
    Removes a plant from the database.
    
    Args:
        plant: The plant to delete from the database.
        
    Returns:
        Plant: The plant that was successfully deleted from the database.

    Raises:

    """

    try:
        return plant_service.remove_plant(plant=plant)
    except (UserNotFoundException, PlantNotFoundException) as e:
        raise HTTPException(status_code=404, detail=str(e))
    except (UserBlankKeyException, PlantBlankIdException) as e:
        raise HTTPException(status_code=422, detail=str(e))
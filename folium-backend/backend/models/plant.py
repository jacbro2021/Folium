"""Plant model serves as the data object for representing plants across application layers."""

from fastapi import Basemodel

class PlantIdentity(Basemodel):
    """
    Pydantic model to represent how 'plants' are 
    represented in the system.
    
    This model is based on the 'PlantEntity' which
    defines the shape of the plant table in the postgres
    database."""

    id: int | None = None

class Plant(PlantIdentity, Basemodel):
    """
    Pydantic model to represent how 'plants' are 
    represented in the system.
    
    This model is based on the 'PlantEntity' which
    defines the shape of the plant table in the postgres
    database."""

    common_name: str = ""
    scientific_name: str = ""
    type: str = ""
    cycle: str = ""
    watering: str = ""
    watering_period = ""
    watering_benchmark_value: str = ""
    watering_benchmark_unit: str = ""
    sunlight: str = ""
    pet_poisson: bool = False
    human_poisson: bool = False
    description: str = ""
    image_url: str = ""
    owner_key: str = ""
    last_watering: str = ""
    health_history: list[int] = []

"""Definition of SQLAlchemy backend table to store plant data"""

from .entity_base import EntityBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ARRAY, Float, Boolean

class PlantEntity(EntityBase):
    """Column definitions for the plant table in the database"""

    # The name of the table in the database.
    __tablename__ = "plant"
    
    # Id of the plant.
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Common name for the plant.
    common_name: Mapped[str] = mapped_column(String)
    # Scientific name for the plant.
    scientific_name: Mapped[str] = mapped_column(String)
    # Type of plant.
    type: Mapped[str] = mapped_column(String)
    # The plants cycle.
    cycle: Mapped[str] = mapped_column(String)
    # The frequency that that the plant should be watered.
    watering: Mapped[str] = mapped_column(String)
    # The time of day that the plant should be watered.
    watering_period: Mapped[str] = mapped_column(String)
    # The amount of time that should pass between the plant being watered.
    watering_benchmark_value: Mapped[str] = mapped_column(String)
    # The unit for the watering benchmark value.
    watering_benchmark_unit: Mapped[str] = mapped_column(String)
    # The amount of sunlight that the plant should get.
    sunlight: Mapped[str] = mapped_column(String)
    # true/false poisonous to pets.
    pet_poison: Mapped[bool] = mapped_column(Boolean)
    # True/false poisonous to humans.
    human_poison: Mapped[bool] = mapped_column(Boolean)
    # Description of the plant.
    description: Mapped[str] = mapped_column(String)
    # Url for an image of the plant.
    image_URL: Mapped[str] = mapped_column(String)
    # The key for the owner of the plant.
    owner_key: Mapped[str] = mapped_column(String, nullable=False)
    # Date last watered.
    last_watering: Mapped[str] = mapped_column(String)
    # Health history, where each index is a ranking of the plants health from 1-10.
    health_history: Mapped[list[int]] = mapped_column(ARRAY(Integer))

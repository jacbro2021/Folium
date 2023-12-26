"""Definition of SQLAlchemy backend table to store plant data"""

from .entity_base import EntityBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ARRAY, Float

class PlantEntity(EntityBase):
    """Column definitions for the plant table in the database"""

    # The name of the table in the database.
    __tablename__ = "plant"
    
    # Id of the plant.
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Common name for the plant.
    common_name: Mapped[str] = mapped_column(String)
    # The slug for the plant.
    slug: Mapped[str] = mapped_column(String)
    # The scientific name for the plant.
    scientific_name: Mapped[str] = mapped_column(String)
    # Plant image URL.
    image_url: Mapped[str] = mapped_column(String)
    # The life cycle of the plant.
    duration: Mapped[list[str]] = mapped_column(ARRAY(String))
    # Relative growth rate of the plant (compared to other plants).
    growth_rate: Mapped[str] = mapped_column(String)
    # The predominant shape of the species.
    shape_and_orientation: Mapped[str] = mapped_column(String)
    # Description of how the plant typically grows.
    growth_description: Mapped[str] = mapped_column(String)
    # Max soil PH.
    ph_maximum: Mapped[float] = mapped_column(Float)
    # Min soil PH.
    ph_minimum: Mapped[float] = mapped_column(Float)
    # The amount of light required for the plant on a scale of 1-10
    light: Mapped[int] = mapped_column(Integer)
    # Min precipitation per year in mm.
    minimum_precipitation: Mapped[float] = mapped_column(Float)
    # Max precipitation per year in mm.
    maximum_precipitation: Mapped[float] = mapped_column(Float)
    # Health history with rankings 1-10
    health_history: Mapped[list[int]] = mapped_column(ARRAY(Integer))
    # Number of days in a row that the plant has met its watering reqs.
    watering_streak: Mapped[int] = mapped_column(Integer, nullable=False)
    # The key  of the plants owner.
    owner_key: Mapped[str] = mapped_column(String, nullable=False)

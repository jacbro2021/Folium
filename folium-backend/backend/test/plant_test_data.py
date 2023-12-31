"""Test data for the 'plant_test' tests for the plant service."""

from sqlalchemy.orm import Session
from .reset_table_id_seq import reset_table_id_seq

from ..entities.plant_entity import PlantEntity
from ..entities.user_entity import UserEntity

from datetime import datetime

user1: UserEntity = UserEntity(
    id=0,
    first_name="Jacob",
    last_name="Brown",
    email="jacobbrown@gmail.com",
    password="password",
    created_at="",
    key="user1"
)

user2: UserEntity = UserEntity(
    first_name="Lebron",
    last_name="James",
    email="SecondGreatestOfAllTime@hotmail.com",
    password="password2",
    created_at="",
    key="user2"
)

plant1 = PlantEntity(
    id=0,
    common_name="fake",
    scientific_name="fake",
    type="fake",
    cycle="fake",
    watering="fake",
    watering_period="fake",
    watering_benchmark_unit="fake",
    watering_benchmark_value="fake",
    sunlight="fake",
    pet_poison=False,
    human_poison=True,
    description="fake",
    image_url="fake",
    owner_key="user1",
    last_watering="fake",
    health_history=list(),
)

plant2 = PlantEntity(
    id=1,
    common_name="fake",
    scientific_name="fake",
    type="fake",
    cycle="fake",
    watering="fake",
    watering_period="fake",
    watering_benchmark_unit="fake",
    watering_benchmark_value="fake",
    sunlight="fake",
    pet_poison=False,
    human_poison=True,
    description="fake",
    image_url="fake",
    owner_key="user2",
    last_watering="fake",
    health_history=list(),
)

users = [user1, user2]

plants = [plant1, plant2]

def insert_test_data(session: Session):
    """Insert fake data for testing."""
    
    # Add users to db.
    for user in users:
        session.add(user)

    # Add plants to db.
    for plant in plants:
        session.add(plant)

    reset_table_id_seq(session=session, entity=PlantEntity, entity_id_column=PlantEntity.id, next_id=len(plants))


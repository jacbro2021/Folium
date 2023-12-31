"""Test data for the 'plant_test' tests for the plant service."""

from sqlalchemy.orm import Session
from .reset_table_id_seq import reset_table_id_seq

from ..models.user import User
from ..entities.user_entity import UserEntity
from ..models.plant import Plant
from ..entities.plant_entity import PlantEntity

user1 = User(
    id=0,
    first_name="jacob",
    last_name="brown",
    email="test@gmail.com",
    password="test",
    created_at="",
    key="user1"
)

user2 = User(
    id=1,
    first_name="Lebron",
    last_name="James",
    email="SecondGreatestOfAllTime@hotmail.com",
    password="password2",
    created_at="",
    key="user2"
)

plant1 = Plant(
    id=0,
    common_name="test1",
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

plant2 = Plant(
    id=1,
    common_name="test2",
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
        new_user = UserEntity.from_model(user=user)
        session.add(new_user)

    # Add plants to db.
    for plant in plants:
        new_plant = PlantEntity.from_model(plant=plant)
        session.add(new_plant)

    ent = session.query(UserEntity).all()

    reset_table_id_seq(session=session, entity=UserEntity, entity_id_column=UserEntity.id, next_id=len(users) + 1)
    reset_table_id_seq(session=session, entity=PlantEntity, entity_id_column=PlantEntity.id, next_id=len(plants) + 1)


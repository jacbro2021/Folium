"""Unit tests for the plant service"""

import pytest
from sqlalchemy.orm import Session
from .plant_test_data import insert_test_data

from ..services.exceptions import (UserNotFoundException,
                                   PlantNotFoundException,
                                   UserBlankKeyException,
                                   PlantBlankIdException,)

from ..services.plant import PlantService
from ..models.plant import Plant

@pytest.fixture(autouse=True, scope="function")
def plant_service(session: Session):
    """This PyTest fixture is injected into each test parameter of the same name below.
    It constructs a new, empty PlantService object."""
    insert_test_data(session)
    session.commit()
    plant_service = PlantService(session=session)
    return plant_service

def test_get_all_user_plants(plant_service: PlantService):
    """Test basic usage for get all user plants service method"""

    plants = plant_service.get_all_user_plants("user1")
    assert len(plants) == 1
    assert plants[0].common_name == "test1"


def test_get_all_user_plants_correct_plants(plant_service: PlantService):
    """Test that get all user plants service method returns the correct plants"""

    plants = plant_service.get_all_user_plants("user1")
    assert len(plants) == 1
    assert plants[0].common_name != "test2"

def test_get_all_user_plants_nonexistent_user(plant_service: PlantService):
    """Test that an exception is thrown when a nonexistent user is input"""

    try:
        plant_service.get_all_user_plants("user3")
        pytest.fail()
    except UserNotFoundException:
        assert True

def test_create_plant(plant_service: PlantService):
    """Tests create plant service method basic usage."""

    plant = Plant(
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
        health_history=[],
    )
    plant_service.create_plant(plant=plant)

def test_create_plant_nonexistent_owner(plant_service: PlantService):
    """Tests that an exception is raised when a plant is created with a nonexistent owner key."""

    plant = Plant(
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
        owner_key="None",
        last_watering="fake",
        health_history=[],
    )

    try:
        plant_service.create_plant(plant=plant)
        pytest.fail()
    except UserNotFoundException:
        assert True

def test_remove_plant(plant_service: PlantService):
    """Tests basic functionality of remove plant service method."""

    plant = Plant(owner_key="user1")
    plant = plant_service.create_plant(plant=plant)
    assert len(plant_service.get_all_user_plants("user1")) == 2
    plant_service.remove_plant(plant=plant)
    assert len(plant_service.get_all_user_plants("user1")) == 1

def test_remove_other_user_plant(plant_service: PlantService):
    """Tests that a user cannot remove another users plants."""

    plant = Plant(id=0, owner_key="user2")
    try:
        plant_service.remove_plant(plant=plant)
        pytest.fail()
    except PlantNotFoundException:
        assert True

def test_remove_nonexistent_plant(plant_service: PlantService):
    """Tests that an error is thrown when remove plant is called on a plant that is not in the db."""
    
    plant = Plant(id=3, owner_key="user1")
    try:
        plant_service.remove_plant(plant=plant)
        pytest.fail()
    except PlantNotFoundException:
        assert True

def test_remove_plant_nonexistent_owner(plant_service: PlantService):
    """Tests that an error is thrown when a plant is removed with an owner key that does not exist"""

    plant = Plant(id=3, owner_key="Test")
    try:
        plant_service.remove_plant(plant=plant)
        pytest.fail()
    except UserNotFoundException:
        assert True

def test_remove_plant_blank_owner(plant_service: PlantService):
    """Tests that an error is thrown when a plant is removed that has a blank owner key."""
    
    try:
        plant_service.remove_plant(Plant())
        pytest.fail()
    except UserBlankKeyException:
        assert True

def test_update_plant(plant_service: PlantService):
    """Test basic usage of update plant service method."""

    plant = Plant(id=0, common_name="not fake", owner_key="user1")
    plant = plant_service.create_plant(plant=plant)
    plant.common_name = "super fake"
    updated_plant = plant_service.update_Plant(plant=plant)
    assert updated_plant.common_name == "super fake"

def test_update_plant_nonexistent_owner(plant_service: PlantService):
    """Test that an exception is raised when a plant is updated with a nonexistent owner."""

    plant = Plant(id=0, owner_key="fake")

    try:
        plant_service.update_Plant(plant=plant)
        pytest.fail()
    except UserNotFoundException:
        assert True

def test_update_plant_nonexistent_plant(plant_service: PlantService):
    """Test that an exception is raised when a plant is updated that does not exist for an owner"""

    plant = Plant(id=0, owner_key="user2")

    try:
        plant_service.update_Plant(plant=plant)
        pytest.fail()
    except:
        assert True
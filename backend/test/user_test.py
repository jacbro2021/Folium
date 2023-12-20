"""Tests for the user service"""

import pytest
from sqlalchemy.orm import Session

from ..services.user import UserService
from ..models.user import User
from ..services.exceptions import (UserNotFoundException,
                                   DuplicateUserException,
                                   InvalidCredentialsUserException)

@pytest.fixture(autouse=True)
def user_service(session: Session):
    """This PyTest fixture is injected into each test parameter of the same name below.
    It constructs a new, empty UserService object."""
    user_service = UserService(session=session)
    return user_service

def test_create_user(user_service: UserService):
    """Tests that a user can be created and the key is returned"""
    key = user_service.create_user(first_name="Jacob", last_name="Brown", email="email")
    assert key

def test_create_multiple_users(user_service: UserService):
    """Tests that multiple users can be created with unique keys"""
    key = user_service.create_user(first_name="Jacob", last_name="Brown", email="email")
    key2 = user_service.create_user(first_name="polly", last_name="dartin", email="email2")
    assert key
    assert key2
    assert key != key2

def test_create_user_empty_property(user_service: UserService):
    try:
        key = user_service.create_user()
        pytest.fail()
    except InvalidCredentialsUserException:
        assert True

def test_create_duplicate_users(user_service: UserService):
    try:
        key = user_service.create_user(first_name="Jacob", last_name="Brown", email="email")
        key2 = user_service.create_user(first_name="Jacob", last_name="Brown", email="email")
        pytest.fail()
    except DuplicateUserException:
        assert True

def test_get_user(user_service: UserService):
    """Tests get user basic usage"""
    key = user_service.create_user(first_name="Jacob", last_name="Brown", email="email")
    user = user_service.get_user(key=key)
    assert user.key == key

def test_get_user_does_not_exist(user_service: UserService):
    """Tests get user raises an exception when called with a key that is not in the database."""
    try:
        user_service.get_user(key="0")
        pytest.fail()
    except UserNotFoundException: 
        assert True

def test_get_user_multiple_users(user_service: UserService):
    """Tests that get user returns the correct user when there are multiple users in the database."""
    key = user_service.create_user(first_name="Jacob", last_name="Brown", email="email")
    key2 = user_service.create_user(first_name="Jim", last_name="Beam", email="email2")
    user = user_service.get_user(key=key2)
    assert user.key == key2

def test_update_user(user_service: UserService):
    """Tests that update user functions properly."""
    key = user_service.create_user(first_name="Jacob", last_name="Brown", email="email")
    user = user_service.get_user(key=key)
    user.first_name = "Jimmy"
    user2 = user_service.update_user(key=key, user=user)
    assert user2.first_name == user.first_name

def test_update_user_multiple_users(user_service: UserService):
    """Tests that the correct user is updated when multiple users are in the database."""
    key = user_service.create_user(first_name="Jacob", last_name="Brown", email="email")
    key2 = user_service.create_user(first_name="Jacob", last_name="Brown", email="email2")
    user = user_service.get_user(key=key)
    user.first_name = "John"
    user.last_name = "Jim"
    user2 = user_service.update_user(key=key, user=user)
    assert user2.first_name == user.first_name
    assert user2.last_name == user.last_name

def test_update_user_not_found(user_service: UserService):
    """Tests that an exception is raised when a user is updated that is not in the database"""
    user = User(id=0, first_name="Jim", last_name="John", email="raa", created_at="ur mom", key="0")
    
    try: 
        user_service.update_user(key="0", user=user)
        pytest.fail()
    except UserNotFoundException:
        assert True

def test_delete_user(user_service: UserService):
    """Tests delete user basic usage"""
    key = user_service.create_user(first_name="Jacob", last_name="Brown", email="email")
    user_service.delete_user(key=key)

    try:
        user_service.get_user(key=key)
        pytest.fail()
    except UserNotFoundException:
        assert True

def test_delete_user_multiple_users(user_service: UserService):
    """Tests that delete user only deletes the user with the specified key"""
    key = user_service.create_user(first_name="Jacob", last_name="Brown", email="email")
    key2 = user_service.create_user(first_name="Jacob", last_name="Brown", email="email2")
    user_service.delete_user(key=key)
    user_service.get_user(key=key2)
    assert True

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
    user = User(first_name="Jacob",
                last_name="Brown",
                email="jacobbrown2002@gmail.com",
                password="password")
    key = user_service.create_user(user=user)
    assert key

def test_create_multiple_users(user_service: UserService):
    """Tests that multiple users can be created with unique keys"""
    user = User(first_name="Jacob",
                last_name="Brown",
                email="jacobbrown2002@gmail.com",
                password="password")
    user2 = User(first_name="Jackson",
                last_name="Brown",
                email="test@gmail.com",
                password="password2")
    model = user_service.create_user(user)
    model2 = user_service.create_user(user2)
    assert model
    assert model2

def test_create_user_empty_property(user_service: UserService):
    try:
        user = User(first_name="Jacob",
                last_name="Brown",
                email="jacobbrown2002@gmail.com",
                password="")
        user_service.create_user(user=user)
        pytest.fail()
    except InvalidCredentialsUserException:
        assert True

def test_create_duplicate_users(user_service: UserService):
    try:
        user = User(first_name="Jacob",
                last_name="Brown",
                email="jacobbrown2002@gmail.com",
                password="password")
        key = user_service.create_user(user = user)
        key2 = user_service.create_user(user = user)
        pytest.fail()
    except DuplicateUserException:
        assert True

def test_sign_in(user_service: UserService):
    """Test sign in basic usage"""
    user = User(first_name="Jacob",
                last_name="Brown",
                email="jacobbrown2002@gmail.com",
                password="password")
    user = user_service.create_user(user)
    user2 = user_service.sign_in(email=user.email, password=user.password)
    assert user2.key == user.key

def test_sign_in_not_found(user_service: UserService):
    user = User(first_name="Jacob",
                last_name="Brown",
                email="jacobbrown2002@gmail.com",
                password="password")
    try:
        user_service.sign_in(email=user.email, password=user.password)
        pytest.fail()
    except UserNotFoundException:
        assert True

def test_get_user(user_service: UserService):
    """Tests get user basic usage"""
    user = User(first_name="Jacob",
                last_name="Brown",
                email="jacobbrown2002@gmail.com",
                password="password")
    new_user: User = user_service.create_user(user = user)
    user2: User = user_service.get_user(key=new_user.key)
    assert user2.key == new_user.key

def test_get_user_does_not_exist(user_service: UserService):
    """Tests get user raises an exception when called with a key that is not in the database."""
    try:
        user_service.get_user(key="0")
        pytest.fail()
    except UserNotFoundException: 
        assert True

def test_update_user(user_service: UserService):
    """Tests that update user functions properly."""
    user = User(first_name="Jacob",
                last_name="Brown",
                email="jacobbrown2002@gmail.com",
                password="password")
    user = user_service.create_user(user=user)
    user.first_name = "Jimmy"
    user2 = user_service.update_user(key=user.key, user=user)
    assert user2.first_name == user.first_name

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
    user = User(first_name="Jacob",
                last_name="Brown",
                email="jacobbrown2002@gmail.com",
                password="password")
    user = user_service.create_user(user=user)
    user_service.delete_user(key=user.key)
    assert True

def test_delete_nonexistent_user(user_service: UserService):
    """Tests that an exception is thrown when a user that does not exist is deleted."""
    try:
        user_service.delete_user("0")
        pytest.fail()
    except UserNotFoundException:
        assert True
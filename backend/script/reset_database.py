"""Reset Database"""


from ..entities.user_entity import  EntityBase
import sqlalchemy
import os
import dotenv

# Load envirnment variables from .env file upon module start.
dotenv.load_dotenv(verbose=True)


def getenv(variable: str) -> str:
    """Get value of environment variable or raise an error if undefined.

    Unlike `os.getenv`, our application expects all environment variables it needs to be defined
    and we intentionally fast error out with a diagnostic message to avoid scenarios of running
    the application when expected environment variables are not set.
    """
    value = os.getenv(variable)
    if value is not None:
        return value
    else:
        raise NameError(f"Error: {variable} Environment Variable not Defined")

def _engine_str() -> str:
    """Helper function for reading settings from environment variables to produce connection string."""
    dialect = "postgresql+psycopg2"
    user = getenv("POSTGRES_USER")
    password = getenv("POSTGRES_PASSWORD")
    host = getenv("POSTGRES_HOST")
    port = getenv("POSTGRES_PORT")
    return f"{dialect}://{user}:{password}@{host}:{port}"


engine = sqlalchemy.create_engine(_engine_str(), echo=True)
"""Application-level SQLAlchemy database engine."""

EntityBase.metadata.drop_all(engine)
EntityBase.metadata.create_all(engine)
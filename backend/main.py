"""Entrypoint of backend API exposing the FastAPI `app` to be served by an application server such as uvicorn."""


from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .api import (
    user,
)
from .api import user
from .database import _engine_str

description = """
Welcome to the Folium RESTful application programming interface
"""

# Metadata to improve the usefulness of OpenAPI Docs /docs API Explorer
app = FastAPI(
    title="Folium API",
    version="0.0.1",
    description=description,
    openapi_tags=[
        user.openapi_tags,
    ],
)

# Plugging in each of the router APIs
feature_apis = [
    user
]

for feature_api in feature_apis:
    app.include_router(feature_api.api)
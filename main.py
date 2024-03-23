from database import get_db  # Absolute import
from fastapi import FastAPI
from schema import (create_todo, delete_todo, query,  # Absolute import
                    update_todo)
from starlette.middleware.cors import CORSMiddleware
from strawberry.asgi import GraphQL

# Create FastAPI app
app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware=["*"],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount GraphQL app
schema = query
schema.mutation(create_todo)
schema.mutation(update_todo)
schema.mutation(delete_todo)
app.add_route("/graphql", GraphQL(schema))

# Startup and shutdown events


@app.on_event("startup")
async def startup_event():
    await get_db.connect()


@app.on_event("shutdown")
async def shutdown_event():
    await get_db.disconnect()

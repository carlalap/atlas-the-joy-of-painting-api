""" Driver program for application """
from api.episodes import models, views
from engine.db import engine, sessionmaker
from fastapi import FastAPI


models.Base.metadata.create_all(bind=engine)
sessionmaker = sessionmaker(bind=engine)
session = sessionmaker()

# Create new FastAPI instance
app = FastAPI()

# Bind routes to views as seen in api/episodes/views.py
app.include_router(views.router)

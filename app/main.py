# app/main.py
from fastapi import FastAPI
from app.api.notifications import router as notifications


from app.db.database import engine, Base

app = FastAPI(debug=True)

# Use the `notifications` object directly without accessing `router` attribute
app.include_router(notifications, prefix="/v1")

# This should be done at the end of the file
Base.metadata.create_all(bind=engine)

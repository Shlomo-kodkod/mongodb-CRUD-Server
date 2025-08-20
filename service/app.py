from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import logging
import uvicorn
from service.data_loader.dal import DAL
from service.model import Soldier



app = FastAPI()
logger = logging.getLogger(__name__)
dal = DAL()

class SoldierFields(BaseModel):
    soldier_id: int
    first_name: str
    last_name: str
    phon_number: str
    rank: str 

class SoldierOptional(BaseModel):
    soldier_id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phon_number: Optional[str] = None
    rank: Optional[str]  = None


@app.get("/")
def get_names():
    """
    Endpoint to return a welcome message.
    """
    return JSONResponse(content={"message": "Welcome to the MongoDB CRUD Server!"})

@app.post("/create")
def create_soldier(soldier: SoldierFields):
    """
    Endpoint to create a new soldier.
    """
    try:
        soldier = Soldier(soldier.soldier_id, soldier.first_name, soldier.last_name, soldier.phon_number, soldier.rank)
        dal.create_soldier(soldier)
        return JSONResponse(content={"message": "Soldier created successfully"})
    except Exception as e:
        logger.error(f"Error creating soldier: {e}")
        return JSONResponse(content={"message": "Failed to create soldier"})
    
@app.get("/read")
def get_soldiers():
    """
    Endpoint to read collection.
    """
    try:
        soldiers = dal.read_collection()
        if soldiers:
            return JSONResponse(content={"soldiers": soldiers})
        else:
            return JSONResponse(content={"message": "Collection not found"})
    except Exception as e:
        logger.error(f"Error reading collection: {e}")
        return JSONResponse(content={"message": "Failed to read collection"})

@app.put("/update")
def update_soldier(soldier: SoldierOptional):
    """
    Endpoint to update a soldier's details.
    """
    try:
        result = dal.update_soldier(soldier.soldier_id, soldier.model_dump(exclude_none=True))
        if result:
            return JSONResponse(content={"message": "Soldier updated successfully"})
        else:
            return JSONResponse(content={"message": "Soldier not found or no changes made"})
    except Exception as e:
        logger.error(f"Error updating soldier: {e}")
        return JSONResponse(content={"message": "Failed to update soldier"})

@app.delete("/delete/{soldier_id}")
def delete_soldier(soldier_id: int):
    """
    Endpoint to delete a soldier.
    """
    try:
        result = dal.delete_soldier(soldier_id)
        if result:
            return JSONResponse(content={"message": "Soldier deleted successfully"})
        else:
            return JSONResponse(content={"message": "Soldier not found"})
    except Exception as e:
        logger.error(f"Error deleting soldier: {e}")
        return JSONResponse(content={"message": "Failed to delete soldier"})



from app.models import SubMenu
from app.db import get_db
from app.schemas import CreateSubMenu, SubMenuInfo

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from app.routers import crud

router = APIRouter()

@router.get("/", response_model=list[SubMenuInfo])
def get_submenu(target_menu_id: str, db: Session = Depends(get_db)):
    return crud.get_submenu(target_menu_id, db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model= SubMenuInfo)
def create_submenu(details: CreateSubMenu, target_menu_id: str, db: Session = Depends(get_db)):
    return crud.create_submenu(details, target_menu_id, db)


@router.get("/{id}", response_model=SubMenuInfo)
def get_submenu_by_id(id: str, db: Session = Depends(get_db)):
    return crud.get_submenu_by_id(id, db)


@router.delete("/{id}")
def delete_submenu(id: str, db: Session = Depends(get_db)):
    return crud.delete_submenu(id, db)


@router.patch("/{id}", response_model=SubMenuInfo)
def update_submenu(id: str, menu: CreateSubMenu, db: Session = Depends(get_db)):
    return crud.update_submenu(id, menu, db)






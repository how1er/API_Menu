from app.db import get_db
from app.schemas import CreateSubMenu, SubMenuInfo

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from app.cache import get_cache, AbstractCache
from app.routers import service

router = APIRouter()


@router.get("/", response_model=list[SubMenuInfo])
def get_submenu(
    target_menu_id: str,
    db: Session = Depends(get_db),
    cache: AbstractCache = Depends(get_cache),
):
    return service.get_submenu(target_menu_id, db, cache)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SubMenuInfo)
def create_submenu(
    details: CreateSubMenu,
    target_menu_id: str,
    db: Session = Depends(get_db),
    cache: AbstractCache = Depends(get_cache),
):
    return service.create_submenu(details, target_menu_id, db, cache)


@router.get("/{id}", response_model=SubMenuInfo)
def get_submenu_by_id(
    id: str, db: Session = Depends(get_db), cache: AbstractCache = Depends(get_cache)
):
    return service.get_submenu_by_id(id, db, cache)


@router.delete("/{id}")
def delete_submenu(
    id: str, db: Session = Depends(get_db), cache: AbstractCache = Depends(get_cache)
):
    return service.delete_submenu(id, db, cache)


@router.patch("/{id}", response_model=SubMenuInfo)
def update_submenu(
    id: str,
    menu: CreateSubMenu,
    db: Session = Depends(get_db),
    cache: AbstractCache = Depends(get_cache),
):
    return service.update_submenu(id, menu, db, cache)

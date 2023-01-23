from app.schemas import MenuInfo, CreateMenu
from app.models import Menu
from app.db import get_db

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter()

@router.get("/", response_model= list[MenuInfo])
def get_menu(db: Session = Depends(get_db)):
    return db.query(Menu).all()

@router.get("/{id}", response_model = MenuInfo)
def get_menu_by_id(id: str, db: Session = Depends(get_db)):
    stored_menu = db.query(Menu).filter(Menu.id == id).first()
    if not stored_menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'menu not found')
    return stored_menu


@router.post("/", status_code=status.HTTP_201_CREATED, response_model = MenuInfo)
def create_menu(details: CreateMenu, db: Session = Depends(get_db), ):
    to_create = Menu(
        title=details.title,
        description = details.description 
    )
    db.add(to_create)
    db.commit()
    return to_create

@router.delete("/")
def delete_menu(db: Session = Depends(get_db)):
    db.query(Menu).delete()
    db.commit()
    return { "success": True }

@router.delete("/{id}")
def delete_menu(id: str, db: Session = Depends(get_db)):
    db.query(Menu).filter(Menu.id == id).delete()
    db.commit()
    return { "success": True }

@router.patch("/{id}", response_model=MenuInfo)
def update_menu(id: str, menu: CreateMenu, db: Session = Depends(get_db)):
    menu_query = db.query(Menu).filter(Menu.id == id)
    stored_menu = menu_query.first()
    if not stored_menu:
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f'No menu with this id: {id} found')
    update_data = menu.dict(exclude_unset=True)
    menu_query.filter(Menu.id == id).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(stored_menu)
    return stored_menu



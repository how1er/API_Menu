from app.schemas import MenuInfo, CreateMenu, SubMenuInfo, CreateSubMenu, DishInfo, CreateDish
from app.models import Menu, SubMenu, Dish
from app.db import get_db

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from app.routers import crud

def get_menu(db):
    return db.query(Menu).all()


def get_menu_by_id(id: str, db: Session):
    stored_menu = db.query(Menu).filter(Menu.id == id).first()
    if not stored_menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'menu not found')
    return stored_menu


def create_menu(details: CreateMenu, db: Session ):
    to_create = Menu(
        title=details.title,
        description = details.description 
    )
    db.add(to_create)
    db.commit()
    return to_create
    

def delete_menu(id, db):
    db.query(Menu).filter(Menu.id == id).delete()
    db.commit()
    return { "success": True }    


def update_menu(id, menu, db):
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


def get_submenu(target_menu_id, db):
    return db.query(SubMenu).filter(SubMenu.menu_id == target_menu_id).all()


def create_submenu(details, target_menu_id, db):
    to_create = SubMenu(
        menu_id = target_menu_id,
        title=details.title,
        description = details.description
    )
    db.add(to_create)
    db.commit()
    return to_create


def get_submenu_by_id(id, db):
    stored_submenu = db.query(SubMenu).filter(SubMenu.id == id).first()
    if not stored_submenu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'submenu not found')
    return stored_submenu


def delete_submenu(id, db):
    db.query(SubMenu).filter(SubMenu.id == id).delete()
    db.commit()
    return { "success": True }


def update_submenu(id, menu, db):
    menu_query = db.query(SubMenu).filter(SubMenu.id == id)
    stored_submenu = menu_query.first()
    if not stored_submenu:
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f'No submenu with this id: {id} found')
    update_data = menu.dict(exclude_unset=True)
    menu_query.filter(SubMenu.id == id).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(stored_submenu)
    return stored_submenu


def get_dish(target_submenu_id, db):
    return db.query(Dish).filter(Dish.submenu_id == target_submenu_id).all()


def create_dish(details, target_submenu_id, db):
    to_create = Dish(
        submenu_id = target_submenu_id,
        title=details.title,
        description = details.description,
        price = details.price
    )
    db.add(to_create)
    db.commit()
    return to_create


def get_dish_by_id(id, db):
    stored_dish = db.query(Dish).filter(Dish.id == id).first()
    if not stored_dish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'dish not found')
    return stored_dish


def delete_dish(id, db):
    db.query(Dish).filter(Dish.id == id).delete()
    db.commit()
    return { "success": True }


def update_dish(id, dish, db):
    dish_query = db.query(Dish).filter(Dish.id == id)
    stored_dish = dish_query.first()
    if not stored_dish:
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f'No dish with this id: {id} found')
    update_data = dish.dict(exclude_unset=True)
    dish_query.filter(Dish.id == id).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(stored_dish)
    return stored_dish

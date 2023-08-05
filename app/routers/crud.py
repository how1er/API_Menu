from app.models import Menu, SubMenu, Dish
from fastapi import HTTPException, status


def get_menus(db):
    return db.query(Menu).all()


def create_menu(details, db):
    to_create = Menu(title=details.title, description=details.description)
    db.add(to_create)
    db.commit()
    return to_create


def get_menu_by_id(id, db):
    stored_menu = db.query(Menu).filter(Menu.id == id).first()
    if not stored_menu:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="menu not found"
        )
    return stored_menu


def delete_menu_by_id(id, db):
    db.query(Menu).filter(Menu.id == id).delete()
    db.commit()
    return {"success": True}


def update_menu_by_id(id, menu, db):
    menu_query = db.query(Menu).filter(Menu.id == id)
    stored_menu = menu_query.first()
    if not stored_menu:
        raise HTTPException(
            status_code=status.HTTP_200_OK, detail=f"No menu with this id: {id} found"
        )
    update_data = menu.dict(exclude_unset=True)
    menu_query.filter(Menu.id == id).update(
        update_data, synchronize_session=False)
    db.commit()
    db.refresh(stored_menu)
    return stored_menu


def get_submenus(target_menu_id, db):
    return db.query(SubMenu).filter(SubMenu.menu_id == target_menu_id).all()


def create_submenu(details, target_menu_id, db):
    to_create = SubMenu(
        menu_id=target_menu_id, title=details.title, description=details.description
    )
    db.add(to_create)
    db.commit()
    return to_create


def get_submenu_by_id(id, db):
    stored_submenu = db.query(SubMenu).filter(SubMenu.id == id).first()
    if not stored_submenu:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="submenu not found"
        )
    return stored_submenu


def delete_submenu_by_id(id, db):
    db.query(SubMenu).filter(SubMenu.id == id).delete()
    db.commit()
    return {"success": True}


def update_submenu_by_id(id, new_data, db):
    submenu_query = db.query(SubMenu).filter(SubMenu.id == id)
    stored_submenu = submenu_query.first()
    if not stored_submenu:
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail=f"No submenu with this id: {id} found",
        )
    update_data = new_data.dict(exclude_unset=True)
    submenu_query.filter(SubMenu.id == id).update(
        update_data, synchronize_session=False)
    db.commit()
    db.refresh(stored_submenu)
    return stored_submenu


def get_dishes(target_submenu_id, db):
    return db.query(Dish).filter(Dish.submenu_id == target_submenu_id).all()


def create_dish(details, target_submenu_id, db):
    to_create = Dish(
        submenu_id=target_submenu_id,
        title=details.title,
        description=details.description,
        price=details.price,
    )
    db.add(to_create)
    db.commit()
    return to_create


def get_dish_by_id(id, db):
    stored_dish = db.query(Dish).filter(Dish.id == id).first()
    if not stored_dish:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="dish not found"
        )
    return stored_dish


def delete_dish_by_id(id, db):
    db.query(Dish).filter(Dish.id == id).delete()
    db.commit()
    return {"success": True}


def update_dish_by_id(id, dish, db):
    dish_query = db.query(Dish).filter(Dish.id == id)
    stored_dish = dish_query.first()
    if not stored_dish:
        raise HTTPException(
            status_code=status.HTTP_200_OK, detail=f"No dish with this id: {id} found"
        )
    update_data = dish.dict(exclude_unset=True)
    dish_query.filter(Dish.id == id).update(
        update_data, synchronize_session=False)
    db.commit()
    db.refresh(stored_dish)
    return stored_dish

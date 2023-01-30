from app.routers import crud
from app.routers import crud_cache


def create_menu(
    menu,
    db,
    cache,
):
    new_menu = crud.create_menu(menu, db)
    answer = make_menu_answer(new_menu)
    crud_cache.set_item(cache, type_="menu", item=answer)
    crud_cache.delete_list(cache, "menus")
    return answer


def delete_menu(menu_id, db, cache):
    result = crud.delete_menu(menu_id, db)
    crud_cache.delete(cache, type_="menu", id_=menu_id)
    crud_cache.delete_list(cache, "menus")
    return result


def get_menu_by_id(menu_id, db, cache):
    cached_menu = crud_cache.get_item(cache, type_="menu", id_=menu_id)
    if cached_menu:
        return cached_menu
    menu = crud.get_menu_by_id(menu_id, db)
    if menu:
        answer = make_menu_answer(menu)
        crud_cache.set_item(cache, type_="menu", item=answer)
        return answer


def get_menu(db, cache):
    cached_menus = crud_cache.get_list(cache, "menus")
    if cached_menus:
        return cached_menus

    menus = crud.get_menu(db)
    menus_list = [make_menu_answer(menu) for menu in menus]
    crud_cache.set_list(cache, "menus", menus_list)
    return menus_list


def update_menu(menu_id, new_data, db, cache):
    menu = crud.update_menu(menu_id, new_data, db)
    if menu:
        answer = make_menu_answer(menu)
        crud_cache.set_item(cache, type_="menu", item=answer)
        crud_cache.delete_list(cache, "menus")
        return answer


def make_menu_answer(menu):
    return {
        "id": str(menu.id),
        "title": menu.title,
        "description": menu.description,
        "submenus_count": len(menu.submenus),
        "dishes_count": sum([len(submenu.dishes) for submenu in menu.submenus])
        if menu.submenus
        else 0,
    }


def create_submenu(menu_id, submenu, db, cache):
    submenu = crud.create_submenu(db, submenu)
    if submenu:
        answer = make_submenu_answer(submenu)
        crud_cache.set_item(cache, type_="submenu", item=answer)
        crud_cache.delete_list(cache, "submenus")
        crud_cache.delete_list(cache, "menus")
        crud_cache.delete(cache, type_="menu", id_=menu_id)
        return answer


def delete_submenu(db, cache, menu_id, submenu_id):
    result = crud.delete_submenu_by_id(db, id_=submenu_id)
    crud_cache.delete(cache, type_="submenu", id_=submenu_id)
    crud_cache.delete_list(cache, "submenus")
    crud_cache.delete_list(cache, "menus")
    crud_cache.delete(cache, type_="menu", id_=menu_id)

    return result


def get_submenu_by_id(submenu_id, db, cache):
    cached_submenu = crud_cache.get_item(cache, type_="submenu", id_=submenu_id)
    if cached_submenu:
        return cached_submenu
    submenu = crud.get_submenu_by_id(db, d_=submenu_id)
    if submenu:
        answer = make_submenu_answer(submenu)
        crud_cache.set_item(cache, type_="submenu", item=answer)
        return answer


def get_submenu(menu_id, db, cache):
    cached_submenus = crud_cache.get_list(cache, "submenus")
    if cached_submenus:
        return cached_submenus
    submenus = crud.get_submenu(db, menu_id=menu_id)
    submenus_list = [make_submenu_answer(submenu) for submenu in submenus]
    crud_cache.set_list(cache, key="submenus", items=submenus_list)
    return submenus_list


def update_submenu(submenu_id, new_data, db, cache):
    submenu = crud.update_submenu(submenu_id, new_data, db)
    if submenu:
        answer = make_submenu_answer(submenu)
        crud_cache.set_item(cache, type_="submenu", item=answer)
        crud_cache.delete_list(cache, "submenus")
        return answer


def create_dish(dish, submenu_id, db, cache):
    dish = crud.create_dish(dish, submenu_id, db)

    if dish:
        answer = make_dish_answer(dish)
        crud_cache.set_item(cache, type_="dish", item=answer)
        crud_cache.delete_list(cache, "submenus")
        crud_cache.delete_list(cache, "menus")
        crud_cache.delete_list(cache, "dishes")
        crud_cache.delete(cache, type_="submenu", id_=submenu_id)
        return answer


def delete_dish(menu_id, submenu_id, dish_id, db, cache):
    result = crud.delete_dish(db, dish_id=dish_id)
    crud_cache.delete_list(cache, "submenus")
    crud_cache.delete_list(cache, "menus")
    crud_cache.delete_list(cache, "dishes")
    crud_cache.delete(cache, type_="menu", id_=menu_id)
    crud_cache.delete(cache, type_="submenu", id_=submenu_id)
    crud_cache.delete(cache, type_="dish", id_=dish_id)

    return result


def get_dish(dish_id, db, cache):
    cached_dish = crud_cache.get_item(cache, type_="dish", id_=dish_id)
    if cached_dish:
        return cached_dish
    dish = crud.get_dish(db, dish_id=dish_id)

    if dish:
        answer = make_dish_answer(dish)
        crud_cache.set_item(cache, type_="dish", item=answer)
        return answer


def get_dish_by_id(submenu_id, db, cache):
    cached_dishes = crud_cache.get_list(cache, "dishes")
    if cached_dishes:
        return cached_dishes
    dishes = crud.get_dish_by_id(db, submenu_id=submenu_id)
    dishes_list = [make_dish_answer(dish) for dish in dishes]
    crud_cache.set_list(cache, "dishes", dishes_list)
    return dishes_list


def update_dish(dish_id, new_data, db, cache):
    dish = crud.update_dish(db, new_data)

    if dish:
        answer = make_dish_answer(dish)
        crud_cache.set_item(cache, type_="dish", item=answer)
        crud_cache.delete_list(cache, "dishes")


def make_dish_answer(dish):
    return {
        "id": str(dish.id),
        "title": dish.title,
        "description": dish.description,
        "price": str(dish.price),
    }


def make_submenu_answer(submenu):
    return {
        "id": str(submenu.id),
        "title": submenu.title,
        "description": submenu.description,
        "dishes_count": len(submenu.dishes),
    }

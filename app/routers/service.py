from app.routers import crud
from app.routers import crud_cache


def get_menus(db, cache):
    cached_menus = crud_cache.get_list(cache, key="menus")
    if cached_menus:
        return cached_menus

    menus = crud.get_menus(db)
    menus_list = [make_menu_answer(menu) for menu in menus]
    crud_cache.set_list(cache, "menus", menus_list)
    return menus_list


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


def get_menu_by_id(menu_id, db, cache):
    cached_menu = crud_cache.get_item(cache, type_="menu", id_=menu_id)
    if cached_menu:
        return cached_menu
    menu = crud.get_menu_by_id(menu_id, db)
    if menu:
        answer = make_menu_answer(menu)
        crud_cache.set_item(cache, type_="menu", item=answer)
        return answer


def delete_menu_by_id(menu_id, db, cache):
    result = crud.delete_menu_by_id(menu_id, db)
    crud_cache.delete(cache, type_="menu", id_=menu_id)
    crud_cache.delete_list(cache, "menus")
    return result


def update_menu_by_id(menu_id, new_data, db, cache):
    menu = crud.update_menu_by_id(menu_id, new_data, db)
    if menu:
        answer = make_menu_answer(menu)
        crud_cache.set_item(cache, type_="menu", item=answer)
        crud_cache.delete_list(cache, "menus")
        return answer


def get_submenus(menu_id, db, cache):
    cached_submenus = crud_cache.get_list(cache, "submenus")
    if cached_submenus:
        return cached_submenus
    submenus = crud.get_submenus(menu_id, db)
    submenus_list = [make_submenu_answer(submenu) for submenu in submenus]
    crud_cache.set_list(cache, key="submenus", items=submenus_list)
    return submenus_list


def create_submenu(submenu, menu_id, db, cache):
    submenu = crud.create_submenu(submenu, menu_id, db)
    if submenu:
        answer = make_submenu_answer(submenu)
        crud_cache.set_item(cache, type_="submenu", item=answer)
        crud_cache.delete_list(cache, "submenus")
        crud_cache.delete_list(cache, "menus")
        crud_cache.delete(cache, type_="menu", id_=menu_id)
        return answer


def get_submenu_by_id(submenu_id, db, cache):
    cached_submenu = crud_cache.get_item(
        cache, type_="submenu", id_=submenu_id)
    if cached_submenu:
        return cached_submenu
    submenu = crud.get_submenu_by_id(submenu_id, db)
    if submenu:
        answer = make_submenu_answer(submenu)
        crud_cache.set_item(cache, type_="submenu", item=answer)
        return answer


def delete_submenu_by_id(submenu_id, menu_id, db, cache):
    result = crud.delete_submenu_by_id(submenu_id, db)
    crud_cache.delete(cache, type_="submenu", id_=submenu_id)
    crud_cache.delete_list(cache, "submenus")
    crud_cache.delete_list(cache, "menus")
    crud_cache.delete(cache, type_="menu", id_=menu_id)

    return result


def update_submenu_by_id(submenu_id, new_data, db, cache):
    submenu = crud.update_submenu_by_id(submenu_id, new_data, db)
    if submenu:
        answer = make_submenu_answer(submenu)
        crud_cache.set_item(cache, type_="submenu", item=answer)
        crud_cache.delete_list(cache, "submenus")
        return answer


def get_dishes(submenu_id, db, cache):
    cached_dishes = crud_cache.get_list(cache, "dishes")
    if cached_dishes:
        return cached_dishes
    dishes = crud.get_dishes(submenu_id, db)
    dishes_list = [make_dish_answer(dish) for dish in dishes]
    crud_cache.set_list(cache, "dishes", dishes_list)
    return dishes_list


def create_dish(dish, submenu_id, menu_id, db, cache):
    dish = crud.create_dish(dish, submenu_id, db)
    if dish:
        answer = make_dish_answer(dish)
        crud_cache.set_item(cache, type_="dish", item=answer)
        crud_cache.delete_list(cache, "submenus")
        crud_cache.delete_list(cache, "menus")
        crud_cache.delete_list(cache, "dishes")
        crud_cache.delete(cache, type_="menu", id_=menu_id)
        crud_cache.delete(cache, type_="submenu", id_=submenu_id)
        return answer


def get_dish_by_id(dish_id, db, cache):
    cached_dish = crud_cache.get_item(cache, type_="dish", id_=dish_id)
    if cached_dish:
        return cached_dish
    dish = crud.get_dish_by_id(dish_id, db)

    if dish:
        answer = make_dish_answer(dish)
        crud_cache.set_item(cache, type_="dish", item=answer)
        return answer


def delete_dish_by_id(dish_id, submenu_id, menu_id, db, cache):
    result = crud.delete_dish_by_id(dish_id, db)
    crud_cache.delete_list(cache, "submenus")
    crud_cache.delete_list(cache, "menus")
    crud_cache.delete_list(cache, "dishes")
    crud_cache.delete(cache, type_="dish", id_=dish_id)
    crud_cache.delete(cache, type_="submenu", id_=submenu_id)
    crud_cache.delete(cache, type_="menu", id_=menu_id)

    return result


def update_dish_by_id(dish_id, new_data, db, cache):
    dish = crud.update_dish_by_id(dish_id, new_data, db)
    if dish:
        answer = make_dish_answer(dish)
        crud_cache.set_item(cache, type_="dish", item=answer)
        crud_cache.delete_list(cache, "dishes")
        return answer


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


def make_menu_answer(menu):
    return {
        "id": str(menu.id),
        "title": menu.title,
        "description": menu.description,
        "submenus_count": len(menu.submenus),
        "dishes_count": sum(len(submenu.dishes) for submenu in menu.submenus)
        if menu.submenus
        else 0,
    }

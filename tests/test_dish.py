import json


from app.models import SubMenu, Menu, Dish

class TestDish:
    def test_create_dish(self, client, menu, submenu,dish, db):
        resp = client.post("/api/v1/menus/", data=json.dumps(menu))
        last_menu = db.query(Menu).first()
        menu_id = str(last_menu.id)
        client.post(f"/api/v1/menus/{menu_id}/submenus/", data=json.dumps(submenu))
        last_submenu = db.query(SubMenu).first()
        submenu_id = str(last_submenu.id)
        resp = client.post(f"/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/", data=json.dumps(dish))
        resp_data = resp.json()
        assert resp.status_code == 201
        assert resp_data["title"] == dish["title"]
        assert resp_data["description"] == dish["description"]
        assert resp_data["price"] == dish["price"]
    
    def test_get_dish_by_id(self, client, menu, create_menu, submenu, dish, db):
        create_menu(db, menu)
        last_menu = db.query(Menu).first()
        menu_id = str(last_menu.id)
        client.post(f"/api/v1/menus/{menu_id}/submenus/", data=json.dumps(submenu))
        last_submenu = db.query(SubMenu).first()
        submenu_id = str(last_submenu.id)
        client.post(f"/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/", data=json.dumps(dish))
        last_dish = db.query(Dish).first()
        dish_id = str(last_dish.id)
        resp = client.get(f"/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}/")
        assert resp.status_code == 200
        resp_data = resp.json()
        assert resp_data["id"] == dish_id
        assert resp_data["title"] == dish["title"]
        assert resp_data["description"] == dish["description"]
        assert resp_data["price"] == dish["price"]
    

    def test_update_submenu(self, client, menu, submenu, create_menu, dish, db):
        new_data = {"title": "Updated title", "description": "Updated description", "price": "15.5"}
        create_menu(db, menu)
        last_menu = db.query(Menu).first()
        menu_id = str(last_menu.id)
        client.post(f"/api/v1/menus/{menu_id}/submenus/", data=json.dumps(submenu))
        last_submenu = db.query(SubMenu).first()
        submenu_id = str(last_submenu.id)
        client.post(f"/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/", data=json.dumps(dish))
        last_dish = db.query(Dish).first()
        dish_id = str(last_dish.id)
        resp = client.patch(f"/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}/", data=json.dumps(new_data))
        resp_data = resp.json()
        assert resp_data["id"] == dish_id
        assert resp_data["title"] == new_data["title"]
        assert resp_data["description"] == new_data["description"]
        assert resp_data["price"] == new_data["price"]
    

    def test_delete_menu(self, client, create_menu, menu, submenu, dish, db):
        create_menu(db, menu)
        last_menu = db.query(Menu).first()
        menu_id = str(last_menu.id)
        client.post(f"/api/v1/menus/{menu_id}/submenus/", data=json.dumps(submenu))
        last_submenu = db.query(SubMenu).first()
        submenu_id = str(last_submenu.id)
        client.post(f"/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/", data=json.dumps(dish))
        last_dish = db.query(Dish).first()
        dish_id = str(last_dish.id)
        resp = client.delete(f"/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}/")
        assert resp.status_code == 200
        resp_data = resp.json()
        assert resp_data["success"] == True

import json


from app.models import SubMenu, Menu


class TestSubMenu:
    def test_create_submenu(self, client, menu, submenu, db):
        resp = client.post("/api/v1/menus/", data=json.dumps(menu))
        last_menu = db.query(Menu).first()
        menu_id = str(last_menu.id)
        resp = client.post(
            f"/api/v1/menus/{menu_id}/submenus/", data=json.dumps(submenu)
        )
        resp_data = resp.json()
        assert resp.status_code == 201
        assert resp_data["title"] == submenu["title"]
        assert resp_data["description"] == submenu["description"]
        assert resp_data["dishes_count"] == 0

    def test_get_submenu_by_id(self, client, menu, create_menu, submenu, db):
        create_menu(db, menu)
        last_menu = db.query(Menu).first()
        menu_id = str(last_menu.id)
        client.post(
            f"/api/v1/menus/{menu_id}/submenus/", data=json.dumps(submenu))
        last_submenu = db.query(SubMenu).first()
        submenu_id = str(last_submenu.id)
        resp = client.get(f"/api/v1/menus/{menu_id}/submenus/{submenu_id}/")
        assert resp.status_code == 200
        resp_data = resp.json()
        assert resp_data["id"] == submenu_id
        assert resp_data["title"] == submenu["title"]
        assert resp_data["description"] == submenu["description"]
        assert resp_data["dishes_count"] == 0

    def test_update_submenu(self, client, menu, submenu, create_menu, db):
        new_data = {"title": "Updated title",
                    "description": "Updated description"}
        create_menu(db, menu)
        last_menu = db.query(Menu).first()
        menu_id = str(last_menu.id)
        client.post(
            f"/api/v1/menus/{menu_id}/submenus/", data=json.dumps(submenu))
        last_submenu = db.query(SubMenu).first()
        submenu_id = str(last_submenu.id)
        resp = client.patch(
            f"/api/v1/menus/{menu_id}/submenus/{submenu_id}/", data=json.dumps(new_data)
        )
        resp_data = resp.json()
        assert resp_data["id"] == submenu_id
        assert resp_data["title"] == new_data["title"]
        assert resp_data["description"] == new_data["description"]
        assert resp_data["dishes_count"] == 0

    def test_delete_menu(self, client, create_menu, menu, submenu, db):
        create_menu(db, menu)
        last_menu = db.query(Menu).first()
        menu_id = str(last_menu.id)
        client.post(
            f"/api/v1/menus/{menu_id}/submenus/", data=json.dumps(submenu))
        last_submenu = db.query(SubMenu).first()
        submenu_id = str(last_submenu.id)
        resp = client.delete(f"/api/v1/menus/{menu_id}/submenus/{submenu_id}/")
        assert resp.status_code == 200
        resp_data = resp.json()
        assert resp_data["success"] is True

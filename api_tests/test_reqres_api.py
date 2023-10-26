import allure
import pytest
import constants as c
from api_methods import reqres_api as ra

USER_NAME = "user"
USER_JOB = "test"
CHANGED_USER_NAME = "user changed"
CHANGED_USER_JOB = "test changed"


def create_user_check(url: str):
    create_user_response = ra.create_user(url, USER_NAME, USER_JOB)
    assert create_user_response.status_code == 201
    assert isinstance(create_user_response.json()["name"], str)
    assert create_user_response.json()["name"] == USER_NAME
    assert isinstance(create_user_response.json()["job"], str)
    assert create_user_response.json()["job"] == USER_JOB
    assert isinstance(create_user_response.json()["id"], str)
    user_id = create_user_response.json()["id"]
    assert isinstance(create_user_response.json()["createdAt"], str)
    return user_id


def get_single_user_by_id_check(url: str, id: int):
    get_single_user_by_id_response = ra.get_single_user_by_id(url, id)
    assert get_single_user_by_id_response.status_code == 200
    # Проверки на тип добавлены, т.к. в практике были случаи, когда типы в контракте менялись и на фронте возникали
    # ошибки
    assert isinstance(get_single_user_by_id_response.json()["data"]["id"], int)
    assert get_single_user_by_id_response.json()["data"]["id"] == id
    assert isinstance(get_single_user_by_id_response.json()["data"]["email"], str)
    assert isinstance(get_single_user_by_id_response.json()["data"]["first_name"], str)
    assert isinstance(get_single_user_by_id_response.json()["data"]["last_name"], str)
    assert isinstance(get_single_user_by_id_response.json()["data"]["avatar"], str)
    assert isinstance(get_single_user_by_id_response.json()["support"]["url"], str)
    assert isinstance(get_single_user_by_id_response.json()["support"]["text"], str)


def patch_update_user_check(url: str, id: int):
    patch_update_user_response = ra.patch_update_user(url, CHANGED_USER_NAME, CHANGED_USER_JOB, id)
    assert patch_update_user_response.status_code == 200
    assert isinstance(patch_update_user_response.json()["name"], str)
    assert patch_update_user_response.json()["name"] == CHANGED_USER_NAME
    assert isinstance(patch_update_user_response.json()["job"], str)
    assert patch_update_user_response.json()["job"] == CHANGED_USER_JOB
    assert isinstance(patch_update_user_response.json()["updatedAt"], str)
    # Возвращаем данные в исходное состояние
    patch_update_user_response = ra.patch_update_user(url, USER_NAME, USER_JOB, id)
    assert patch_update_user_response.status_code == 200


def put_update_user_check(url: str, id: int):
    patch_update_user_response = ra.put_update_user(url, CHANGED_USER_NAME, CHANGED_USER_JOB, id)
    assert patch_update_user_response.status_code == 200
    assert isinstance(patch_update_user_response.json()["name"], str)
    assert patch_update_user_response.json()["name"] == CHANGED_USER_NAME
    assert isinstance(patch_update_user_response.json()["job"], str)
    assert patch_update_user_response.json()["job"] == CHANGED_USER_JOB
    assert isinstance(patch_update_user_response.json()["updatedAt"], str)
    # Возвращаем данные в исходное состояние
    patch_update_user_response = ra.put_update_user(url, USER_NAME, USER_JOB, id)
    assert patch_update_user_response.status_code == 200


def delete_user_by_id_check(url: str, id: int):
    delete_user_by_id_response = ra.delete_user_by_id(url, id)
    assert delete_user_by_id_response.status_code == 204


@allure.suite("User flow")
@pytest.mark.api
def test_user_flow():
    created_user_id = create_user_check(c.URL_API)
    get_single_user_by_id_check(c.URL_API, 12)
    patch_update_user_check(c.URL_API, created_user_id)
    put_update_user_check(c.URL_API, created_user_id)
    delete_user_by_id_check(c.URL_API, 12)

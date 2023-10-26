import allure
import requests


def create_user(url: str, name: str, job: str):
    body = {
        "name": name,
        "job": job
    }
    with allure.step("Create user"):
        create_user_response = requests.post(f"{url}/api/users", json=body)
    return create_user_response


def get_single_user_by_id(url: str, id: int):
    with allure.step(f"Get single user by id: {id}"):
        get_single_user_by_id_response = requests.get(f"{url}/api/users/{id}")
    return get_single_user_by_id_response


def patch_update_user(url: str, name: str, job: str, id: int):
    body = {
        "name": name,
        "job": job
    }
    with allure.step(f"Update user with id: {id} by PATCH"):
        patch_update_user_response = requests.patch(f"{url}/api/users/{id}", json=body)
    return patch_update_user_response


def put_update_user(url: str, name: str, job: str, id: int):
    body = {
        "name": name,
        "job": job
    }
    with allure.step(f"Update user with id: {id} by PUT"):
        put_update_user_response = requests.put(f"{url}/api/users/{id}", json=body)
    return put_update_user_response


def delete_user_by_id(url: str, id: str):
    with allure.step(f"Delete user by id: {id}"):
        delete_user_by_id_response = requests.delete(f"{url}/api/users/{id}")
    return delete_user_by_id_response

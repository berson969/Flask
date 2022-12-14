import json
from typing import Literal
from urllib.parse import urljoin

import requests
from advs.errors import ApiError
from advs.tests.config import API_URL

session = requests.Session()


def base_request(http_method: Literal["get", "post", "delete", "patch"], path: "str", *args, **kwargs) -> dict:
    method = getattr(session, http_method)
    response = method(urljoin(API_URL, path), *args, **kwargs)
    if response.status_code >= 400:
        try:
            message = response.json()
        except json.JSONDecodeError:
            message = response.text
        raise ApiError(response.status_code, message)
    return response.json()


def register(email: str, password: str) -> int:
    return base_request("post", "users", json={"email": email, "password": password})["id"]


def login(email: str, password: str) -> str:
    return base_request("post", "login", json={"email": email, "password": password})["password"]


def get_user(user_id: int) -> dict:
    return base_request("get", f"users/{user_id}")


# def delete_user(user_id: int) -> bool:
#     return base_request("delete", f"users/{user_id}")["deleted"]


# def logout(email: str, password: str) -> str:
#     return base_request("post", "login", json={"email": email, "password": password})["password"]

# def post_adv(id: int, title: str, description: str = None, token: str = None) -> dict:
#     params = {key: value for key, value in (("title", title), ("description", description)) if value is not None}
#     return base_request("post", f"adv}", json=params)
#
# def patch_adv(id: int, email: str, password: str = None, current_user.id) -> dict:
#     params = {key: value for key, value in (("email", email), ("password", password)) if value is not None}
#     return base_request("patch", f"users/id}", json=params, headers={"token": token})
#
#
import pytest

from backend_api_automation.clients.users_client import UsersClient
from backend_api_automation.models.user_models import User
from backend_api_automation.utils.assertions import assert_status_code


@pytest.mark.smoke
def test_list_users_response(users_client: UsersClient) -> None:
    response = users_client.list_users()

    assert_status_code(response, 200)
    users = [User.model_validate(item) for item in response.json()]
    assert len(users) == 10, f"Expected JSONPlaceholder to return 10 users, got {len(users)}"
    assert all(user.email for user in users), "Expected every user to include an email address"


@pytest.mark.regression
def test_single_user_response(users_client: UsersClient) -> None:
    response = users_client.get_user(1)

    assert_status_code(response, 200)
    user = User.model_validate(response.json())

    assert user.id == 1, "Expected user id 1"
    assert user.name == "Leanne Graham", "Expected stable JSONPlaceholder fixture user name"
    assert user.company.name, "Expected user company details to be present"


@pytest.mark.negative
def test_user_not_found_behavior(users_client: UsersClient) -> None:
    response = users_client.get_user(999_999)

    assert_status_code(response, 404)
    assert response.json() == {}, "Expected not-found JSONPlaceholder user response to be an empty object"


@pytest.mark.regression
def test_user_posts_nested_resource(users_client: UsersClient) -> None:
    response = users_client.get_user_posts(1)

    assert_status_code(response, 200)
    posts = response.json()
    assert posts, "Expected user 1 to have posts"
    assert all(post["userId"] == 1 for post in posts), "Expected every nested post to belong to user 1"

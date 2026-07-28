import pytest
import allure
from services.user_service import UserService
from models.user_model import UserData, CreateUserResponse


@allure.epic("User API Operations")
@allure.feature("Parametrized Data Testing")
class TestParametrizedUsers:

    @allure.story("Retrieve Multiple Users")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("user_id, expected_name", [
        (1, "Leanne Graham"),
        (2, "Ervin Howell"),
        (3, "Clementine Bauch")
    ])
    def test_go_multiple_users_id(self, user_service: UserService, user_id: int, expected_name: str):
        """Runs test cases sequentially across multiple user IDs."""
        allure.dynamic.title(f"Fetch User ID #{user_id} - Expected: {expected_name}")
        
        with allure.step(f"Fetch details for user ID {user_id}"):
            response = user_service.get_user_by_id(user_id)
            assert response.status == 200

        with allure.step("Validate response contract with Pydantic"):
            user = UserData(**response.json())
            assert user.id == user_id
            assert user.name == expected_name

    @allure.story("Create Multiple Users")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("name, job", [
        ("Saransh", "Automation Engineer"),
        ("Alex", "DevOps Engineer"),
        ("Maya", "Data Analyst"),
        ("Sam", "QA Lead")
    ])
    def test_create_multiple_users(self, user_service: UserService, name: str, job: str):
        """Tests user creation across varied roles and names."""
        allure.dynamic.title(f"Create User: {name} ({job})")

        with allure.step(f"Send POST request to create {name} as {job}"):
            response = user_service.create_user(name=name, job=job)
            assert response.status == 201

        with allure.step("Validate creation response ID"):
            created_user = CreateUserResponse(**response.json())
            assert created_user.id is not None
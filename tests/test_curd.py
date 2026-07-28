import allure 
from services.user_service import UserService

@allure.epic("User API Operation")
@allure.feature("CRUD Lifecycle")
class TestUserCRUD:

    @allure.story("Full User Update")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_put_full_user_update(self,user_service:UserService):
        """Verifies full replacement of user data using PUT"""
        update_payload = {
            "name":"Saransh Updated",
            "username":"saransh_dev",
            "email":"saransh@example.com"
        }

        with allure.step("1. Send PUT request to update the details"):
            response = user_service.update_user(user_id=1,payload=update_payload)

        with allure.step("2. Verify HTTP status code is 200 OK"):
            assert response.status == 200

        with allure.step("3. Validate updated values in response payload"):
            data =  response.json()
            assert data['name'] == "Saransh Updated"
            assert data['username'] == "saransh_dev"


    @allure.story("Patrial User Update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_patch_partial_user_update(self,user_service:UserService):
        """Verifies updating only specific feilds using PATCH"""
        patch_payload = {
            "email":"new_email@example.com"
        }
        with allure.step("1. Send PATCH request with updated email"):
            response = user_service.patch_user(user_id=1, payload=patch_payload)
        with allure.step("2. Assert status in 200 and email is updated"):
            assert response.status == 200
            assert response.json()['email'] == "new_email@example.com"

    @allure.story("Delete User")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_user_success(self, user_service: UserService):
        """Verifies user deletion using DELETE."""
        with allure.step("1. Send DELETE request for user ID 1"):
            response = user_service.delete_user(user_id=1)

        with allure.step("2. Confirm status is 200 or 204"):
            assert response.status in [200, 204]
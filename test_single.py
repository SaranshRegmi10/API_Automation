import pytest 
from playwright.sync_api import sync_playwright
from pydantic import BaseModel

class UserData(BaseModel):
    id: int
    first_name: str
    email: str

class UserResponse(BaseModel):
    data: UserData

def test_get_user():
    #Start Playwright's HTTP engine
    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url = "https://jsonholder.typicode.com",
            extra_http_headers = {"Content-Type":"application/json"}
        )
        response = request_context.get("/users/1")

        assert response.status == 200

        json_data = response.json()
        print("\nAPI OUTPUT",json_data)

        assert "name" in json_data
        assert json_data['id'] == 1

if __name__ == "__main__":
    test_get_user()
    print("\n Test Passed!!!")


def test_get_user():
    # Step A: Start Playwright's HTTP engine
    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url="https://jsonplaceholder.typicode.com",
            extra_http_headers={"Content-Type": "application/json"}
        )

        # Step B: Make the API call to /users/1
        response = request_context.get("/users/1")

        # Step C: Check status code
        assert response.status == 200

        # Step D: Read the JSON response
        json_data = response.json()
        print("\nAPI Output:", json_data)

        # Step E: Check that 'name' is in the response
        assert "name" in json_data
        assert json_data["id"] == 1


# 3. RUN IT IMMEDIATELY
if __name__ == "__main__":
    test_get_user()
    print("\n✅ TEST PASSED SUCCESSFULLY!")
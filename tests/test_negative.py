# from services.user_service import UserService

# def test_get_non_existance_user(user_service:UserService):
#     """Verifies that requesting a userId that doesn't exists returns 404"""
#     #jsonplaceholder only has userid 1-10
#     response = user_service.get_user_by_id(user_id=999999)

#     #Assert HTTP status is 404 not found
#     assert response.status == 404, f"Expected 404,got {response.status}"

#     #Assert response body is an empty JSON object{}
#     assert response.json() == {}

# def test_get_user_invalid_id_format(user_service:UserService):
#     """Verifies behaviour when sending a string/alphanumeric ID instead of an integer"""
#     response = user_service.get_user_by_id(user_id="invalid_abc")

#     assert response.status == 404

# def test_delete_non_existance_user(user_service:UserService):
#     """Verifies deleting a non-existance user,"""
#     response = user_service.delete_user(user_id=9999)

#     assert response.status in [200,204,404]
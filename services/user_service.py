from typing import Dict,Any
from playwright.sync_api import APIResponse
from client.api_client import APIClient

class UserService:
    def __init__(self,api_client:APIClient):
        self.client = api_client
        self.endpoint = "/users"

    def get_users(self,page:int=1)->APIResponse:
        return self.client.get(self.endpoint,params={"page":page})

    def get_user_by_id(self,user_id:int)->APIResponse:
        return self.client.get(f"{self.endpoint}/{user_id}")

    def create_user(self,name:str,job:str)->APIResponse:
        payload = {
            "name":name,
            "job": job
        }
        return self.client.post(self.endpoint,data=payload)

    def update_user(self, user_id: int, payload: Dict[str, Any]) -> APIResponse:
        return self.client.put(f"{self.endpoint}/{user_id}", data=payload)

    def patch_user(self,user_id:int,payload:Dict[str,Any])->APIResponse:
        """Partial update via Patch"""
        return self.client.patch(f"{self.endpoint}/{user_id}",data=payload)

    def delete_user(self,user_id:int) ->APIResponse:
        return self.client.delete(f"{self.endpoint}/{user_id}")

from typing import Dict,Any,Optional
from playwright.sync_api import APIRequestContext,APIResponse

class APIClient:
    """Wrapper aroung Playwright APIRequestContext to standardrize requests and logging.Central engine for sending HTTP requests safely."""
    def __init__(self,request_context:APIRequestContext,base_url:str):
        self.request = request_context
        self.base_url = base_url.rstrip("/")

    def get(self,endpoint:str,params:Optional[Dict[str,Any]]=None) ->APIResponse:
        url = f"{self.base_url}{endpoint}"
        kwargs = {}
        if params:
            kwargs["params"] = params
        return self.request.get(url,**kwargs)

    def post(self,endpoint:str,data:Optional[Dict[str,Any]]=None)->APIResponse:
        url = f"{self.base_url}{endpoint}"
        kwargs = {}
        if data:
            kwargs["data"] = data
        return self.request.post(url,**kwargs)

    def put(self,endpoint:str,data:Optional[Dict[str,Any]]=None)->APIResponse:
        url = f"{self.base_url}{endpoint}"
        kwargs = {}
        if data:
            kwargs["data"] = data
        return self.request.put(url,**kwargs)

    def patch(self,endpoint:str,data:Optional[Dict[str,Any]]=None)->APIResponse:
        url = f"{self.base_url}{endpoint}"
        kwargs = {}
        if data:
            kwargs["data"] = data
        return self.request.patch(url,**kwargs)

    def delete(self,endpoint:str)->APIResponse:
        url = f"{self.base_url}{endpoint}"
        return self.request.delete(url)

    
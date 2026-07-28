# tests/conftest.py

import pytest
from playwright.sync_api import sync_playwright, APIRequestContext
from client.api_client import APIClient
from services.user_service import UserService


@pytest.fixture(scope="session")
def api_request_context():
    """Initializes Playwright's API context once per test session."""
    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url="https://jsonplaceholder.typicode.com",
            extra_http_headers={
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
        )
        yield request_context
        request_context.dispose()


@pytest.fixture
def api_client(api_request_context: APIRequestContext) -> APIClient:
    return APIClient(api_request_context, base_url="https://jsonplaceholder.typicode.com")


@pytest.fixture
def user_service(api_client: APIClient) -> UserService:
    return UserService(api_client)
# models/user_model.py

from typing import List, Optional
from pydantic import BaseModel, EmailStr, RootModel


class Geo(BaseModel):
    lat: str
    lng: str


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Optional[Geo] = None


class Company(BaseModel):
    name: str
    catchPhrase: Optional[str] = None
    bs: Optional[str] = None


class UserData(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    address: Optional[Address] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    company: Optional[Company] = None


# --- Pydantic V2 RootModel for Top-Level JSON Arrays ---
class UserListResponse(RootModel[List[UserData]]):
    pass


class CreateUserResponse(BaseModel):
    id: int
    name: Optional[str] = None
    job: Optional[str] = None
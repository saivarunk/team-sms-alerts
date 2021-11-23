from typing import List

from pydantic import BaseModel


class DeveloperBase(BaseModel):
    name: str
    phone_number: str


class DeveloperCreate(DeveloperBase):
    pass


class Developer(DeveloperBase):
    id: int
    team_id: int

    class Config:
        orm_mode = True


class TeamBase(BaseModel):
    name: str


class TeamCreate(TeamBase):
    pass


class Team(TeamBase):
    id: int
    developers: List[Developer] = []

    class Config:
        orm_mode = True

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session

from pagerduty.crud import get_teams, create_team
from pagerduty.dependency import get_db

router = APIRouter()


class Developer(BaseModel):
    name: str
    phone_number: str


class Team(BaseModel):
    name: str


class TeamCreationPayload(BaseModel):
    team: Team
    developers: List[Developer]


@router.post("/")
def create_team_endpoint(team: TeamCreationPayload, db: Session = Depends(get_db)):
    team = create_team(db, team.team, team.developers)
    if team:
        return team
    else:
        raise HTTPException(status_code=400, detail="Unable to create a team")


@router.get("/")
def get_teams_endpoint(db: Session = Depends(get_db)):
    teams = get_teams(db)
    return teams

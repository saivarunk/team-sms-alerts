from sqlalchemy.orm import Session

from typing import List
from pagerduty import models, schemas


def get_developers(db: Session, team_id: int):
    return db.query(models.Developer).filter(models.Developer.team_id == team_id).all()


def get_teams(db: Session):
    return db.query(models.Team).all()


def create_team(
    db: Session, team: schemas.TeamCreate, developers: List[schemas.DeveloperCreate]
):
    # Create Team
    db_team = models.Team(name=team.name)
    db.add(db_team)
    db.commit()

    # Add Developers to team
    for dev in developers:
        db.add(
            models.Developer(
                name=dev.name, phone_number=dev.phone_number, team_id=db_team.id
            )
        )

    db.commit()
    db.refresh(db_team)
    return db_team

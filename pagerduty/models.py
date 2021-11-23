from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from pagerduty.database import Base


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=False, nullable=False)

    developers = relationship("Developer")


class Developer(Base):
    __tablename__ = "developers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=False, nullable=False)
    phone_number = Column(String, nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id"))

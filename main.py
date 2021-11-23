import uvicorn
from fastapi import FastAPI

from pagerduty.controllers import teams, alerts
from pagerduty import models
from pagerduty.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(alerts.router, prefix="/alerts", tags=["alerts"])
app.include_router(teams.router, prefix="/teams", tags=["teams"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

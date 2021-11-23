import requests

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from pagerduty.crud import get_developers
from pagerduty.dependency import get_db
from pagerduty.settings import settings

router = APIRouter()


class CreateAlertPayload(BaseModel):
    team_id: int
    alert_message: str


def send_alert(phone_number: str, message: str):
    try:
        payload = {"phone_number": phone_number, "message": message}
        response = requests.post(settings.sms_endpint, json=payload)
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()
        else:
            return {}
    except Exception as e:
        print("Exception while making SMS call", str(e))
        return False


@router.post("/")
async def send_alert_endpoint(
    payload: CreateAlertPayload, db: Session = Depends(get_db)
):
    developers = get_developers(db, payload.team_id)
    if developers:
        sms_response = send_alert(developers[0].phone_number, payload.alert_message)
        if sms_response:
            return {"Message": "SMS Alert delivered"}
        else:
            raise HTTPException(status_code=400, detail="Unable to send alert to team")
    else:
        raise HTTPException(status_code=404, detail="Unable to find team with give ID")

from http import client
from typing import Optional

from fastapi import HTTPException
from src.models.Notification import Notification
from src.workers.notification_worker import NotificationWorker

def notification_controller(app):

    @app.post("/notification/create", tags=["notifications"])
    async def create_notification_for_user(request:Notification):
        try:
            response = NotificationWorker().create_notification_for_user(request)
        except HTTPException:
            raise HTTPException(status_code=404, detail="Error on creation")
        return response

    @app.get("/notification/{client_id}", tags=["notifications"])
    async def get_notification_for_user(client_id:str):
        try:
            response = NotificationWorker().get_notification_for_user(client_id)
        except HTTPException:
            raise HTTPException(status_code=404, detail="Error getting info")
        return response

    @app.put("/notification/update", tags=["notifications"])
    async def update_notification_for_user(request:Notification):
        try:
            response = NotificationWorker().update_notification_for_user(request)
        except HTTPException:
            raise HTTPException(status_code=404, detail="Error on update")
        return response

    @app.delete("/notification/delete/{client_id}", tags=["notifications"])
    async def delete_notification_for_user(client_id:str):
        try:
            response = NotificationWorker().delete_notification_for_user(client_id)
        except HTTPException:
            raise HTTPException(status_code=404, detail="Error on deletion")
        return response
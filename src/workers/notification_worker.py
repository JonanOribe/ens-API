from dataclasses import dataclass

from src.infrastructure.notification_adapter import NotificationAdapter
from src.models.Notification import Notification


@dataclass
class NotificationWorker:
    def create_notification_for_user(self,request:Notification):
        return NotificationAdapter.create_notification_for_user(self,request)

    def get_notification_for_user(self,client_id:str):
        return NotificationAdapter.get_notification_for_user(self,client_id)

    def update_notification_for_user(self,request:Notification):
        return NotificationAdapter.update_notification_for_user(self,request)

    def delete_notification_for_user(self,client_id:str):
        return NotificationAdapter.delete_notification_for_user(self,client_id)
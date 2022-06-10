import asyncio
import pytest

from src.workers.notification_worker import NotificationWorker


@pytest.mark.asyncio
async def test_notification_for_user():
    client_id:str = "NzIMN8jMOZyVuWktmLMwa1jDvdMqXbc3"
    new_user = {
                "client_id": client_id,
                "title":"Test title",
                "text":"Test text",
                "timestamp":"12/05/2022"
    }

    updated_user = {
                "client_id": client_id,
                "title":"Test title 111",
                "text":"Test text",
                "timestamp":"12/05/2022"
    }

    NotificationWorker().create_notification_for_user(new_user)
    detect_new_user = NotificationWorker().get_notification_for_user(client_id)
    is_correct = detect_new_user[0]['title'] == 'Test title'
    NotificationWorker().update_notification_for_user(updated_user)
    detect_updated_user = NotificationWorker().get_notification_for_user(client_id)
    is_correct_updated = detect_updated_user[0]['title'] == 'Test title 111'
    is_destroyed = NotificationWorker().delete_notification_for_user(client_id)

    assert(is_correct and is_correct_updated and is_destroyed)

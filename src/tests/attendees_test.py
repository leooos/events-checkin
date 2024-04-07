import pytest
from src.models.settings.connection import db_connection_handler

from src.models.repository.attendees_repository import AttendeesRepository

db_connection_handler.connect_to_db()

# @pytest.mark.skip("novo registro em banco de dados")
def test_insert_attendee():
    event_id = "meu-uuid-e-nois2"
    
    attendee_info = {
        "uuid": "attendee-uuid", 
        "name": "attendee name",
        "email": "attendee@test.com",
        "event_id": event_id,
    }

    attendee_repository = AttendeesRepository()
    response = attendee_repository.insert_attendee(attendee_info)
    print(response)
    
def test_get_attendee_badge_by_id():
    attendee_id = "attendee-uuid"
    attendee_repository = AttendeesRepository()
    response = attendee_repository.get_attendee_badge_by_id(attendee_id)
    print(response)
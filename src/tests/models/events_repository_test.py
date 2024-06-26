import pytest
from src.models.settings.connection import db_connection_handler
from src.models.repository.events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip("novo registro em banco de dados")
def test_insert_event():
    event = {
        "uuid": "meu-uuid-e-nois",
        "title": "meu title",
        "slug": "meu-slug-aqui!",
        "maximum_attendees": 20
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)
    
def test_get_event_by_id():
    event_id = "meu-uuid-e-nois!aaaaaaa"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)
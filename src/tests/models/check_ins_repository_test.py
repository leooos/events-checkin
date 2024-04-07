import pytest
from src.models.settings.connection import db_connection_handler

from src.models.repository.check_ins_repository import CheckInsRepository

db_connection_handler.connect_to_db()

# @pytest.mark.skip("novo registro em banco de dados")
def test_insert_check_in():
    attendee_id = "attendee-uuid"
    check_in = CheckInsRepository()
    response = check_in.insert_check_in(attendee_id)
    print(response)

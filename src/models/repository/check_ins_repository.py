from src.models.settings.connection import db_connection_handler
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from src.models.entities.check_ins import CheckIns
from src.models.entities.attendees import Attendees


class CheckInsRepository:
    def insert_check_in(self, attendee_id: str) -> str:
        with db_connection_handler as database:
            try:
                check_in = (
                    CheckIns(attendeeId = attendee_id)
                )
                database.session.add(check_in)
                database.session.commit()
                
                return attendee_id
                
            except IntegrityError:
                raise Exception("Participante já cadastrado!")
            except Exception as exception:
                database.session.rollback()
                raise exception

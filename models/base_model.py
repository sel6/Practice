#!/usr/bin/python3
import uuid
from datetime import date

class BaseModel:
    """ common attribute, methods
    for other classes"""
    def __init__(self, id, created_at, updated_at):
        """unique IDs"""
        self.id=str(uuid.uuid(4))
        self.created_at=
        self.updated_at=

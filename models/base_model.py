#!/usr/bin/python3
import uuid
from datetime import date

class BaseModel:
    """ common attribute, methods
    for other classes"""
    def __init__(self, id, created_at, updated_at):
        """unique IDs"""
        self.id = str(uuid.uuid4())
        self.created_at = date.today()
        self.updated_at = self.created_at
    
    def __str__(self):
        return"[{}]({}){}.format(self.__class__.__name__, self.id, self.__dict__)

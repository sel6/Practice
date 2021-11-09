#!/usr/bin/python3
import uuid

class BaseModel:
    """ common attribute, methods
    for other classes"""
    def __init__(self, id):
        """unique IDs"""
        self.id=uuid.uuid(4)
 

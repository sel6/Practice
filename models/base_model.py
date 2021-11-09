#!/usr/bin/python3
import uuid
from datetime import date

class BaseModel:
    """ common attribute, methods
    for other classes"""
    def __init__(self, id, created_at, updated_at):
        """unique IDs"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at
    
    def __str__(self):
        return"[{}]({}){}.format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
         """updates the public instance attribute updated_at with the current datetime"""
         self.updated_at = datetime.today()
         
        
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        for key, value in self.__dict__.items():
            return(repr(self.__dict__))
            

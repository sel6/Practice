#!/usr/bin/python3
import unittest
import model
from datetime import date

class TestBaseModel:
  
  
  def test___init__(self):
    assertIsInstance(self.id, uuid.uuid4())
    assertIsInstance(self.id, str)
    assertIsEqual(created_at, datetime.today())
    assertIsEqual(updated_at, created_at)
    
  def test___str__(self):
    
    
    
  def test_save(self):
    
   
  def test_to_dict(self):

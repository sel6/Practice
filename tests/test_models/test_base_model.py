#!/usr/bin/python3
import unittest
import model
from datetime import date

class TestBaseModel:
  
  
  def test___init__(self):
    self.assertIsInstance(self.id, uuid.uuid4())
    self.assertIsInstance(self.id, str)
    self.assertIsEqual(created_at, datetime.today())
    self.assertIsEqual(updated_at, created_at)
    
  def test___str__(self):
    
    
    
  def test_save(self):
    
   
  def test_to_dict(self):

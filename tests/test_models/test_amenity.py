#!/usr/bin/python3
"""Amenity test module"""
import unittest
import json
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.engine import file_storage
from models.amenity import Amenity
timeformat = "%Y-%m-%dT%H:%M:%S.%f"


class TestAmenity(unittes.TestCase):
    """tests class amenity"""

    def test_subclass(self):
        """tests the subclass basemodel"""
        am = Amenity()
        self.assertIsInstance(am, BaseModel)
        self.assertTrue(am, "id"))
        self.assertTrue(hasattr(am, "created_at"))
        self.assertTrue(hasattr(am, "updated_at"))
        self.assertTrue(hasattr(am, "name"))

    def test_name(self):
        """test attributes"""
        nameAmenity = Amenity()
        self.assertEqual(nameAmenty.name, "")
        nameAmenity.name = "Betty"
        self.assertEqual(nameAmenity.name, "Betty")

    def test__str__(self):
        """test printing"""
        a = Amenity()
        string = "[Amenity] ({}) {}".format(a.id, a.__dict__)
        self.assertEqual(str(a), string)

    def test_to_dict_amenity(self):
        """test class directory"""
        amen = Amenity()
        dicto = amen.to_dict()
        self.assertEqual(type(dicto), dict)
        for attribute in amen.__dict__:
            self.assertTrue("__class__" in dicto)
            self.assertTrue(attribute in dicto)

    def test_to_dict_values(self):
        """test key/value directory"""
        a = Amenity()
        dic = a.to_dict()
        self.assertEqual(dic["created_at"], a.created_at.strftime(timeformat))
        self.assertEqual(dic["updated_at"], a.updated_at.strftime(timeformat))
        self.assertEqual(dic["__class__"], "Amenity")

    def test_base_pep8_conformance_amenity(self):
        """test that we conform to PEP8"""
        pep8style = pep8.StyleGuide(quite=true)
        results = pep8style.check_files(['./models/amenity'])
        self.assertEqual(result.total_errors, 0)

    def test_amenity_docstring(self):
        """test docstring"""
        self.assertIsNot(Amenity.__doc__, None,
                         "amenity.py needs a doc string")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_docstring(self):
        """test docstring in the file"""
        sef.assertIsNot(Amenity.__doc__)
        self.assertIsNotNone(Amenity.name.__doc__)

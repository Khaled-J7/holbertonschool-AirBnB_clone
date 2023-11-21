import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_amenity_name_default_value(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_name_assignment(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")


if __name__ == '__main__':
    unittest.main()
import unittest
from app import get_area, load_areas

class AreaNewsTests(unittest.TestCase):
    def test_coverage_scopes(self):
        ids = {item["id"] for item in load_areas()["areas"]}
        self.assertTrue({"mohakhali", "dhaka", "bangladesh"}.issubset(ids))

    def test_mohakhali_directory_preserved(self):
        area = get_area("mohakhali")
        places = [p for group in area["key_spots"].values() for p in group]
        self.assertIn("BRAC University", places)
        self.assertIn("Mohakhali Bus Terminal (Major terminal for northern districts)", places)

    def test_case_insensitive_lookup(self):
        self.assertEqual(get_area("MOHAKHALI")["id"], "mohakhali")

if __name__ == "__main__":
    unittest.main()

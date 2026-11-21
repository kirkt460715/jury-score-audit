"""核对交接文件中的来源依据。"""
import unittest
from inspect_delivery import read_table


class DeliveryTest(unittest.TestCase):
    def test_linked_records(self):
        works = {r["work"] for r in read_table("entries.json")}
        ratings = read_table("ratings.json")
        self.assertTrue(all(r["work"] in works for r in ratings))
        self.assertEqual(sum(r["judge"] == "JB" and r["work"].startswith("P") for r in ratings), 4)
        self.assertTrue(any(r["round"] > 1 and r["status"] == "有效" for r in ratings))
        self.assertTrue({r["work"] for r in read_table("decisions.json")} <= works)

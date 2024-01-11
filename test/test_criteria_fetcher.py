import unittest
from src.application import Application
from src.criteria_fetcher import fetch_criterion, fetch_criteria
from src.criteria.criteria_employment import evaluate as employment_criteria
from src.criteria.criteria_criminal import evaluate as criminal_criteria

class TestCriteriaFetcher(unittest.TestCase):

    def test_fetch_criterion_import_error(self):
        with self.assertRaises(ImportError):
            fetch_criterion("criteria_non_existent")

    def test_fetch_criterion_employment(self):
        criterion = fetch_criterion('employment')

        app = Application(has_previous_employment = True)

        self.assertEqual(criterion(app), employment_criteria(app))

    def test_fetch_criterion_criminal(self):
        criterion = fetch_criterion('criminal')

        app = Application(has_criminal_record = False)

        self.assertEqual(criterion(app), criminal_criteria(app))

    def test_fetch_criteria_includes_employment_and_criminal_criteria(self):
        criteria = fetch_criteria()

        evaluation_functions = [criterion_info["evaluate"] for criterion_info in criteria.values()]

        employment_found = employment_criteria in evaluation_functions

        criminal_found = criminal_criteria in evaluation_functions

        self.assertTrue(employment_found and criminal_found)

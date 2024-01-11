import unittest
from src.process_application import ApplicationResult
from src.application import Application
from src.criteria.criteria_criminal import evaluate as criminal_criteria

class TestCriminalCriteria(unittest.TestCase):
    def test_process_application_criminal_pass(self):
        app = Application(has_criminal_record = False)

        result = criminal_criteria(app)

        self.assertEqual(result, (ApplicationResult.PASS, "Applicant has had no criminal record."))

    def test_process_application_criminal_fail(self):
        app = Application(has_criminal_record = True)

        result = criminal_criteria(app)

        self.assertEqual(result, (ApplicationResult.FAIL, "Applicant has criminal records."))

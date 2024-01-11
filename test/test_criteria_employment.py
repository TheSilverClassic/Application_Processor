import unittest
from src.criteria.criteria_employment import evaluate as employment_criteria
from src.application import Application
from src.process_application import ApplicationResult

class TestEmploymentCriteria(unittest.TestCase):
    def test_process_application_employment_pass(self):
        app = Application(has_previous_employment = True)

        result = employment_criteria(app)

        self.assertEqual(result, (ApplicationResult.PASS, "Applicant has had previous employment."))

    def test_process_application_employment_fail(self):
        app = Application(has_previous_employment = False)

        result = employment_criteria(app)

        self.assertEqual(result, (ApplicationResult.FAIL, "Applicant has no previous employment."))

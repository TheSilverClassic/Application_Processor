import unittest
from src.application import Application
from src.process_application import ApplicationResult
from src.criteria.criteria_security_clearance import evaluate as security_criteria

class TestClearanceCriteria(unittest.TestCase):
    def test_process_application_clearance_pass(self):
        app = Application(meets_security_clearance = True)

        result = security_criteria(app)

        self.assertEqual(result, (ApplicationResult.PASS, "Applicant meets security clearance requirements."))

    def test_process_application_clearance_fail(self):
        app = Application(meets_security_clearance = False)

        result = security_criteria(app)

        self.assertEqual(result, (ApplicationResult.FAIL, "Applicant does not meet security clearance requirements."))

import unittest
from src.process_application import ApplicationResult
from src.application import Application
from src.criteria.criteria_credit import evaluate as credit_criteria

class TestCreditCriteria(unittest.TestCase):
    def test_process_application_credit_pass(self):
        app = Application(meets_credit = True)

        result = credit_criteria(app)

        self.assertEqual(result, (ApplicationResult.PASS, "Applicant has sufficient credit."))

    def test_process_application_credit_fail(self):
        app = Application(meets_credit = False)

        result = credit_criteria(app)

        self.assertEqual(result, (ApplicationResult.FAIL, "Applicant has non sufficient credit."))

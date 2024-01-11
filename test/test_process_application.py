import unittest
from src.application import Application
from src.process_application import process_application, ApplicationResult
from src.criteria.criteria_employment import evaluate as employment_criteria
from src.criteria.criteria_criminal import evaluate as criminal_criteria
from src.criteria.criteria_credit import evaluate as credit_criteria
from src.criteria.criteria_security_clearance import evaluate as security_criteria

class TestProcessApplication(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_process_application_no_criteria(self):
        app = Application(has_previous_employment = True)

        result = process_application(app)

        self.assertEqual(result, (ApplicationResult.PASS, "Nothing to check."))

    def test_process_application_with_criteria_employment_pass(self):
        app = Application(has_previous_employment = True)

        result = process_application(app, employment_criteria)

        self.assertEqual(result, (ApplicationResult.PASS, "Applicant has had previous employment."))

    def test_process_application_with_criteria_employment_fail(self):
        app = Application(has_previous_employment = False)

        result = process_application(app, employment_criteria)

        self.assertEqual(result, (ApplicationResult.FAIL, "Applicant has no previous employment."))

    def test_process_application_pass_has_employment_no_criminal_record(self):
        app = Application(has_previous_employment = True, has_criminal_record = False)

        result = process_application(app, employment_criteria, criminal_criteria)

        self.assertEqual(result, (ApplicationResult.PASS, "Applicant has had previous employment. Applicant has had no criminal record."))

    def test_process_application_fail_no_employment_no_criminal_record(self):
        app = Application(has_previous_employment = False, has_criminal_record = False)

        result = process_application(app, employment_criteria, criminal_criteria)

        self.assertEqual(result, (ApplicationResult.FAIL, "Applicant has no previous employment. Applicant has had no criminal record."))

    def test_process_application_fail_has_employment_has_criminal_record(self):
        app = Application(has_previous_employment = True, has_criminal_record = True)

        result = process_application(app, employment_criteria, criminal_criteria)

        self.assertEqual(result, (ApplicationResult.FAIL, "Applicant has had previous employment. Applicant has criminal records."))

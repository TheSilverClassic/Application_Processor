from src.process_application import ApplicationResult

def evaluate(application):
    if application.meets_security_clearance:
        return (ApplicationResult.PASS, "Applicant meets security clearance requirements.")

    return (ApplicationResult.FAIL, "Applicant does not meet security clearance requirements.")

required_fields = {
    "meets_security_clearance": {
        "prompt": "Meets security clearance? (True/False): ",
        "type": "boolean"
    }
}

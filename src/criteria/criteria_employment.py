from src.process_application import ApplicationResult

def evaluate(application):
    if application.has_previous_employment:
        return (ApplicationResult.PASS, "Applicant has had previous employment.")

    return (ApplicationResult.FAIL, "Applicant has no previous employment.")

required_fields = {
    "has_previous_employment": {
        "prompt": "Has previous employment? (True/False): ",
        "type": "boolean"
    }
}

from src.process_application import ApplicationResult

def evaluate(application):
    if application.meets_credit:
        return (ApplicationResult.PASS, "Applicant has sufficient credit.")

    return (ApplicationResult.FAIL, "Applicant has non sufficient credit.")

required_fields = {
    "meets_credit": {
        "prompt": "Has sufficient credit? (True/False): ",
        "type": "boolean"
    }
}

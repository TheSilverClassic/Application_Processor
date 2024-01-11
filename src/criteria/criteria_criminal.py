from src.process_application import ApplicationResult

def evaluate(application):
    if application.has_criminal_record:
        return (ApplicationResult.FAIL, "Applicant has criminal records.")

    return (ApplicationResult.PASS, "Applicant has had no criminal record.")

required_fields = {
    "has_criminal_record": {
        "prompt": "Has criminal record? (True/False): ",
        "type": "boolean"
    }
}

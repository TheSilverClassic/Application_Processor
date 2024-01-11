from src.application_result import ApplicationResult
from functools import reduce

def combine_results(result1, result2):
    (status1, message1) = result1
    (status2, message2) = result2

    combined_status = ApplicationResult.FAIL if status1 == ApplicationResult.FAIL or status2 == ApplicationResult.FAIL else ApplicationResult.PASS
    combined_message = " ".join([message1, message2])

    return (combined_status, combined_message)

def process_application(application, *criteria):
    if not criteria:
        return (ApplicationResult.PASS, "Nothing to check.")

    return reduce(combine_results, [criterion(application) for criterion in criteria])

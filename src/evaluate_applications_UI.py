import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.application import Application
from src.criteria_fetcher import fetch_criteria
from src.process_application import process_application

def get_application_details(selected_criteria, all_criteria):
    application_data = {}

    for criterion in all_criteria:
        for field, field_info in criterion["required_fields"].items():

            value = input(field_info["prompt"])

            application_data[field] = value.lower() == "true" if field_info["type"] == "boolean" else value

    return Application(**application_data)

def display_criteria(criteria):
    print("Available Criteria:")

    for i, criterion_name in enumerate(criteria, start = 1):
        print(f"{i}. {criterion_name}")

def main():
    criteria = fetch_criteria()

    while True:
        display_criteria(criteria)

        selected_criteria_indices = input("Select criteria numbers separated by commas: ")

        selected_criteria = [list(criteria.values())[int(i) - 1] for i in selected_criteria_indices.split(',')]

        application = get_application_details(selected_criteria, criteria.values())

        result = process_application(application, *[criterion["evaluate"] for criterion in selected_criteria])

        print("Result:", result)

        if input("Process another application? (yes/no): ").lower() != "yes":
            break

if __name__ == "__main__":
    main()

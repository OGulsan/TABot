import os
import sys
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv(".env")  # Load variables from .env

access_token = os.getenv("CANVAS_API_KEY")  # Retrieve Canvas Access token
api_url = os.getenv("CANVAS_BASE_URL")  # Retrieve Canvas API URL

# Set up HTTP authentication header
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

def returnAssignmentsDict(courseID):
    # Set up the URL for the assignments API endpoint
    url = '{}/courses/{}/assignments'.format(api_url, courseID)

    # Make a GET request and pass in the Access Token in the header for authentication purposes
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Request was successful, parse the response into a list of assignments
        assignments = response.json()

        # Initialize a dictionary to contain relevant information about assignments
        assignmentDict = {}

        for i, assignment in enumerate(assignments):
            # Build up assignment key
            assignment_key = {
                'assignment_id': assignment['id'],
                'assignment_name': assignment['name'],
                'points_possible': assignment['points_possible']
            }

            # Check if assignment has no due date
            if assignment['due_at'] is None:
                assignment_key['assignment_due_date'] = 'No due date'
            else:
                # Convert string representation of due date into datetime object
                date_object = datetime.strptime(assignment['due_at'], '%Y-%m-%dT%H:%M:%SZ')

                # Extract the month, day, and time components
                month = date_object.month
                day = date_object.day
                time = date_object.time()
                # Set the assignment's due date 
                assignment_key['assignment_due_date'] = '{}/{} at {}'.format(month, day, time)

            # Add assignment and its info to dictionary
            assignmentDict['Assignment {}'.format(i+1)] = assignment_key

        return assignmentDict
    else:
        # Request failed
        print('Failed to list courses. Status code: {}'.format(response.status_code))
        sys.exit(1)


if __name__ == '__main__':
    courseID = input("Enter course ID for which you want the assignment information: ")
    # Assignments: key - assignment number, value - dictionary of info about assignment
    assignments = returnAssignmentsDict(courseID=courseID)

    for key, value in assignments.items():
        if value['assignment_due_date'] == 'No due date':
            print('{}: {}\n{}\n-----------------\n'.format(key, value['assignment_name'], value['assignment_due_date']))
        else:
            print('{}: {}\ndue on {}\n-----------------\n'.format(key, value['assignment_name'], value['assignment_due_date']))

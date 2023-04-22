import requests
import os
import sys
from datetime import datetime
from dotenv import load_dotenv


api_url = "https://templeu.instructure.com/api/v1"

load_dotenv(".env")  # loads variables from .env
access_token = os.getenv("CANVAS_ACCESS_TOKEN") # retrieve Canvas Access token

# setup HTTP authentication header
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

def returnAssignmentsDict(courseID):
    # Set up the URL for the assignments API endpoint
    url = '{}/courses/{}/assignments'.format(api_url, courseID)

     # make a get request and pass in the Access Token in the header for authentication purposes
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Request was successful, parse the response into a list of assignments
        assignments = response.json()

        # init dict to contain relevant information about assignments
        assignmentDict = {}

        for i,assignment in enumerate(assignments):
            # convert string representation of due date into datetime object
            date_object = datetime.strptime(assignment['due_at'], '%Y-%m-%dT%H:%M:%SZ')

            # Extract the month, day, and time components
            month = date_object.month
            day = date_object.day
            time = date_object.time()
            
            # build up assignment key
            assignment_key = {
            'assignment_id': assignment['id'],
            'assignment_name': assignment['name'],
            'assignment_due_date': '{}/{} at {}'.format(month, day, time)}  

            # add asignment and it's info to dict
            assignmentDict['Assignment {}'.format(i+1)] = assignment_key

        return assignmentDict
    else:
        # Request failed
        print('Failed to list courses. Status code: {}'.format(response.status_code))
        sys.exit(1)

if __name__ == '__main__':
    courseID = input("Enter course id you want the assignment information about: ")
    # assignments: key - assignment number, value - dict of info about assignment
    assignments = returnAssignmentsDict(courseID=courseID)

    for key, value in assignments.items():
        print('{}: {}\ndue on {}\n-----------------\n'.format(key, value['assignment_name'], value['assignment_due_date']))
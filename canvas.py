import os
import sys
from datetime import datetime

import requests
from dotenv import load_dotenv



load_dotenv(".env")  # loads variables from .env

access_token = os.getenv("CANVAS_API_KEY") # retrieve Canvas Access token
api_url = os.getenv("CANVAS_BASE_URL") # retrieve canvas api url

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
            # build up assignment key
            assignment_key = {
            'assignment_id': assignment['id'],
            'assignment_name': assignment['name'],
            'points_possible': assignment['points_possible']}  

            # check if assignment has no due date
            if assignment['due_at'] is None:
                assignment_key['assignment_due_date'] = 'No due date'
            else:
                # convert string representation of due date into datetime object
                date_object = datetime.strptime(assignment['due_at'], '%Y-%m-%dT%H:%M:%SZ')

                # Extract the month, day, and time components
                month = date_object.month
                day = date_object.day
                time = date_object.time()
                # set the assignments due date 
                assignment_key['assignment_due_date'] = '{}/{} at {}'.format(month, day, time)

            # add assignment and it's info to dict
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
        if(value['assignment_due_date'] == 'No due date'):
            print('{}: {}\n{}\n-----------------\n'.format(key, value['assignment_name'], value['assignment_due_date']))
        else:
            print('{}: {}\ndue on {}\n-----------------\n'.format(key, value['assignment_name'], value['assignment_due_date']))

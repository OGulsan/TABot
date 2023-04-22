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

def printAssignments(courseID):
    # Set up the URL for the assignments API endpoint
    url = '{}/courses/{}/assignments'.format(api_url, courseID)

     # make a get request and pass in the Access Token in the header for authentication purposes
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Request was successful, parse the response into a list of assignments
        assignments = response.json()

        for i,assignment in enumerate(assignments):
            # display info about each assignment
            assignment_id = assignment['id']
            assignment_name = assignment['name']
            assignment_due_date = assignment['due_at']
            date_object = datetime.strptime(assignment_due_date, '%Y-%m-%dT%H:%M:%SZ')

            # Extract the month, day, and time components
            month = date_object.month
            day = date_object.day
            time = date_object.time()
            

            # ... perform other operations with assignment object
            print(i + 1)
            print("Assignment ID: ", assignment_id)
            print("Assignment Name: ", assignment_name)
            print(f'Assignment due date: {month}/{day} at {time}')
            print("----------------------------------")
            print()
        #print(type(assignments[0]))
    else:
        # Request failed
        print('Failed to list courses. Status code: {}'.format(response.status_code))
        sys.exit(1)

if __name__ == '__main__':
    courseID = input("Enter course id you want the assignment information about: ")
    printAssignments(courseID=courseID)

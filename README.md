How to Run the Project
1. Clone the Repository
git clone <repository-url>
cd BugTracker
2. Create a Virtual Environment
python -m venv venv
3. Activate the Virtual Environment
Windows PowerShell:
.\\venv\\Scripts\\Activate.ps1
If using Command Prompt:
venv\\Scripts\\activate
4. Install Dependencies
pip install -r requirements.txt

5. Start the Development Server
python manage.py runserver
The API will be available at:
http://127.0.0.1:8000/
API Endpoints
Issues & Reporters
Get All Issues
GET /issuelist/
GET /issue/?id=1
GET /reporterlist/
GET /reporter/?id=1
POST /issues/create/
Returns a list of all bugs/issues.
Example response:
[
    {
        "id": 1,
        "title": "Login button not working",
        "description": "User cannot login using valid credentials",
        "status": "Open",
        "priority": "High"
    }
]
Get an Issue by ID
GET /api/issues/<id>/
Returns details of a specific issue.
Example:
GET /api/issues/1/
Create an Issue
POST /api/issues/
Creates a new bug/issue.
Example request:
{
    "title": "Login button not working",
    "description": "Login button does not respond",
    "status": "Open",
    "priority": "High"
}
The API validates the required fields and returns an appropriate validation error if required information is missing


Design Decision
I chose to use Django REST Framework  to handle conversion and validation between Python/Django model objects and JSON data.
For example, when creating an issue through the API, validates the incoming request before saving the data.
This provides a clean separation between:
API request/response handling
Data validation
Database models
It also prevents invalid data, such as an issue being created without a required title, from being saved to the database.
This makes the application easier to maintain and extend as additional fields and validation rules are added.
Error Handling
The API returns appropriate HTTP status codes for different required fields.
Examples:
200 OK – Request completed successfully
201 Created – New issue/reporter created
400 Bad Request – Invalid input or missing required fields
404 Not Found – Requested issue/reporter does not exist
500 Internal Server Error – Unexpected server-side error
Example validation response:
{
    "title": [
        "This field is required."
    ]
}
Testing the API
The APIs can be tested using:
Postman
Django REST Framework Browsable API
PyCharm HTTP Client
Example:
GET http://127.0.0.1:8000/api/issues/

Author
Archana Ravinder
Python / Django BugTracker Project

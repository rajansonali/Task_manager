**Task Manager API (Flask)**
Project Overview
This project is a backend API for managing comments on tasks, built using Flask.
It implements full CRUD functionality (Create, Read, Update, Delete) for comments and includes automated tests to ensure correctness.

**Features:**
Add a comment to a task (POST /api/tasks/<task_id>/comments)

List all comments for a task (GET /api/tasks/<task_id>/comments)

Update a comment (PUT /api/tasks/<task_id>/comments/<comment_id>)

Delete a comment (DELETE /api/tasks/<task_id>/comments/<comment_id>)

Automated tests using pytest

Demo script (demo_crud.py) to showcase CRUD operations

**Getting Started:**
Prerequisites:
Python 3.13+
pip package manager

**Installation**

1.Clone the repository:
git clone https://github.com/<rajansonali>/Task_manager.git
cd Task_manager


2.Install dependencies:
pip install -r requirements.txt


3.Run the Flask server:
python run.py
Server runs at http://127.0.0.1:5000

**Running Tests**
pytest tests/test_comments.py

**Demo Script:**
You can run demo_crud.py to see all CRUD operations in action:
python demo_crud.py

**API Endpoints:**
Method	Endpoint	Description
POST	/api/tasks/<task_id>/comments	Add a new comment
GET	/api/tasks/<task_id>/comments	List all comments
PUT	/api/tasks/<task_id>/comments/<comment_id>	Update a comment
DELETE	/api/tasks/<task_id>/comments/<comment_id>	Delete a comment

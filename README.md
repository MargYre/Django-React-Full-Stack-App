# Django-React-Full-Stack-App
Using Python and JavaScript to create a full-stack web application.
Django for the backend and React for the frontend, as well as setting up authentication using JWT tokens.

## Prerequisites
- Python 3.x
- Node.js
- npm or yarn
- Git

## Installation

### 1. Clone the Repository
```bash
git https://github.com/MargYre/Django-React-Full-Stack-App.git
cd Django-React-Full-Stack-App
```


### 2. Setup Backend
a. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
b. Install Backend Dependencies
```bash
pip install -r requirements.txt
c. Apply Migrations
```
```bash
python manage.py migrate
```
d. Create a Superuser
```bash
python manage.py createsuperuser
```
e. Run the Backend Server
```bash
python manage.py runserver
```
### 3. Setup Frontend
a. Navigate to the Frontend Directory
```bash
cd frontend
```
b. Install Frontend Dependencies
```bash
npm install
# or
yarn install
```
c. Run the Frontend Development Server
```bash
npm run dev
# or
yarn dev
```
### Running the Application
Backend: Make sure the backend server is running on http://127.0.0.1:8000/.
Frontend: The frontend development server should be running on http://localhost:3000/.

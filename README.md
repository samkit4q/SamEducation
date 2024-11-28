Sam Education: Education in Burundi
Project Overview
Sam Education: Education in Burundi is a web-based platform designed to provide accessible and high-quality educational resources to students in Burundi. The platform includes features such as user registration and login, course browsing, assignment management, and teacher-student interactions. It leverages Firebase for authentication and notifications and Dropbox for file storage.

Key Features
User Registration and Login:
Users can register as either a student or teacher.
Secure authentication via Firebase.
Student Dashboard:
View courses and educational materials.
Submit assignments and access progress reports.
Teacher Dashboard:
Upload and manage courses.
Send assignments to students, grade submissions, and send progress reports.
Offline Functionality:
Download content for offline access.
Notifications:
Push and email notifications for updates (e.g., new courses, assignments).
Multilingual Support:
English is supported with plans for future language expansions.
Technologies Used
Frontend
HTML5, CSS3: Core structure and styling.
JavaScript: Interactive features and client-side logic.
React.js: Modular and dynamic component design (if used in specific sections).
Responsive Design: Optimized for mobile and desktop users.
Backend
Node.js and Express.js: Backend server and API handling.
Firebase:
Authentication: Manage user login and registration.
Notifications: Send push/email updates.
Dropbox:
File Storage: Store and retrieve course materials and assignments.
Database
Firebase Firestore:
Store user data, course details, and other related information.
Hosting
Firebase Hosting (or alternative, if applicable).
Project Structure
bash
project/
├── frontend/
│   ├── index.html
│   ├── css/
│   │   ├── styles.css
│   │   └── login.css
│   ├── js/
│   │   ├── dashboard.js
│   │   └── courses.js
│   └── assets/
│       └── images/
├── backend/
│   ├── firebase.js
│   ├── authRoutes.js
│   ├── keys/
│   │   └── serviceAccountKey.json
│   ├── controllers/
│   │   ├── userController.js
│   │   └── assignmentController.js
│   ├── routes/
│   │   ├── userRoutes.js
│   │   └── assignmentRoutes.js
│   └── app.js
├── .env
├── .gitignore
└── README.md
Setup Instructions
1. Prerequisites
Node.js installed (Download Here)
Firebase account with project set up
Dropbox API Key
2. Installation
Clone the repository:

bash
git clone https://github.com/your-repo-url.git
cd sam-education
Install dependencies:

bash
npm install
Create a .env file with the following keys:

3. Running the Project
Frontend
Navigate to the frontend/ directory and serve the files (e.g., with live-server or similar tools).
Backend
Start the Node.js server:
bash
node app.js
Backend will run on http://localhost:5000 by default.
Usage
Register:
Students and teachers can sign up via the registration page.
Login:
Users are redirected to their respective dashboards based on roles.
Dashboard Features:
Students: View courses, download content, and submit assignments.
Teachers: Upload courses, send assignments, and grade submissions.
Future Improvements
Enhanced multilingual support (e.g., Kirundi, French).
AI-driven personalized course recommendations.
Real-time chat between students and teachers.
License
This project is licensed under the MIT License.
Steps to Run the Project
1. Prerequisites
Before running the project, ensure you have the following installed:

Node.js (Download: https://nodejs.org/)
A Firebase account and project set up for authentication and Firestore.
A Dropbox API key for file storage.
2. Clone the Repository
Open your terminal and run:

git clone https://github.com/your-repo-url.git
Navigate into the project directory:
cd sam-education
3. Backend Setup
Navigate to the backend folder:


cd backend
Install dependencies:


npm install
Add the Firebase service account key:

Place your Firebase service account key file in the keys folder.
Ensure the file is named serviceAccountKey.json.
Create a .env file and add the following variables:

env
Copy code
FIREBASE_API_KEY=your-firebase-api-key
DROPBOX_API_KEY=your-dropbox-api-key
Start the backend server:

bash
Copy code
node app.js
By default, the server will run on http://localhost:3000.

4. Frontend Setup
Navigate to the frontend folder:

bash
Copy code
cd ../frontend
Use a live server to host the frontend files. For example:

Install live-server globally:
bash
npm install -g live-server
Start the server:
bash
live-server
The frontend will open in your default web browser.

5. Running the Application
Access the Frontend:

Open your browser and navigate to the URL provided by live-server.
Alternatively, open index.html in your browser if you are not using live-server.
Interact with the Backend:

The frontend communicates with the backend API running on http://localhost:3000.
Ensure the backend server is running before interacting with features like login, registration, and course management.

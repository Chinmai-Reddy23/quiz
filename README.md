🎯 MCQ Quiz Application – Python

A desktop-based MCQ Quiz Application developed using Python and Tkinter. The application allows users to register, log in, select a difficulty level, answer randomly selected questions, calculate scores, and view a leaderboard.

🚀 Features
🔐 User Registration & Login
🎯 Difficulty Selection
Easy
Medium
Hard
Mixed
📚 90 Python/Programming MCQs
30 Easy
30 Medium
30 Hard
🎲 Automatic Question Selection
🔄 Different Questions on Play Again
Previously attempted questions are not repeated until the available question bank is exhausted.
🏷️ Difficulty Level Display
📂 Question Category Display
🧮 Automatic Score Calculation
🏆 Leaderboard
💾 SQLite Database
📊 Percentage Calculation
🔒 Password Hashing
🖥️ GUI using Tkinter
🛠️ Technologies Used
Python
Tkinter – Graphical User Interface
SQLite3 – Database management
Hashlib – Password hashing
Random – Random question selection
Datetime – Quiz date and time management
🎮 Scoring System
Difficulty	Points
Easy	1
Medium	2
Hard	3

The application calculates the total score and percentage automatically after completing the quiz.

🔄 Smart Question Selection

The application does not simply shuffle the same questions when the user clicks Play Again.

It keeps track of previously attempted question IDs:

Quiz 1
   ↓
10 Questions
   ↓
Play Again
   ↓
10 DIFFERENT Questions
   ↓
Play Again
   ↓
10 DIFFERENT Questions

Once all questions of the selected difficulty have been used, a new question cycle begins.

🗄️ Database

The application uses SQLite to store:

Users
User ID
Username
Password
Questions
Question
Four options
Correct answer
Difficulty
Category
Scores
Username
Score
Total questions
Percentage
Difficulty
Quiz date

The database is automatically created when the application starts.

📁 Project Structure
MCQ-Quiz-Application/
│
├── quiz_app.py
├── quiz_application.db
└── README.md

quiz_application.db is generated automatically when the application runs.

▶️ How to Run
1. Install Python

Make sure Python is installed:

python --version
2. Clone the Repository
git clone https://github.com/your-username/MCQ-Quiz-Application.git
3. Navigate to the Project
cd MCQ-Quiz-Application
4. Run the Application
python quiz_app.py
📌 Application Workflow
Start Application
       ↓
Register / Login
       ↓
Select Difficulty
       ↓
Automatic Question Selection
       ↓
Answer 10 MCQs
       ↓
Score Calculation
       ↓
Display Result
       ↓
Save Score
       ↓
Leaderboard
       ↓
Play Again / Change Difficulty / Logout
🎯 Objective

The main objective of this project is to develop an interactive quiz platform that provides automatically selected MCQ questions based on difficulty level, prevents immediate question repetition, calculates scores, and maintains a leaderboard using a local database.

🔮 Future Enhancements
Add more programming languages such as Java, C, C++, and JavaScript.
Add a countdown timer.
Add negative marking.
Add an admin panel for adding questions.
Add question search and filtering.

⭐ Project Highlights

Python | Tkinter | SQLite | MCQ Quiz | Random Question Selection | Score Calculation | Leaderboard | User Authentication
Add graphical performance statistics.
Add a web version using Flask or Django.
Add online multiplayer functionality.

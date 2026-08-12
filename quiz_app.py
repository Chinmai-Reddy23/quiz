import tkinter as tk
from tkinter import messagebox
import sqlite3
import random
import hashlib
from datetime import datetime

# DATABASE

DB_NAME = "quiz_application.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            question_id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_answer TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            category TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            score_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            total_questions INTEGER NOT NULL,
            percentage REAL NOT NULL,
            difficulty TEXT NOT NULL,
            quiz_date TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        )
    """)

    conn.commit()
    conn.close()

    seed_questions()

# QUESTION BANK

def seed_questions():

    conn = get_connection()
    cursor = conn.cursor()

    # Check how many questions currently exist

    cursor.execute("""
        SELECT COUNT(*)
        FROM questions
    """)

    total_questions = cursor.fetchone()[0]

    # If old database contains fewer than 90 questions,
    # replace the old question bank.

    if total_questions < 90:

        cursor.execute("""
            DELETE FROM questions
        """)

        conn.commit()

    # Check again
    cursor.execute("""
        SELECT COUNT(*)
        FROM questions
    """)

    total_questions = cursor.fetchone()[0]

    if total_questions >= 90:

        conn.close()
        return

    # 90 QUESTIONS

    questions = [

        # EASY - 30

        (
            "Which keyword is used to define a function in Python?",
            "function", "def", "fun", "define",
            "B", "Easy", "Python"
        ),

        (
            "Which symbol is used for comments in Python?",
            "//", "/*", "#", "--",
            "C", "Easy", "Python"
        ),

        (
            "Which function displays output in Python?",
            "show()", "display()", "print()", "output()",
            "C", "Easy", "Python"
        ),

        (
            "Which brackets are used to create a list?",
            "()", "{}", "[]", "<>",
            "C", "Easy", "Python"
        ),

        (
            "Which data type stores True or False?",
            "int", "float", "bool", "string",
            "C", "Easy", "Python"
        ),

        (
            "Which keyword is used to create a class?",
            "class", "object", "struct", "define",
            "A", "Easy", "Python"
        ),

        (
            "Which function returns the length of a list?",
            "size()", "length()", "len()", "count()",
            "C", "Easy", "Python"
        ),

        (
            "Which operator is used for exponentiation?",
            "^", "**", "//", "%%",
            "B", "Easy", "Python"
        ),

        (
            "Which of these is immutable?",
            "List", "Dictionary", "Set", "Tuple",
            "D", "Easy", "Python"
        ),

        (
            "Which keyword is used to import a module?",
            "include", "import", "require", "using",
            "B", "Easy", "Python"
        ),

        (
            "Which method adds an element to a list?",
            "append()", "add()", "push()", "insertEnd()",
            "A", "Easy", "Python"
        ),

        (
            "Which function converts a value to an integer?",
            "str()", "float()", "int()", "number()",
            "C", "Easy", "Python"
        ),

        (
            "Which keyword is used to check a condition?",
            "when", "if", "check", "condition",
            "B", "Easy", "Python"
        ),

        (
            "Which loop is commonly used to iterate over a sequence?",
            "repeat", "loop", "for", "iterate",
            "C", "Easy", "Python"
        ),

        (
            "Which operator checks equality?",
            "=", "==", "===", "!=",
            "B", "Easy", "Python"
        ),

        (
            "Which keyword terminates a loop?",
            "stop", "exit", "break", "end",
            "C", "Easy", "Python"
        ),

        (
            "Which keyword skips the current loop iteration?",
            "skip", "continue", "pass", "next",
            "B", "Easy", "Python"
        ),

        (
            "Which function accepts input from the user?",
            "scan()", "read()", "input()", "get()",
            "C", "Easy", "Python"
        ),

        (
            "Which operator performs floor division?",
            "/", "//", "%", "**",
            "B", "Easy", "Python"
        ),

        (
            "Which operator returns the remainder?",
            "/", "//", "%", "**",
            "C", "Easy", "Python"
        ),

        (
            "Which collection does not allow duplicate values?",
            "List", "Set", "Tuple", "String",
            "B", "Easy", "Python"
        ),

        (
            "Which keyword sends a value back from a function?",
            "send", "return", "output", "give",
            "B", "Easy", "Python"
        ),

        (
            "Which function converts a value into a string?",
            "string()", "str()", "text()", "convert()",
            "B", "Easy", "Python"
        ),

        (
            "Which function converts a value into a float?",
            "float()", "decimal()", "double()", "real()",
            "A", "Easy", "Python"
        ),

        (
            "Which function returns the largest value?",
            "maximum()", "max()", "highest()", "top()",
            "B", "Easy", "Python"
        ),

        (
            "Which function returns the smallest value?",
            "minimum()", "min()", "lowest()", "small()",
            "B", "Easy", "Python"
        ),

        (
            "Which keyword represents the absence of a value?",
            "null", "empty", "None", "void",
            "C", "Easy", "Python"
        ),

        (
            "Which extension is normally used for Python files?",
            ".java", ".py", ".python", ".pt",
            "B", "Easy", "Python"
        ),

        (
            "Which function returns the absolute value?",
            "absolute()", "abs()", "positive()", "value()",
            "B", "Easy", "Python"
        ),

        (
            "Which keyword is used to handle exceptions?",
            "catch", "try", "error", "exception",
            "B", "Easy", "Python"
        ),

        # MEDIUM - 30

        (
            "What is the time complexity of binary search?",
            "O(n)", "O(log n)", "O(n²)", "O(1)",
            "B", "Medium", "Algorithms"
        ),

        (
            "Which data structure follows LIFO?",
            "Queue", "Array", "Stack", "Linked List",
            "C", "Medium", "Data Structures"
        ),

        (
            "Which data structure follows FIFO?",
            "Stack", "Queue", "Tree", "Graph",
            "B", "Medium", "Data Structures"
        ),

        (
            "Which Python structure stores key-value pairs?",
            "List", "Tuple", "Dictionary", "Set",
            "C", "Medium", "Python"
        ),

        (
            "Which method removes and returns the last list element?",
            "delete()", "remove()", "pop()", "clear()",
            "C", "Medium", "Python"
        ),

        (
            "Which keyword begins an exception handling block?",
            "catch", "try", "error", "exception",
            "B", "Medium", "Python"
        ),

        (
            "What does SQL stand for?",
            "Structured Query Language",
            "Simple Query Language",
            "Standard Query Language",
            "System Query Language",
            "A", "Medium", "SQL"
        ),

        (
            "Which SQL command retrieves data?",
            "GET", "OPEN", "SELECT", "FETCH",
            "C", "Medium", "SQL"
        ),

        (
            "Which sorting algorithm compares adjacent elements?",
            "Merge Sort", "Bubble Sort", "Quick Sort", "Heap Sort",
            "B", "Medium", "Algorithms"
        ),

        (
            "Which graph traversal uses a queue?",
            "DFS", "BFS", "Binary Search", "Hashing",
            "B", "Medium", "Algorithms"
        ),

        (
            "What is the default return value of a Python function with no return statement?",
            "0", "False", "None", "Empty",
            "C", "Medium", "Python"
        ),

        (
            "Which collection does not allow duplicate elements?",
            "List", "Tuple", "Set", "Array",
            "C", "Medium", "Python"
        ),

        (
            "Which function returns the largest number?",
            "large()", "maximum()", "max()", "highest()",
            "C", "Medium", "Python"
        ),

        (
            "Which function returns the smallest number?",
            "small()", "min()", "minimum()", "low()",
            "B", "Medium", "Python"
        ),

        (
            "Which SQL command adds a new record?",
            "ADD", "INSERT", "CREATE", "UPDATE",
            "B", "Medium", "SQL"
        ),

        (
            "Which SQL command modifies existing records?",
            "CHANGE", "MODIFY", "UPDATE", "ALTER",
            "C", "Medium", "SQL"
        ),

        (
            "Which SQL command removes selected records?",
            "DROP", "DELETE", "REMOVE", "CLEAR",
            "B", "Medium", "SQL"
        ),

        (
            "Which keyword is used to create a loop over a range?",
            "loop", "for", "repeat", "iterate",
            "B", "Medium", "Python"
        ),

        (
            "What is a tuple in Python?",
            "Mutable collection",
            "Immutable collection",
            "Function",
            "Class",
            "B", "Medium", "Python"
        ),

        (
            "Which operator represents logical AND in Python?",
            "&", "and", "&&", "AND",
            "B", "Medium", "Python"
        ),

        (
            "Which operator represents logical OR in Python?",
            "|", "or", "||", "OR",
            "B", "Medium", "Python"
        ),

        (
            "Which function creates a sequence of numbers?",
            "numbers()", "range()", "sequence()", "series()",
            "B", "Medium", "Python"
        ),

        (
            "Which method converts a string to lowercase?",
            "lower()", "small()", "lowercase()", "down()",
            "A", "Medium", "Python"
        ),

        (
            "Which method converts a string to uppercase?",
            "upper()", "capital()", "uppercase()", "up()",
            "A", "Medium", "Python"
        ),

        (
            "Which SQL clause filters rows?",
            "HAVING", "WHERE", "FILTER", "SELECT",
            "B", "Medium", "SQL"
        ),

        (
            "Which SQL clause groups records?",
            "GROUP BY", "ORDER BY", "COLLECT", "GROUP",
            "A", "Medium", "SQL"
        ),

        (
            "Which SQL clause sorts query results?",
            "SORT BY", "ORDER BY", "ARRANGE", "SORT",
            "B", "Medium", "SQL"
        ),

        (
            "Which algorithm uses a pivot element?",
            "Bubble Sort", "Quick Sort", "Merge Sort", "Selection Sort",
            "B", "Medium", "Algorithms"
        ),

        (
            "Which data structure stores elements sequentially?",
            "Array", "Graph", "Tree", "Hash Table",
            "A", "Medium", "Data Structures"
        ),

        (
            "Which search algorithm requires a sorted array?",
            "Linear Search", "Binary Search", "DFS", "BFS",
            "B", "Medium", "Algorithms"
        ),

        # HARD - 30

        (
            "Which OOP concept allows a class to inherit from multiple classes?",
            "Encapsulation", "Polymorphism",
            "Multiple inheritance", "Abstraction",
            "C", "Hard", "OOP"
        ),

        (
            "What is the average search complexity of a hash table?",
            "O(n)", "O(log n)", "O(1)", "O(n²)",
            "C", "Hard", "Data Structures"
        ),

        (
            "Which algorithm finds shortest paths from a source in a graph with non-negative weights?",
            "Bubble Sort", "Dijkstra's Algorithm",
            "Binary Search", "Merge Sort",
            "B", "Hard", "Algorithms"
        ),

        (
            "Which sorting algorithm has average O(n log n) complexity?",
            "Bubble Sort", "Selection Sort",
            "Merge Sort", "Linear Search",
            "C", "Hard", "Algorithms"
        ),

        (
            "Which Python feature can remember variables from an enclosing scope?",
            "Inheritance", "Closure", "Polymorphism", "Recursion",
            "B", "Hard", "Python"
        ),

        (
            "Which SQL command completely removes a table?",
            "DELETE", "REMOVE", "DROP", "CLEAR",
            "C", "Hard", "SQL"
        ),

        (
            "Which BST traversal produces sorted order?",
            "Preorder", "Postorder", "Inorder", "Level Order",
            "C", "Hard", "Data Structures"
        ),

        (
            "What is the worst-case complexity of Quick Sort?",
            "O(log n)", "O(n)", "O(n log n)", "O(n²)",
            "D", "Hard", "Algorithms"
        ),

        (
            "Which algorithm uses divide and conquer?",
            "Merge Sort", "Linear Search", "Bubble Sort", "Counting Sort",
            "A", "Hard", "Algorithms"
        ),

        (
            "Which data structure is used to implement recursion?",
            "Queue", "Stack", "Heap", "Graph",
            "B", "Hard", "Data Structures"
        ),

        (
            "Which OOP concept allows one interface to have multiple implementations?",
            "Encapsulation", "Inheritance",
            "Polymorphism", "Compilation",
            "C", "Hard", "OOP"
        ),

        (
            "Which SQL clause filters grouped results?",
            "WHERE", "HAVING", "GROUP", "FILTER",
            "B", "Hard", "SQL"
        ),

        (
            "What is the worst-case complexity of binary search?",
            "O(1)", "O(log n)", "O(n)", "O(n²)",
            "B", "Hard", "Algorithms"
        ),

        (
            "Which data structure is commonly used in BFS?",
            "Stack", "Queue", "Heap", "Set",
            "B", "Hard", "Algorithms"
        ),

        (
            "Which OOP principle hides implementation details?",
            "Inheritance", "Abstraction",
            "Polymorphism", "Overloading",
            "B", "Hard", "OOP"
        ),

        (
            "Which algorithm finds a minimum spanning tree?",
            "Kruskal's Algorithm", "Binary Search",
            "Dijkstra's Algorithm", "Bubble Sort",
            "A", "Hard", "Algorithms"
        ),

        (
            "Which algorithm also finds a minimum spanning tree?",
            "Prim's Algorithm", "Linear Search",
            "Quick Sort", "DFS",
            "A", "Hard", "Algorithms"
        ),

        (
            "Which data structure is commonly used in optimized Dijkstra's Algorithm?",
            "Stack", "Priority Queue", "Array", "Linked List",
            "B", "Hard", "Algorithms"
        ),

        (
            "What is the space complexity of recursive DFS in a graph?",
            "O(1)", "O(V)", "O(E²)", "O(V²)",
            "B", "Hard", "Graphs"
        ),

        (
            "Which tree is self-balancing?",
            "Binary Tree", "AVL Tree", "Heap", "Trie",
            "B", "Hard", "Trees"
        ),

        (
            "What is the height of a balanced binary search tree approximately?",
            "O(n)", "O(log n)", "O(n²)", "O(1)",
            "B", "Hard", "Trees"
        ),

        (
            "Which data structure is useful for prefix searching?",
            "Stack", "Trie", "Queue", "Heap",
            "B", "Hard", "Data Structures"
        ),

        (
            "Which technique stores previously calculated results?",
            "Greedy", "Memoization", "Backtracking", "Hashing",
            "B", "Hard", "Algorithms"
        ),

        (
            "Which technique solves problems with overlapping subproblems?",
            "Dynamic Programming",
            "Binary Search",
            "Sorting",
            "Hashing",
            "A", "Hard", "Algorithms"
        ),

        (
            "Which sorting algorithm is stable by default?",
            "Quick Sort", "Heap Sort", "Merge Sort", "Selection Sort",
            "C", "Hard", "Algorithms"
        ),

        (
            "Which SQL constraint uniquely identifies each row?",
            "FOREIGN KEY", "PRIMARY KEY", "CHECK", "DEFAULT",
            "B", "Hard", "SQL"
        ),

        (
            "Which SQL key references another table's primary key?",
            "PRIMARY KEY", "FOREIGN KEY", "UNIQUE KEY", "CHECK",
            "B", "Hard", "SQL"
        ),

        (
            "Which Python feature allows custom behavior for operators?",
            "Operator overloading", "Inheritance",
            "Decorators", "Generators",
            "A", "Hard", "Python"
        ),

        (
            "Which keyword is used to produce values from a generator?",
            "generate", "yield", "generator", "return",
            "B", "Hard", "Python"
        ),

        (
            "Which technique explores possible solutions and abandons invalid paths?",
            "Backtracking", "Hashing", "Sorting", "Indexing",
            "A", "Hard", "Algorithms"
        )
    ]

    # INSERT QUESTIONS

    cursor.executemany("""
        INSERT INTO questions (
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer,
            difficulty,
            category
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, questions)

    conn.commit()
    conn.close()

# PASSWORD HASHING

def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()

# MAIN APPLICATION

class QuizApplication:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "MCQ Quiz Application"
        )

        self.root.geometry(
            "950x700"
        )

        self.root.resizable(
            False,
            False
        )

        # USER

        self.current_user_id = None
        self.current_username = None

        # QUIZ VARIABLES

        self.questions = []

        self.current_question_index = 0

        self.score = 0

        self.correct_answers = 0

        self.selected_difficulty = ""

        # USED QUESTION IDs
        #
        # These sets prevent the same questions appearing
        # again when Play Again is clicked.

        self.used_questions = {

            "Easy": set(),

            "Medium": set(),

            "Hard": set(),

            "Mixed": set()
        }

        self.setup_login_screen()

    # CLEAR SCREEN

    def clear_screen(self):

        for widget in self.root.winfo_children():

            widget.destroy()

    # LOGIN SCREEN

    def setup_login_screen(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="MCQ QUIZ APPLICATION",
            font=("Arial", 28, "bold")
        ).pack(
            pady=45
        )

        frame = tk.Frame(
            self.root
        )

        frame.pack()

        tk.Label(
            frame,
            text="Username:",
            font=("Arial", 14)
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=15
        )

        self.username_entry = tk.Entry(
            frame,
            font=("Arial", 14),
            width=25
        )

        self.username_entry.grid(
            row=0,
            column=1
        )

        tk.Label(
            frame,
            text="Password:",
            font=("Arial", 14)
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=15
        )

        self.password_entry = tk.Entry(
            frame,
            font=("Arial", 14),
            width=25,
            show="*"
        )

        self.password_entry.grid(
            row=1,
            column=1
        )

        tk.Button(
            self.root,
            text="LOGIN",
            font=("Arial", 14, "bold"),
            width=18,
            command=self.login
        ).pack(
            pady=12
        )

        tk.Button(
            self.root,
            text="REGISTER",
            font=("Arial", 14, "bold"),
            width=18,
            command=self.register_screen
        ).pack(
            pady=8
        )

    # REGISTER SCREEN

    def register_screen(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="CREATE ACCOUNT",
            font=("Arial", 26, "bold")
        ).pack(
            pady=45
        )

        frame = tk.Frame(
            self.root
        )

        frame.pack()

        tk.Label(
            frame,
            text="Username:",
            font=("Arial", 14)
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=15
        )

        self.reg_username = tk.Entry(
            frame,
            font=("Arial", 14),
            width=25
        )

        self.reg_username.grid(
            row=0,
            column=1
        )

        tk.Label(
            frame,
            text="Password:",
            font=("Arial", 14)
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=15
        )

        self.reg_password = tk.Entry(
            frame,
            font=("Arial", 14),
            width=25,
            show="*"
        )

        self.reg_password.grid(
            row=1,
            column=1
        )

        tk.Button(
            self.root,
            text="CREATE ACCOUNT",
            font=("Arial", 14, "bold"),
            width=20,
            command=self.register
        ).pack(
            pady=20
        )

        tk.Button(
            self.root,
            text="BACK TO LOGIN",
            font=("Arial", 12),
            command=self.setup_login_screen
        ).pack()

    # REGISTER

    def register(self):

        username = self.reg_username.get().strip()

        password = self.reg_password.get()

        if not username or not password:

            messagebox.showwarning(
                "Input Error",
                "Please enter username and password."
            )

            return

        conn = get_connection()

        cursor = conn.cursor()

        try:

            cursor.execute("""
                INSERT INTO users (
                    username,
                    password
                )
                VALUES (?, ?)
            """, (
                username,
                hash_password(password)
            ))

            conn.commit()

            messagebox.showinfo(
                "Success",
                "Account created successfully."
            )

            self.setup_login_screen()

        except sqlite3.IntegrityError:

            messagebox.showerror(
                "Error",
                "Username already exists."
            )

        finally:

            conn.close()

    # LOGIN

    def login(self):

        username = self.username_entry.get().strip()

        password = self.password_entry.get()

        if not username or not password:

            messagebox.showwarning(
                "Input Error",
                "Enter username and password."
            )

            return

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT user_id, username
            FROM users
            WHERE username = ?
            AND password = ?
        """, (
            username,
            hash_password(password)
        ))

        user = cursor.fetchone()

        conn.close()

        if user:

            self.current_user_id = user[0]

            self.current_username = user[1]

            self.home_screen()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )

    # HOME SCREEN

    def home_screen(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text=f"Welcome, {self.current_username}",
            font=("Arial", 26, "bold")
        ).pack(
            pady=35
        )

        tk.Label(
            self.root,
            text="Select Difficulty",
            font=("Arial", 18, "bold")
        ).pack(
            pady=10
        )

        tk.Label(
            self.root,
            text="Questions will be selected automatically.",
            font=("Arial", 12)
        ).pack(
            pady=5
        )

        for difficulty in [
            "Easy",
            "Medium",
            "Hard",
            "Mixed"
        ]:

            tk.Button(
                self.root,
                text=difficulty,
                font=("Arial", 14, "bold"),
                width=22,
                command=lambda d=difficulty:
                self.start_quiz(d)
            ).pack(
                pady=7
            )

        tk.Button(
            self.root,
            text="VIEW LEADERBOARD",
            font=("Arial", 13, "bold"),
            width=22,
            command=self.leaderboard_screen
        ).pack(
            pady=20
        )

        tk.Button(
            self.root,
            text="LOGOUT",
            font=("Arial", 12),
            width=15,
            command=self.logout
        ).pack()

    # START QUIZ

    def start_quiz(self, difficulty):

        self.selected_difficulty = difficulty

        conn = get_connection()

        cursor = conn.cursor()

        # Get questions according to difficulty

        if difficulty == "Mixed":

            cursor.execute("""
                SELECT *
                FROM questions
            """)

        else:

            cursor.execute("""
                SELECT *
                FROM questions
                WHERE difficulty = ?
            """, (
                difficulty,
            ))

        all_questions = cursor.fetchall()

        conn.close()

        # SAFETY CHECK

        if len(all_questions) < 10:

            messagebox.showerror(
                "Database Error",
                f"Only {len(all_questions)} "
                f"questions found for {difficulty}.\n\n"
                "The question bank could not be loaded."
            )

            return

        # Previously used question IDs

        used_ids = self.used_questions[
            difficulty
        ]

        # Remove all previously used questions

        available_questions = [

            question

            for question in all_questions

            if question[0] not in used_ids
        ]

        # NEW CYCLE
        #
        # If fewer than 10 unused questions remain,
        # it means the entire bank has already been used.
        # Only then do we clear the history.

        if len(available_questions) < 10:

            used_ids.clear()

            available_questions = all_questions.copy()

        # RANDOMLY SELECT EXACTLY 10
        #
        # random.sample guarantees no duplicates inside
        # the same quiz.

        self.questions = random.sample(
            available_questions,
            10
        )

        # SAVE QUESTION IDs AS USED

        for question in self.questions:

            used_ids.add(
                question[0]
            )

        # RESET QUIZ

        self.current_question_index = 0

        self.score = 0

        self.correct_answers = 0

        self.quiz_screen()

    # QUIZ SCREEN

    def quiz_screen(self):

        self.clear_screen()

        data = self.questions[
            self.current_question_index
        ]

        (
            question_id,
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer,
            difficulty,
            category
        ) = data

        # TITLE

        tk.Label(
            self.root,
            text="PYTHON MCQ QUIZ",
            font=("Arial", 25, "bold")
        ).pack(
            pady=15
        )

        # QUESTION NUMBER

        tk.Label(
            self.root,
            text=(
                f"Question "
                f"{self.current_question_index + 1}"
                f" / {len(self.questions)}"
            ),
            font=("Arial", 14)
        ).pack()

        # DIFFICULTY

        tk.Label(
            self.root,
            text=f"Difficulty: {difficulty}",
            font=("Arial", 16, "bold")
        ).pack(
            pady=7
        )

        # CATEGORY

        tk.Label(
            self.root,
            text=f"Category: {category}",
            font=("Arial", 12)
        ).pack()

        # QUESTION

        tk.Label(
            self.root,
            text=question,
            font=("Arial", 17, "bold"),
            wraplength=800,
            justify="center"
        ).pack(
            pady=25
        )

        # ANSWER VARIABLE

        self.answer_var = tk.StringVar()

        self.answer_var.set("")

        options = [
            ("A", option_a),
            ("B", option_b),
            ("C", option_c),
            ("D", option_d)
        ]

        for letter, option in options:

            tk.Radiobutton(
                self.root,
                text=f"{letter}. {option}",
                variable=self.answer_var,
                value=letter,
                font=("Arial", 14),
                anchor="w",
                width=60
            ).pack(
                pady=5
            )

        # SUBMIT

        tk.Button(
            self.root,
            text="SUBMIT ANSWER",
            font=("Arial", 14, "bold"),
            width=20,
            command=self.check_answer
        ).pack(
            pady=20
        )

        # SCORE

        tk.Label(
            self.root,
            text=f"Current Score: {self.score}",
            font=("Arial", 12)
        ).pack()

    # CHECK ANSWER

    def check_answer(self):

        selected_answer = self.answer_var.get()

        if not selected_answer:

            messagebox.showwarning(
                "Select Answer",
                "Please select an answer."
            )

            return

        data = self.questions[
            self.current_question_index
        ]

        correct_answer = data[6]

        difficulty = data[7]

        # CORRECT

        if selected_answer == correct_answer:

            self.correct_answers += 1

            points = self.get_points(
                difficulty
            )

            self.score += points

            messagebox.showinfo(
                "Correct Answer",
                f"Correct!\n\n"
                f"You earned {points} point(s)."
            )

        # WRONG

        else:

            messagebox.showerror(
                "Wrong Answer",
                f"Wrong answer.\n\n"
                f"Correct Answer: {correct_answer}"
            )
        # NEXT QUESTION

        self.current_question_index += 1

        if (
            self.current_question_index
            <
            len(self.questions)
        ):

            self.quiz_screen()

        else:

            self.show_result()

    # POINT SYSTEM

    def get_points(self, difficulty):

        if difficulty == "Easy":

            return 1

        elif difficulty == "Medium":

            return 2

        elif difficulty == "Hard":

            return 3

        return 1

    # RESULT SCREEN

    def show_result(self):

        self.clear_screen()

        total = len(
            self.questions
        )

        # Calculate maximum score

        max_score = sum(
            self.get_points(
                question[7]
            )

            for question in self.questions
        )

        # Percentage

        percentage = (
            self.score
            /
            max_score
            *
            100
        )

        wrong_answers = (
            total
            -
            self.correct_answers
        )

        # TITLE

        tk.Label(
            self.root,
            text="QUIZ COMPLETED!",
            font=("Arial", 27, "bold")
        ).pack(
            pady=30
        )

        # RESULT

        result = (
            f"Player: {self.current_username}\n\n"
            f"Difficulty: {self.selected_difficulty}\n\n"
            f"Total Questions: {total}\n\n"
            f"Correct Answers: {self.correct_answers}\n\n"
            f"Wrong Answers: {wrong_answers}\n\n"
            f"Score: {self.score}/{max_score}\n\n"
            f"Percentage: {percentage:.2f}%"
        )

        tk.Label(
            self.root,
            text=result,
            font=("Arial", 16),
            justify="center"
        ).pack()

        # SAVE SCORE

        self.save_score(
            self.score,
            total,
            percentage,
            self.selected_difficulty
        )

        # PLAY AGAIN
        #
        # This calls start_quiz() again.
        #
        # Because used question IDs were stored,
        # DIFFERENT QUESTIONS will be selected.

        tk.Button(
            self.root,
            text="PLAY AGAIN",
            font=("Arial", 13, "bold"),
            width=22,
            command=lambda:
            self.start_quiz(
                self.selected_difficulty
            )
        ).pack(
            pady=12
        )

        # CHANGE DIFFICULTY

        tk.Button(
            self.root,
            text="CHANGE DIFFICULTY",
            font=("Arial", 13, "bold"),
            width=22,
            command=self.home_screen
        ).pack(
            pady=8
        )

        # LEADERBOARD

        tk.Button(
            self.root,
            text="VIEW LEADERBOARD",
            font=("Arial", 13, "bold"),
            width=22,
            command=self.leaderboard_screen
        ).pack(
            pady=8
        )

        # EXIT

        tk.Button(
            self.root,
            text="EXIT",
            font=("Arial", 12),
            width=22,
            command=self.root.destroy
        ).pack(
            pady=8
        )

    # SAVE SCORE

    def save_score(
        self,
        score,
        total_questions,
        percentage,
        difficulty
    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO scores (
                user_id,
                score,
                total_questions,
                percentage,
                difficulty,
                quiz_date
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            self.current_user_id,
            score,
            total_questions,
            percentage,
            difficulty,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        ))

        conn.commit()

        conn.close()

    # LEADERBOARD

    def leaderboard_screen(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="LEADERBOARD",
            font=("Arial", 27, "bold")
        ).pack(
            pady=25
        )

        frame = tk.Frame(
            self.root
        )

        frame.pack()

        headers = [
            "Rank",
            "Player",
            "Score",
            "Percentage",
            "Difficulty",
            "Date"
        ]

        for column, header in enumerate(headers):

            tk.Label(
                frame,
                text=header,
                font=("Arial", 10, "bold"),
                width=15,
                relief="ridge"
            ).grid(
                row=0,
                column=column
            )

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                users.username,
                scores.score,
                scores.percentage,
                scores.difficulty,
                scores.quiz_date

            FROM scores

            JOIN users
            ON scores.user_id = users.user_id

            ORDER BY
                scores.score DESC,
                scores.percentage DESC

            LIMIT 20
        """)

        results = cursor.fetchall()

        conn.close()

        # DISPLAY SCORES

        for rank, row in enumerate(
            results,
            start=1
        ):

            values = [
                rank,
                row[0],
                row[1],
                f"{row[2]:.2f}%",
                row[3],
                row[4]
            ]

            for column, value in enumerate(values):

                tk.Label(
                    frame,
                    text=value,
                    font=("Arial", 10),
                    width=15,
                    relief="ridge"
                ).grid(
                    row=rank,
                    column=column
                )

        # NO SCORES

        if not results:

            tk.Label(
                self.root,
                text="No scores available.",
                font=("Arial", 14)
            ).pack(
                pady=20
            )

        # BACK

        tk.Button(
            self.root,
            text="BACK TO HOME",
            font=("Arial", 13, "bold"),
            width=20,
            command=self.home_screen
        ).pack(
            pady=30
        )

        tk.Button(
            self.root,
            text="LOGOUT",
            font=("Arial", 12),
            width=15,
            command=self.logout
        ).pack()

    # LOGOUT

    def logout(self):

        self.current_user_id = None

        self.current_username = None

        self.questions = []

        self.current_question_index = 0

        self.score = 0

        self.correct_answers = 0

        # Reset used-question history
        self.used_questions = {

            "Easy": set(),

            "Medium": set(),

            "Hard": set(),

            "Mixed": set()
        }

        self.setup_login_screen()

# MAIN

if __name__ == "__main__":

    create_database()

    root = tk.Tk()

    app = QuizApplication(
        root
    )

    root.mainloop()
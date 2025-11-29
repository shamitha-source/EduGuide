from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# -----------------------------
# Mock function with full PDF answers
# -----------------------------
mock_answers = {
    "what is python": """Python is a high-level, interpreted programming language known for its simplicity and readability. 
It supports multiple programming paradigms including procedural, object-oriented, and functional programming.""",

    "what is a variable": """Variables are used to store data in Python. You don’t need to declare the type explicitly; Python infers it automatically.
Example:
x = 10
name = "Shamitha"
""",

    "what are data types": """Python has several built-in data types:
- Numbers: int, float, complex
- Sequence: list, tuple, range
- Text: str
- Set: set, frozenset
- Mapping: dict
- Boolean: bool
""",

    "what are operators": """Operators in Python include:
- Arithmetic: +, -, *, /, //, %, **
- Comparison: ==, !=, >, <, >=, <=
- Logical: and, or, not
- Assignment: =, +=, -=, *=, /=
""",

    "what is if else": """Python uses if, elif, and else to perform conditional logic.
Example:
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")
""",

    "what is a loop": """Loops are used to repeat tasks:
- for loop iterates over sequences: 
for i in range(5): 
    print(i)
- while loop runs until a condition is false: 
count = 0
while count < 5:
    print(count)
    count += 1
""",

    "what is a function": """Functions are reusable blocks of code:
def greet(name):
    return f"Hello, {name}"
""",

    "what are lists": """Lists store multiple items in an ordered way:
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple
""",

    "what are dictionaries": """Dictionaries store key-value pairs:
student = {"name": "Shamitha", "age": 21}
print(student["name"])
""",

    "what are classes": """Python supports object-oriented programming:
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Shamitha")
print(p.name)
""",

    "what are modules": """Modules are Python files containing functions and variables. Use import to access them:
import math
print(math.sqrt(16))
"""
}

def get_mock_answer(question):
    question_lower = question.lower()
    for key in mock_answers:
        if key in question_lower:
            return mock_answers[key]
    return "Sorry, I don't know the answer to that question."

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.form.get("question")
    answer = get_mock_answer(user_question)
    return jsonify({"answer": answer})

# -----------------------------
# Run Flask
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)

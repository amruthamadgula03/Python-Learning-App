import streamlit as st

# ------------------------------------
# APP HEADER
# ------------------------------------
st.title("🐍 Python Learning Notes")
st.subheader("Learn Python Concepts with Examples and Quizzes")

st.write("""
Welcome to **Python Learning Notes App** 🎓  
Choose a topic to explore concepts, see examples, and test your understanding with a short quiz.
""")

# ------------------------------------
# TOPIC DATA
# ------------------------------------
topics = {
    "Variables": {
        "info": "Variables are containers for storing data values. They can hold numbers, strings, or any data type.",
        "examples": [
            "x = 10\nname = 'Amrutha'\nprint(x, name)",
            "price = 99.99\nquantity = 5\ntotal = price * quantity\nprint('Total:', total)",
            "is_active = True\nprint('User active:', is_active)"
        ],
        "real_world": "Used for storing user data, configuration settings, or temporary results in programs.",
        "quiz": [
            {
                "q": "Which of the following is a valid variable name?",
                "options": ["1num", "_value", "my-var", "def"],
                "answer": "_value"
            },
            {
                "q": "What data type is the value in `x = 10`?",
                "options": ["string", "integer", "float", "boolean"],
                "answer": "integer"
            },
            {
                "q": "Which symbol is used for assignment in Python?",
                "options": ["=", "==", "->", ":"],
                "answer": "="
            },
            {
                "q": "What will `type(3.14)` return?",
                "options": ["int", "float", "str", "bool"],
                "answer": "float"
            },
            {
                "q": "Variables in Python are:",
                "options": ["Statically typed", "Dynamically typed", "Constant", "Immutable"],
                "answer": "Dynamically typed"
            }
        ]
    },

    "Loops": {
        "info": "Loops are used to repeat a block of code multiple times until a condition is met.",
        "examples": [
            "for i in range(5):\n    print(i)",
            "count = 0\nwhile count < 3:\n    print('Hello')\n    count += 1",
            "for char in 'Python':\n    print(char)"
        ],
        "real_world": "Used for iterating over datasets, processing files, or sending repeated messages.",
        "quiz": [
            {"q": "Which loop is used when the number of iterations is known?", "options": ["while", "for", "do-while", "loop"], "answer": "for"},
            {"q": "What will `range(3)` generate?", "options": ["0,1,2", "1,2,3", "0,1,2,3", "Error"], "answer": "0,1,2"},
            {"q": "Which statement exits a loop?", "options": ["exit", "stop", "break", "quit"], "answer": "break"},
            {"q": "Which statement skips the current iteration?", "options": ["break", "skip", "continue", "pass"], "answer": "continue"},
            {"q": "How many times does `for i in range(5):` loop run?", "options": ["4", "5", "6", "0"], "answer": "5"}
        ]
    },

    "Functions": {
        "info": "Functions are reusable blocks of code that perform specific tasks and can return values.",
        "examples": [
            "def greet():\n    print('Hello!')\ngreet()",
            "def add(a, b):\n    return a + b\nprint(add(3, 5))",
            "def square(x):\n    return x**2\nprint(square(4))"
        ],
        "real_world": "Functions help modularize programs like handling user input, validating data, or computing values.",
        "quiz": [
            {"q": "Which keyword is used to define a function?", "options": ["func", "define", "def", "lambda"], "answer": "def"},
            {"q": "What is returned if no `return` statement is used?", "options": ["0", "None", "False", "Error"], "answer": "None"},
            {"q": "What is a function that calls itself called?", "options": ["Lambda", "Recursive", "Nested", "Inline"], "answer": "Recursive"},
            {"q": "What symbol is used to start a function block?", "options": [":", ";", "{", "("], "answer": ":"},
            {"q": "Functions improve code by making it:", "options": ["longer", "faster", "modular", "unreadable"], "answer": "modular"}
        ]
    },

    "Lists": {
        "info": "Lists are ordered, mutable collections used to store multiple items in one variable.",
        "examples": [
            "fruits = ['apple', 'banana', 'cherry']\nprint(fruits)",
            "numbers = [1, 2, 3]\nnumbers.append(4)\nprint(numbers)",
            "items = ['pen', 'book', 'bag']\nfor i in items:\n    print(i)"
        ],
        "real_world": "Used to manage collections like student records, shopping carts, or data processing.",
        "quiz": [
            {"q": "Lists in Python are:", "options": ["Immutable", "Mutable", "Constant", "Static"], "answer": "Mutable"},
            {"q": "What will `len([1,2,3])` return?", "options": ["2", "3", "1", "Error"], "answer": "3"},
            {"q": "How do you access the first element of a list?", "options": ["list(1)", "list[0]", "list.first()", "list[-1]"], "answer": "list[0]"},
            {"q": "Which method adds an element at the end?", "options": ["add()", "append()", "insert()", "push()"], "answer": "append()"},
            {"q": "Which of the following creates an empty list?", "options": ["()", "{}", "[]", "None"], "answer": "[]"}
        ]
    },

    "Dictionaries": {
        "info": "Dictionaries are unordered collections that store data as key-value pairs.",
        "examples": [
            "student = {'name': 'Amrutha', 'age': 21}\nprint(student['name'])",
            "info = {}\ninfo['city'] = 'Hyderabad'\ninfo['pincode'] = 500072\nprint(info)",
            "for key, value in {'a':1, 'b':2}.items():\n    print(key, value)"
        ],
        "real_world": "Used in APIs, storing user profiles, and managing configuration settings.",
        "quiz": [
            {"q": "How are dictionary elements accessed?", "options": ["By index", "By key", "By position", "By order"], "answer": "By key"},
            {"q": "What does `dict.keys()` return?", "options": ["List of values", "List of keys", "List of items", "Tuple"], "answer": "List of keys"},
            {"q": "Which symbol is used to separate key and value?", "options": ["=", ":", "->", ","], "answer": ":"},
            {"q": "Dictionaries are enclosed within:", "options": ["[]", "()", "{}", "<>"], "answer": "{}"},
            {"q": "What will `len({'a':1,'b':2,'c':3})` return?", "options": ["2", "3", "1", "Error"], "answer": "3"}
        ]
    }
}

# ------------------------------------
# TOPIC SELECTION
# ------------------------------------
selected_topic = st.selectbox("📘 Choose a Python Topic:", list(topics.keys()))
topic_data = topics[selected_topic]

# ------------------------------------
# DISPLAY CONTENT
# ------------------------------------
st.header(selected_topic)
st.markdown(f"**📖 Description:** {topic_data['info']}")
st.markdown("### 💡 Real-world Usage")
st.info(topic_data["real_world"])

st.markdown("### 🧠 Example Codes")
for i, code in enumerate(topic_data["examples"], 1):
    st.code(code, language='python')

# ------------------------------------
# QUIZ SECTION
# ------------------------------------
st.markdown("### 🧩 Quick Quiz")
score = 0

for i, qdata in enumerate(topic_data["quiz"], 1):
    st.write(f"**Q{i}. {qdata['q']}**")
    user_ans = st.radio(f"Choose your answer for Q{i}:", qdata["options"], key=f"q{i}_{selected_topic}")
    if st.button(f"Submit Q{i}", key=f"btn{i}_{selected_topic}"):
        if user_ans == qdata["answer"]:
            st.success("✅ Correct!")
            score += 1
        else:
            st.error(f"❌ Wrong! Correct answer: {qdata['answer']}")

# ------------------------------------
# RATING (simple summary)
# ------------------------------------
if st.button("Show My Rating"):
    st.markdown(f"### 🌟 Your Score: {score} / {len(topic_data['quiz'])}")
    if score == 5:
        st.success("Outstanding! 🌟🌟🌟🌟🌟")
        st.balloons()
    elif score >= 3:
        st.info("Good job! 🌟🌟🌟")
    else:
        st.warning("Needs improvement! 🌟🌟")

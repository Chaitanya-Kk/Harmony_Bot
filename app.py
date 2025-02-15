from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from textblob import TextBlob
import spacy
import json
import os
import numpy as np
import bisect
import threading
import time
from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor
from sklearn.neighbors import NearestNeighbors

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'supersecretkey'
executor = ThreadPoolExecutor(max_workers=5)

# Load NLP model with optimized components for efficiency
nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])

# Load and Sort Knowledge Base
def load_sorted_knowledge_base(file_path='knowledge_base.json'):
    with open(file_path, 'r') as file:
        knowledge_base = json.load(file)
    knowledge_base["questions"].sort(key=lambda q: q["question"])  # Sort alphabetically
    return knowledge_base

knowledge_base = load_sorted_knowledge_base()
knowledge_dict = {q["question"]: q["answer"] for q in knowledge_base["questions"]}

# Global variables for background processing
vectorized_questions = None
nbrs = None
processing_complete = False

# **Background Function: Process Questions in Batches**
def process_questions_in_background(batch_size=50):
    global vectorized_questions, nbrs, processing_complete
    print("🔄 Processing question embeddings in the background...")

    vectors = []
    for i in range(0, len(knowledge_base["questions"]), batch_size):
        batch = [nlp(q["question"]).vector for q in knowledge_base["questions"][i:i+batch_size]]
        vectors.extend(batch)

    vectorized_questions = np.array(vectors)
    nbrs = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(vectorized_questions)
    processing_complete = True  # Mark as completed
    print("✅ Processing complete! Chatbot is fully optimized.")

# **Start processing in a background thread**
processing_thread = threading.Thread(target=process_questions_in_background, daemon=True)
processing_thread.start()

# Normalize input
def normalize_input(user_input):
    return user_input.strip().capitalize()

# Cached sentiment analysis (O(1))
@lru_cache(maxsize=1000)
def get_sentiment_cached(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

# Binary Search for fast question lookup (O(log n))
def binary_search_question(query):
    questions = [q["question"] for q in knowledge_base["questions"]]
    index = bisect.bisect_left(questions, query)
    if index < len(questions) and questions[index] == query:
        return knowledge_base["questions"][index]["answer"]
    return None  # Not found

# Nearest Neighbors for similarity matching (O(log n))
def find_best_match(user_input):
    if not processing_complete:
        return "I'm still learning... Please ask again in a few seconds."

    user_vector = nlp(user_input).vector.reshape(1, -1)
    _, indices = nbrs.kneighbors(user_vector)
    return knowledge_base["questions"][indices[0][0]]["answer"]

# Optimized Chatbot Response
def get_bot_response(user_input):
    normalized_input = normalize_input(user_input)

    # 1. Exact match from dictionary (O(1))
    if normalized_input in knowledge_dict:
        return knowledge_dict[normalized_input]

    # 2. Use binary search if dictionary lookup fails (O(log n))
    response = binary_search_question(normalized_input)
    if response:
        return response

    # 3. If no match, use similarity search (O(log n))
    return find_best_match(normalized_input)

# Home Route
@app.route('/')
def home():
    return render_template('chat.html') if 'username' in session else redirect(url_for('signin'))

# Sign-in and Sign-up
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        action = request.form['action']
        users = load_users()

        if action == "signin":
            for user in users['users']:
                if user['username'] == username and user['password'] == password:
                    session['username'] = username
                    return redirect(url_for('home'))
            return render_template('signin.html', error="Invalid username or password.")

        elif action == "signup":
            if any(user['username'] == username for user in users['users']):
                return render_template('signin.html', error="Username already taken.")
            users['users'].append({"username": username, "password": password})
            save_users(users)
            session['username'] = username
            return redirect(url_for('home'))

    return render_template('signin.html')

@app.route('/guest')
def guest():
    session['username'] = 'Guest'
    return redirect(url_for('home'))

# Sign-out
@app.route('/signout')
def signout():
    session.pop('username', None)
    return redirect(url_for('signin'))

# Multi-threaded Chat API
@app.route('/chat', methods=['POST'])
def chat():
    if 'username' not in session:
        return jsonify({"response": "Please sign in first."})

    data = request.json
    user_input = data.get('message', '')

    if not user_input:
        return jsonify({"response": "Please enter a message."})

    future = executor.submit(get_bot_response, user_input)
    return jsonify({"response": future.result()})

# Real-time Autocomplete API
@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('query', '')
    matches = [q for q in knowledge_dict.keys() if query.lower() in q.lower()]
    return jsonify({"matches": matches})

# Utility functions for user management
def load_users(file_path='users.json'):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_users(users, file_path='users.json'):
    with open(file_path, 'w') as file:
        json.dump(users, file, indent=4)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

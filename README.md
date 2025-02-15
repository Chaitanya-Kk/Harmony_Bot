# Harmony Bot

Harmony Bot is an advanced, ready-to-deploy chatbot solution built using Flask and modern Natural Language Processing (NLP) techniques. It is designed for seamless user interaction, providing intelligent responses in real-time. This project is ideal for developers and organizations seeking an adaptable chatbot framework.

## Key Features

### User Management
- **Sign In/Sign Up**: Secure authentication system for registered users.
- **Guest Mode**: Allows access without registration.
- **Session Handling**: Persistent sessions for enhanced user experience.

### Chat Functionality
- **Real-time Conversations**: Provides quick and accurate responses to user queries.
- **Autocomplete Suggestions**: Dynamically suggests possible queries as users type.
- **Dynamic Response Generation**: Combines predefined answers with context-aware NLP responses.

### Knowledge Base
- **Predefined Data**: Questions and answers are stored in a structured format (`knowledge_base.json`).
- **Optimized Search**: Supports binary search and similarity matching for fast and accurate query resolution.
- **Scalable Updates**: Easily add, modify, or sort questions and answers.

### NLP Integration
- **Text Analysis**: Leverages spaCy for text vectorization and TextBlob for sentiment analysis.
- **Similarity Matching**: Uses machine learning models for context-aware responses.
- **Sentiment Analysis**: Provides insights into user sentiment for tailored responses.

### Performance Optimization
- **Background Processing**: Pre-processes knowledge base embeddings for enhanced performance.
- **Multi-threading**: Handles multiple chat sessions efficiently.
- **Caching**: Implements caching for frequently accessed data.

## Libraries Used

### 1. Flask
- **Purpose**: Provides the web framework for the chatbot, enabling route handling and user interactions.
- **Why Used**: Lightweight, easy to set up, and well-suited for APIs and web applications.
- **Time Complexity**: Route handling and rendering templates operate in O(1) for typical cases.

### 2. spaCy
- **Purpose**: Performs text vectorization for understanding and processing user queries.
- **Why Used**: High performance for NLP tasks, including text similarity and tokenization.
- **Time Complexity**: Tokenization and vectorization are O(n), where n is the length of the input text.

### 3. TextBlob
- **Purpose**: Conducts sentiment analysis on user inputs.
- **Why Used**: Simple API for extracting polarity and subjectivity of text.
- **Time Complexity**: Sentiment analysis typically operates in O(n).

### 4. NumPy
- **Purpose**: Handles numerical operations and stores vectorized data efficiently.
- **Why Used**: Offers optimized mathematical functions and data structures.
- **Time Complexity**: Vector operations such as dot product are O(n).

### 5. scikit-learn
- **Purpose**: Provides nearest neighbor algorithms for similarity matching.
- **Why Used**: Efficient implementation of machine learning algorithms like NearestNeighbors.
- **Time Complexity**: k-NN search complexity is O(log(n)) for preprocessed data.

### 6. threading
- **Purpose**: Allows background processing of embeddings and simultaneous user interactions.
- **Why Used**: Ensures the application remains responsive during computational tasks.
- **Time Complexity**: Dependent on the background task; typically O(n) for batch operations.

## Deployment Ready

Harmony Bot is designed for deployment on cloud platforms like AWS, Azure, or Heroku. It includes configurations and modular scripts for a smooth deployment experience.

### Deployment Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/harmony-bot.git
   cd harmony-bot
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the Environment**:
   - Set up your Flask environment.
   - Add environment variables for deployment (e.g., `SECRET_KEY`, `FLASK_ENV`).

4. **Run Locally**:
   ```bash
   python app.py
   ```
   Access the app locally at `http://127.0.0.1:5000/`.

5. **Deploy to Production**:
   - Use Docker for containerization.
   - Deploy on platforms like Heroku, AWS Elastic Beanstalk, or Azure App Service.

6. **Monitoring and Scaling**:
   - Integrate logging and monitoring tools (e.g., ELK stack, Prometheus).
   - Configure autoscaling based on traffic demands.

## Project Structure

```plaintext
harmony_bot/
├── app.py                    # Main application logic
├── conversation.json         # Chat history (if enabled)
├── knowledge_base.json       # Question-answer knowledge base
├── requirements.txt          # Project dependencies
├── sort_knowledge_base.py    # Utility script to sort the knowledge base
├── users.json                # User authentication data
├── static/                   # Static assets (CSS, JS)
│   ├── chat-styles.css       # Styles for chat interface
│   ├── script.js             # JavaScript for client-side interactions
│   ├── signin.js             # JavaScript for sign-in functionality
│   └── styles.css            # General styles
├── templates/                # HTML templates
│   ├── chat.html             # Chat interface
│   └── signin.html           # Sign-in page
└── README.md                 # Project documentation
```

## Configuration

### Environment Variables
Set up the following environment variables for deployment:
- `SECRET_KEY`: Secret key for Flask sessions.
- `FLASK_ENV`: Set to `production` for live deployment.
- `PORT`: Specify the port for the Flask app (default is 5000).

### Knowledge Base
To customize the knowledge base, edit the `knowledge_base.json` file. Run `sort_knowledge_base.py` to optimize it for performance:
```bash
python sort_knowledge_base.py
```

## Scalability
Harmony Bot is designed to scale with your needs:
- **Add New Features**: Enhance functionality with minimal changes to the existing architecture.
- **Distributed Deployment**: Deploy in distributed environments using Docker and Kubernetes.
- **Cloud-based NLP**: Leverage advanced NLP services from AWS, Google Cloud, or Azure.

## Future Enhancements
- **Multi-language Support**: Expand the bot to handle multiple languages for global accessibility.
- **Voice Integration**: Add support for voice-based queries to make the bot more interactive.
- **Analytics Dashboard**: Build a dashboard to track user interactions and analyze chatbot performance.
- **AI-based Learning**: Enable the bot to learn from interactions and improve its responses over time.

## Contributing
We welcome contributions to improve Harmony Bot! Follow these steps:
1. Fork the repository.
2. Create a feature branch (`feature-name`).
3. Commit and push your changes.
4. Submit a pull request for review.

## License
This project is licensed under the [MIT License](LICENSE).

## Support
For questions or issues, please contact `chaitanya.kamble24@vit.edu`. We’re here to help!

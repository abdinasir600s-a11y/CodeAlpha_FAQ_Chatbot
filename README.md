# CodeAlpha FAQ Chatbot

## Internship Domain

Artificial Intelligence

## Task Name

Task 2: Chatbot for FAQs

## Project Overview

CodeAlpha FAQ Chatbot is a simple university admission FAQ chatbot built with Python and Streamlit. It allows users to ask admission-related questions and returns the most relevant answer from a stored FAQ dataset.

## Project Objective

The objective of this project is to create a beginner-friendly FAQ matching chatbot that uses basic Natural Language Processing techniques to compare a user's question with stored FAQ questions and return the best matching answer.

## Features

- User can ask university admission related questions.
- FAQ questions are preprocessed before matching.
- TF-IDF vectorization is used to represent questions.
- Cosine similarity is used to find the closest FAQ.
- The chatbot displays the answer, matched FAQ question, category, and confidence score.
- Low-confidence questions return a friendly fallback response.
- Chat history works during the current Streamlit session.
- Clear chat history button is available.
- Sample questions are visible in the sidebar.

## NLP Approach

This project does not use a generative AI model. It uses a simple FAQ matching approach:

1. Store FAQ questions and answers inside the project.
2. Clean and preprocess the user question and FAQ questions.
3. Convert questions into numerical vectors using TF-IDF.
4. Compare the user question with FAQ questions using cosine similarity.
5. Return the answer from the most similar FAQ if the confidence score is high enough.
6. Return a fallback message if the confidence score is too low.

## Technologies Used

- Python
- Streamlit
- scikit-learn
- pandas

## Folder Structure

```text
CodeAlpha_FAQ_Chatbot/
├── app.py
├── frontend.py
├── chatbot.py
├── faq_data.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
    └── .gitkeep
```

## Installation Steps

1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Create and activate a virtual environment.

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

4. Install the required packages.

```bash
pip install -r requirements.txt
```

## How to Run the App

Run this command from the project folder:

```bash
streamlit run app.py
```

## How to Use the Chatbot

1. Open the Streamlit app in your browser.
2. Type a university admission related question.
3. Click the **Ask Chatbot** button.
4. View the chatbot answer, matched FAQ question, category, and confidence score.
5. Use the sidebar button to clear chat history when needed.

## Screenshots

Add application screenshots inside the `screenshots/` folder.

Example:

```text
screenshots/homepage.png
screenshots/chatbot_response.png
```

## Demo Video

Add your demo video link here:

```text
Demo Video: Your LinkedIn or Google Drive video link
```

## GitHub Repository

Add your GitHub repository link here:

```text
GitHub Repository: https://github.com/abdinasir600s-a11y/CodeAlpha_FAQ_Chatbot
```

## Author

**Name:** Abdinasir Osman Warsame  
**Role:** CodeAlpha Artificial Intelligence Intern  
**GitHub:** [abdinasir600s-a11y](https://github.com/abdinasir600s-a11y)

## CodeAlpha Acknowledgement

This project was created as part of the CodeAlpha Artificial Intelligence Internship program.

## Disclaimer

This is a FAQ matching chatbot, not a generative AI chatbot. It does not use OpenAI API, Gemini API, or any paid AI API. The chatbot only matches user questions with stored university admission FAQs and returns the most relevant saved answer.

# CodeAlpha FAQ Chatbot

## Internship Domain

Artificial Intelligence

## Task Name

Task 2: Chatbot for FAQs

## Project Overview

CodeAlpha FAQ Chatbot is a simple university admission FAQ chatbot built with
Python and Streamlit. Users can ask admission-related questions, and the app
returns the most relevant saved FAQ answer.

This project is designed for a beginner-friendly CodeAlpha internship
submission. It does not use a paid AI API or a generative AI model.

## Project Objective

The objective of this project is to create a simple FAQ matching chatbot that:

- Stores a small FAQ dataset inside the project.
- Cleans and preprocesses user questions.
- Uses TF-IDF vectorization.
- Uses cosine similarity to find the closest FAQ.
- Returns a fallback message when no confident FAQ match is found.

## Features

- User can ask university admission questions.
- Chatbot preprocesses the question before matching.
- TF-IDF vectorization converts questions into numerical form.
- Cosine similarity finds the closest stored FAQ.
- Response displays the chatbot answer.
- Response displays the matched FAQ question for confident matches.
- Response displays category for confident matches.
- Response displays confidence score.
- Low-confidence questions return a friendly fallback response.
- Chat history works during the current Streamlit session.
- Clear Chat History button is available.
- Sample questions are visible in the sidebar.
- Empty input validation prevents crashes.

## NLP Approach

This is a FAQ matching chatbot, not a generative AI chatbot.

The NLP workflow is:

1. Store FAQ questions, answers, and categories in `faq_data.py`.
2. Clean user questions and FAQ questions with `clean_text()`.
3. Convert cleaned questions into TF-IDF vectors.
4. Compare the user question with stored FAQ questions using cosine similarity.
5. Return the best answer if the confidence score is high enough.
6. Return a fallback response if the confidence score is too low.

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
├── .streamlit/
│   └── config.toml
└── screenshots/
    ├── home_page.png
    ├── chatbot_response.png
    └── no_match_response.png
```

## Installation Steps

1. Clone the repository.

```bash
git clone https://github.com/abdinasir600s-a11y/CodeAlpha_FAQ_Chatbot.git
```

2. Open the project folder.

```bash
cd CodeAlpha_FAQ_Chatbot
```

3. Create a virtual environment.

```bash
python -m venv venv
```

4. Activate the virtual environment.

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

5. Install the required packages.

```bash
python -m pip install -r requirements.txt
```

## How to Run the App

Run this command from the project folder:

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## How to Use the Chatbot

1. Type a university admission related question in the input box.
2. Click the **Ask Chatbot** button.
3. Read the chatbot answer in the Chat History section.
4. Review the matched FAQ, category, confidence score, and status.
5. Use the sidebar button to clear chat history when needed.

## Screenshots

### Home Page

![Home Page](screenshots/home_page.png)

### Confident FAQ Response

![Chatbot Response](screenshots/chatbot_response.png)

### Fallback Response

![No Match Response](screenshots/no_match_response.png)

## Demo Video

Add your demo video link here:

```text
Demo Video: Your LinkedIn or Google Drive demo video link
```

## GitHub Repository

```text
https://github.com/abdinasir600s-a11y/CodeAlpha_FAQ_Chatbot
```

## Author

**Name:** Abdinasir Osman Warsame  
**Role:** CodeAlpha Artificial Intelligence Intern  
**GitHub:** [abdinasir600s-a11y](https://github.com/abdinasir600s-a11y)

## CodeAlpha Acknowledgement

This project was created as part of the CodeAlpha Artificial Intelligence
Internship program.

## Disclaimer

This is a FAQ matching chatbot, not a generative AI chatbot. It does not use
OpenAI API, Gemini API, or any paid AI API. The chatbot only compares a user's
question with stored university admission FAQs and returns the most relevant
saved answer.

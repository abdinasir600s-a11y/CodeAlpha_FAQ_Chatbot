import re

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faq_data import FAQ_DATA


CONFIDENCE_THRESHOLD = 0.30
FALLBACK_RESPONSE = (
    "I could not find a confident answer. Please try asking your question in a different way."
)


def clean_text(text):
    """Prepare text for FAQ matching."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


faq_df = pd.DataFrame(FAQ_DATA)
faq_df["clean_question"] = faq_df["question"].apply(clean_text)

vectorizer = TfidfVectorizer(stop_words="english")
faq_vectors = vectorizer.fit_transform(faq_df["clean_question"])


def get_bot_response(user_question):
    """Return the best FAQ answer for a user's question."""
    cleaned_question = clean_text(user_question)

    if not cleaned_question:
        return {
            "answer": FALLBACK_RESPONSE,
            "matched_question": "No confident match",
            "category": "Unknown",
            "confidence_score": 0.0,
            "is_confident": False,
        }

    user_vector = vectorizer.transform([cleaned_question])
    similarity_scores = cosine_similarity(user_vector, faq_vectors).flatten()

    best_match_index = similarity_scores.argmax()
    best_score = float(similarity_scores[best_match_index])
    is_confident = best_score >= CONFIDENCE_THRESHOLD

    if not is_confident:
        return {
            "answer": FALLBACK_RESPONSE,
            "matched_question": faq_df.iloc[best_match_index]["question"],
            "category": faq_df.iloc[best_match_index]["category"],
            "confidence_score": round(best_score, 2),
            "is_confident": False,
        }

    matched_faq = faq_df.iloc[best_match_index]

    return {
        "answer": matched_faq["answer"],
        "matched_question": matched_faq["question"],
        "category": matched_faq["category"],
        "confidence_score": round(best_score, 2),
        "is_confident": True,
    }

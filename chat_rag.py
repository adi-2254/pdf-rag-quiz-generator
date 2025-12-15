from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
import json


load_dotenv()

client= OpenAI()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding = embeddings,
    url = "http://localhost:6334",
    collection_name= "quiz_taker"
)

user_query = input("Enter the topics u want to practice for...  ")

search_results = vector_db.similarity_search(query=user_query)





SYSTEM_PROMPT = """
You are a strict Quiz Master. 
Your task is to generate a quiz based strictly on the provided CONTEXT below.
User will give u the topic.
Do not use outside knowledge. If the answer is not in the context, do not ask the question.

--- CONTEXT START ---
{context}
--- CONTEXT END ---

Instructions:
1. Create exactly 5 multiple-choice questions based on the context above.
2. For each question, provide 4 options labeled A, B, C, and D.
3. Identify the correct option letter.
4. Output strictly valid JSON.

JSON Structure:
{{
"quiz": [
    {{
        "question_number": "1",
        "question": "The question text...",
        "options": {{
        "A": "Option text...",
        "B": "Option text...",
        "C": "Option text...",
        "D": "Option text..."
    }},
    "correct_option": "A" 
    }}
]
}}
"""


response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query},
    ],
    response_format={"type": "json_object"}
)

data = json.loads(response.choices[0].message.content)

quiz= data.get("quiz")

print(f"🤖 Ready for the quiz..... ")

score = 0

for i, q in enumerate(quiz, 1):
    print(f"\nQuestion {i}: {q['question']}")
    
    for key, value in q['options'].items():
        print(f"{key}) {value}")
    

    user_choice = input("Your Answer: ").strip().upper()
    
    if user_choice == q['correct_option']:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['correct_option']}")

print(f"\nFinal Score: {score}/{len(quiz)}")


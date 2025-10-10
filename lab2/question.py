import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from util import call_ollama

def answer_question(context, question):
    """
    Answer questions based on provided context.
    
    Args:
        context: Background information
        question: Question to answer
    """
    
    # TODO: Build your prompt
    # Make it clear to only use the context
    # Handle cases where answer isn't available
    
    prompt = f"""Answer questons only with the information provided in the context.
                Answer 'I don't know' if the information needed is not in the context. 
    
Context: {context}

Question: {question}

Answer:"""
    
    response = call_ollama(
        prompt, 
        temperature=0.1, 
        num_predict=100
    )
    return response

# Test context
context = """
Python is a high-level programming language created by Guido van Rossum 
in 1991. It emphasizes code readability and uses significant indentation. 
Python supports multiple programming paradigms including procedural, 
object-oriented, and functional programming. It is widely used in web 
development, data science, and automation.
"""

# Test questions
questions = [
    "Who created Python?",
    "What year was Python created?",
    "What is Python used for?",
    "What is Python's execution speed?"  # Not in context!
]

if __name__ == "__main__":
    for q in questions:
        answer = answer_question(context, q)
        print(f"\nQ: {q}")
        print(f"A: {answer}")
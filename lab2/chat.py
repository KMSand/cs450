import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from util import chat_ollama

def run_conversation():
    """Demonstrate multi-turn conversation."""
    
    messages = [
        {
            'role': 'system',
            'content': 'You are a helpful Python programming tutor.'
        },
        {
            'role': 'user',
            'content': 'What is a list comprehension?'
        }
    ]
    
    # First response
    response = chat_ollama(messages, temperature=0.3)
    print("Assistant:", response)
    
    # Add to conversation
    messages.append({
        'role': 'assistant',
        'content': response
    })
    
    messages.append({
        'role': 'user',
        'content': 'Can you show me an example?'
    })
    
    # Second response
    response = chat_ollama(messages, temperature=0.3)
    print("\nAssistant:", response)

if __name__ == "__main__":
    run_conversation()
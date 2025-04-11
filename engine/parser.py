# engine/parser.py

import re

def parse_input(user_input):
    """
    Naive parser that tries to extract Java programming task from user input.
    Later we’ll make it smarter.
    """
    user_input = user_input.lower()
    entities = []

    # Match common Java topics
    if "sort" in user_input:
        if "bubble" in user_input:
            return {
                "intent": "bubble_sort",
                "task": "sort an array",
                "method": "bubble sort",
                "entities": ["array", "sort", "bubble sort"]
            }
        elif "quick" in user_input:
            return {
                "intent": "quick_sort",
                "task": "sort an array",
                "method": "quick sort",
                "entities": ["array", "sort", "quick sort"]
            }
        else:
            return {
                "intent": "generic_sort",
                "task": "sort an array",
                "method": "unspecified",
                "entities": ["array", "sort"]
            }

    elif "thread" in user_input or "multithread" in user_input:
        return {
            "intent": "threading",
            "task": "create a thread",
            "method": "Thread class",
            "entities": ["thread", "Thread class"]
        }

    elif "file" in user_input and "read" in user_input:
        return {
            "intent": "file_reading",
            "task": "read from a file",
            "method": "BufferedReader",
            "entities": ["file", "read", "BufferedReader"]
        }

    elif "inheritance" in user_input or "extends" in user_input:
        return {
            "intent": "inheritance",
            "task": "demonstrate inheritance",
            "method": "inheritance",
            "entities": ["class", "inheritance", "extends"]
        }

    elif "simple gui" in user_input or "swing" in user_input or "window" in user_input:
        return {
            "intent": "simple_gui",
            "task": "build a simple GUI",
            "method": "Swing",
            "entities": ["gui", "swing", "window"]
        }

    # Default fallback
    return {
        "intent": "unknown",
        "task": user_input,
        "method": "unsure",
        "entities": []
    }

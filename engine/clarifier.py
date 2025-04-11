# engine/clarifier.py

def needs_more_info(parsed_data):
    """
    Checks if the parsed intent is too vague to generate code.
    """
    if parsed_data["intent"] == "unknown" or parsed_data["method"] == "unsure":
        return True
    return False


def ask_questions(parsed_data):
    """
    Ask clarifying questions based on the missing parts.
    """
    questions = []

    if parsed_data["intent"] == "unknown":
        questions.append("Can you describe what you want the Java program to do?")
    
    if parsed_data["method"] == "unsure":
        questions.append("Do you have a specific algorithm or method in mind?")

    if not parsed_data["entities"]:
        questions.append("What kind of input/output should the program handle?")

    return questions

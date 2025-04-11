# java-ai-coder/main.py

from engine.parser import parse_input
from engine.responder import generate_java_code
from engine.clarifier import needs_more_info, ask_questions
from engine.file_generator import save_project_structure
from engine.memory import SessionMemory

context = {
    "last_intent": None,
    "history": [],
}

def chat(user_input):
    parsed = parse_input(user_input)

    if parsed["intent"] == "unknown" and context["last_intent"]:
        parsed["intent"] = context["last_intent"]

    context["last_intent"] = parsed["intent"]
    context["history"].append(user_input)

    code, explanation, files = generate_java_code(parsed)
    return code, explanation, files

def main():
    memory = SessionMemory()
    print("👋 Welcome to Java AI Coder!\nAsk me anything related to Java programming.")
    while True:
        user_input = input("\n🧠 You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        parsed_data = parse_input(user_input)
        print("🧩 Parsed data:", parsed_data)
        memory.add_entry(user_input, parsed_data)

        if needs_more_info(parsed_data):
            questions = ask_questions(parsed_data)
            print("\n🤔 I need more info:")
            for q in questions:
                print(" - " + q)
            continue

        java_code, explanation, files = generate_java_code(parsed_data)
        save_project_structure(files)

        print("\n✅ Here’s your Java code:\n")
        print(java_code)
        print("\n📖 Explanation:\n")
        print(explanation)

if __name__ == "__main__":
    main()

"""
# java-ai-coder/main.py

from engine.parser import parse_input
from engine.responder import generate_java_code
from engine.clarifier import needs_more_info, ask_questions
from engine.file_generator import save_project_structure
from engine.memory import SessionMemory

def main():
    memory = SessionMemory()
    print("👋 Welcome to Java AI Coder!\nAsk me anything related to Java programming.")
    
    last_parsed_data = None  # 🧠 store last parsed input

    while True:
        user_input = input("\n🧠 You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        # 🧠 pass previous context into parser
        parsed_data = parse_input(user_input, context=last_parsed_data)

        # 🧠 fix unknown intent if continuing a GUI conversation
        if parsed_data["intent"] == "unknown" and last_parsed_data:
            if last_parsed_data["intent"] in ["simple_gui", "gui_with_button", "gui_with_input"]:
                parsed_data["intent"] = "update_gui_add_textfield"

        print("🧩 Parsed data:", parsed_data)
        memory.add_entry(user_input, parsed_data)

        # 🤔 Ask follow-up questions if needed
        if needs_more_info(parsed_data):
            questions = ask_questions(parsed_data)
            print("\n🤔 I need more info:")
            for q in questions:
                print(" - " + q)
            continue

        # ✅ Generate Java code
        java_code, explanation, files = generate_java_code(parsed_data)
        save_project_structure(files)

        print("\n✅ Here’s your Java code:\n")
        print(java_code)
        print("\n📖 Explanation:\n")
        print(explanation)

        # 🧠 Save last parsed data for next turn
        last_parsed_data = parsed_data

if __name__ == "__main__":
    main()
"""
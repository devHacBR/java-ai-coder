# java-ai-coder/main.py

"""
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

# java-ai-coder/main.py

from engine.parser import parse_input
from engine.responder import generate_java_code
from engine.clarifier import needs_more_info, ask_questions
from engine.file_generator import save_project_structure
from engine.memory import SessionMemory

context = {
    "last_intent": None,
    "history": [],
    "last_parsed_data": None,  # 🆕 Added for memory
    "gui_components": []
}

def chat(user_input):
    parsed = parse_input(user_input, context=context.get("last_parsed_data"))

    # If intent is unknown, fallback to previous
    if parsed["intent"] == "unknown" and context["last_intent"]:
        parsed["intent"] = context["last_intent"]

    # Save memory context
    context["last_intent"] = parsed["intent"]
    context["last_parsed_data"] = parsed
    context["history"].append(user_input)

    # 🔁 Generate and return Java code
    code, explanation, files = generate_java_code(parsed, context.get("gui_components"))
    return code, explanation, files

def main():
    memory = SessionMemory()
    print("👋 Welcome to Java AI Coder!\nAsk me anything related to Java programming.")
    
    while True:
        user_input = input("\n🧠 You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        # 🔍 Parse with memory-aware context
        parsed_data = parse_input(user_input, context=context.get("last_parsed_data"))

        # 🧠 Add smart GUI follow-up context (new logic)
        if (
            context["last_intent"] == "simple_gui"
            and "add" in user_input.lower()
            and any(x in user_input.lower() for x in ["text field", "textfield", "label", "checkbox", "submit"])
        ):
            parsed_data["intent"] = "add_gui_component"

            # Identify component
            if "text field" in user_input.lower() or "textfield" in user_input.lower():
                parsed_data["component"] = "text_field"
            elif "label" in user_input.lower():
                parsed_data["component"] = "label"
            elif "checkbox" in user_input.lower():
                parsed_data["component"] = "checkbox"
            elif "submit" in user_input.lower():
                parsed_data["component"] = "textfield_button"

        print("🧩 Parsed data:", parsed_data)

        # 💾 Save in memory
        memory.add_entry(user_input, parsed_data)

        # ❓ Ask for clarification if needed
        if needs_more_info(parsed_data):
            questions = ask_questions(parsed_data)
            print("\n🤔 I need more info:")
            for q in questions:
                print(" - " + q)
            continue

        # 🧠 Fallback to last known intent if needed
        if parsed_data["intent"] == "unknown" and context["last_intent"]:
            parsed_data["intent"] = context["last_intent"]

        # 🧠 Update context
        context["last_intent"] = parsed_data["intent"]
        context["last_parsed_data"] = parsed_data
        context["history"].append(user_input)

        # ⚙️ Generate and save code
        java_code, explanation, files = generate_java_code(parsed_data, context.get("gui_components"))
        # 🧠 Update GUI memory if it's a GUI-related response
        if parsed_data["intent"] in ["simple_gui", "add_gui_component"]:
            context["gui_components"] = parsed_data.get("gui_components", context["gui_components"])

        save_project_structure(files)

        print("\n✅ Here’s your Java code:\n")
        print(java_code)
        print("\n📖 Explanation:\n")
        print(explanation)

if __name__ == "__main__":
    main()

# java-ai-coder/main.py

from engine.parser import parse_input
from engine.responder import generate_java_code
from engine.clarifier import needs_more_info, ask_questions
from engine.file_generator import save_project_structure
from engine.memory import SessionMemory

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

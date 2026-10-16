
import json
from pathlib import Path

DATA_FILE = Path("learning_data.json")


def load_topics():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            print("Could not read saved data. Starting fresh.")
    return []


def save_topics(topics):
    DATA_FILE.write_text(
        json.dumps(topics, indent=4),
        encoding="utf-8"
    )


def main():
    print("=" * 40)
    print("       PYTHON LEARNING TRACKER")
    print("=" * 40)

    name = input("Enter your name: ").strip() or "Learner"
    topics = load_topics()

    print(f"\nWelcome back, {name}!")
    print(f"Previously learned topics: {len(topics)}")

    while True:
        print("\n1. Add a topic")
        print("2. View learned topics")
        print("3. Remove a topic")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            topic = input("Enter the topic you learned: ").strip()

            if topic:
                topics.append(topic)
                save_topics(topics)
                print(f"Saved: {topic}")
            else:
                print("Topic cannot be empty.")

        elif choice == "2":
            if topics:
                print("\nTopics learned:")
                for number, topic in enumerate(topics, start=1):
                    print(f"{number}. {topic}")
                print(f"Total topics learned: {len(topics)}")
            else:
                print("No topics recorded yet.")

        elif choice == "3":
            if not topics:
                print("There are no topics to remove.")
                continue

            for number, topic in enumerate(topics, start=1):
                print(f"{number}. {topic}")

            try:
                number = int(input("Enter topic number to remove: "))
                if 1 <= number <= len(topics):
                    removed = topics.pop(number - 1)
                    save_topics(topics)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid topic number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Progress saved. Keep learning!")
            break

        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

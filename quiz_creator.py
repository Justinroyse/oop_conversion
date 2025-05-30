# Initialize class to encapsulate the whole program
# Initialize Question class to modularize questions

class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def format_question(self):
        formatted = f"Question: {self.question_text}\n"
        formatted += f"a) {self.options['a']}\n"
        formatted += f"b) {self.options['b']}\n"
        formatted += f"c) {self.options['c']}\n"
        formatted += f"d) {self.options['d']}\n"
        formatted += f"Correct Answer: {self.correct_answer}\n"
        formatted += "-" * 30 + "\n"
        return formatted


class Quiz:
    def __init__(self):
        self.questions = []
        self.quiz_started = False

    def main_menu(self):
        print("\n********** Welcome to Quiz Creator! **********")
        if not self.quiz_started:
            print("1. Create Quiz")
        else:
            print("1. Create New Question")
        print("2. Exit and save to file")
        print("**********************************************")

    def create_question(self):
        print("\n--- Creating a New Question ---")
        question_text = input("\nEnter your quiz question:\n> ")

        print("\nNow enter the 4 options:")
        options = {
            'a': input("a) "),
            'b': input("b) "),
            'c': input("c) "),
            'd': input("d) ")
        }

        while True:
            correct_answer = input("\nEnter the correct answer (a, b, c, d): ").lower()
            if correct_answer in options:
                break
            else:
                print("Invalid choice. Please enter a, b, c, or d.")

        new_question = Question(question_text, options, correct_answer)
        self.questions.append(new_question)
        self.quiz_started = True

    def save_to_file(self, filename="quiz_questions.txt"):
        with open(filename, "w") as file:
            for question in self.questions:
                file.write(question.format_question())
        print(f"\n--- All questions saved to ({filename}) ---")
        print("Exiting program... Goodbye!")

    def run(self):
        while True:
            self.main_menu()
            try:
                choice = int(input("\nChoice (1 or 2): "))
            except ValueError:
                print("Please enter a valid number (1 or 2).")
                continue

            if choice == 1:
                self.create_question()
            elif choice == 2:
                self.save_to_file()
                break
            else:
                print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    quiz_creator = Quiz()
    quiz_creator.run()

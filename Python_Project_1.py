# Trivia Game 
# break down of the problem (paln)
# we need list of Questions
# we need their ans
# randomly give question
# check the user ans and check if its correct
# track their score
# tell user final score

import random
import tkinter as tk

questions = {
    "What is the largest planet in our solar system?": "jupiter",
    "Which country invented pizza?": "italy",
    "How many bones are in the adult human body?": "206",
    "What is the fastest land animal in the world?": "cheetah",
    "Who wrote the play 'Romeo and Juliet'?": "william shakespeare",
    "What is the smallest prime number?": "2",
    "Which ocean is the deepest?": "pacific ocean",
    "What year did the first iPhone release?": "2007",
    "How many players are there in a cricket team?": "11",
    "Which country is known as the Land of the Rising Sun?": "japan",
    "What is the largest mammal on Earth?": "blue whale",
    "Who painted the Mona Lisa?": "leonardo da vinci",
    "Which gas do plants absorb from the air?": "carbon dioxide",
    "How many days are there in a leap year?": "366",
    "Which planet is known as the Red Planet?": "mars",
    "What is the capital city of Australia?": "canberra",
    "What is the hardest natural substance on Earth?": "diamond",
    "Who was the first person to step on the Moon?": "neil armstrong",
    "Which Greek god is known as the messenger of the gods?": "hermes",
    "What language has the most native speakers worldwide?": "Chinese",
}
question_list = list(questions.keys())
total_questions = 5
selected_questions = random.sample(question_list, total_questions)

current_index = 0
score = 0

root = tk.Tk()
root.title("Trivia Game")
root.geometry("500x400")

question_label = tk.Label(root, text="", font=("Calibri", 16), wraplength=450)
question_label.pack(pady=20)

answer_entry = tk.Entry(root, font=("Arial", 14))
answer_entry.pack(pady=10)

feedback_label = tk.Label(root, text="", font=("Arial", 14))
feedback_label.pack(pady=5)

score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack(pady=5)

def show_question():
    question_label.config(
        text=f"{current_index + 1}. {selected_questions[current_index]}"
    )
    answer_entry.delete(0, tk.END)
    feedback_label.config(text="")

def submit_answer():
    global current_index, score

    user_ans = answer_entry.get().lower().strip()
    correct_ans = questions[selected_questions[current_index]]

    if user_ans == correct_ans:
        feedback_label.config(text="Correct!! ✅")
        score += 1
    else:
        feedback_label.config(
            text=f"Wrong ❌ Correct answer: {correct_ans}"
        )

    score_label.config(text=f"Score: {score}")

    current_index += 1

    if current_index < total_questions:
        root.after(1000, show_question)  # auto-next after 1.2 sec
    else:
        root.after(1000, end_game)

def end_game():
    question_label.config(
        text=f"Game Over 🎉\nFinal Score: {score}/{total_questions}"
    )
    answer_entry.delete(0, tk.END) 
    answer_entry.config(state="disabled")
    submit_btn.config(state="disabled")

submit_btn = tk.Button(root, text="Submit", command=submit_answer)
submit_btn.pack(pady=10)

show_question()
root.mainloop()


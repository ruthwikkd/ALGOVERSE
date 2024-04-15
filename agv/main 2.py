import mysql.connector
import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Quiz")
        
        self.question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=600)
        self.question_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        self.option_vars = []
        self.option_radios = []

        for i in range(4):
            var = tk.StringVar()
            self.option_vars.append(var)
            radio = tk.Radiobutton(root, text="", font=("Arial", 12), variable=var, value=str(i),
                                   command=self.on_radio_select)
            radio.grid(row=i+1, column=0, padx=20, pady=5, sticky="w")
            self.option_radios.append(radio)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.grid(row=5, column=0, pady=10)

        self.load_questions()

    def load_questions(self):
        try:
            # Connect to MySQL database
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Nani200508#11",
                database="SortingQuizDB"
            )

            cursor = db_connection.cursor()

            # Fetch questions from the database
            cursor.execute("SELECT * FROM SortingMCQs")
            self.questions = cursor.fetchall()

            self.display_question()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to fetch questions from database: {err}")

        finally:
            if db_connection.is_connected():
                cursor.close()
                db_connection.close()

    def display_question(self):
        question = self.questions[self.question_index]
        self.question_label.config(text=question[1])

        options = [question[2], question[3], question[4], question[5]]
        for i in range(4):
            self.option_radios[i].config(text=options[i], background="SystemButtonFace")
            self.option_vars[i].set("")

    def on_radio_select(self):
     for i, var in enumerate(self.option_vars):
        if var.get() == str(i):
            self.option_radios[i].config(bg="lightblue")
        else:
            self.option_radios[i].config(bg="SystemButtonFace")

    def next_question(self):
        selected_option = None
        for i, var in enumerate(self.option_vars):
            if var.get() == "1":
                selected_option = i
                break

        if selected_option is not None and self.option_vars[selected_option].get() == self.questions[self.question_index][6]:
            self.score += 1

        self.question_index += 1
        if self.question_index < len(self.questions):
            self.display_question()
        else:
            messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(self.questions)}")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

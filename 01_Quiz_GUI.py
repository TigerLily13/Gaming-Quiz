from tkinter import *
import random


class Quiz:
    def __init__(self, parent):

        # Formatting Variables:
        background_colour = "#A4C2F4"
        button_colour = "#CFE2F3"
        answer = ()
        answers = ["answer 1", "answer 2", "answer 3"]

        # Quiz Main GUI
        self.quiz_frame = Frame(width=500, height=600, bg=background_colour, pady=10)
        self.quiz_frame.grid()

        # Heading Label
        self.quiz_label = Label(self.quiz_frame, text="Gaming Quiz",
                                font=("Arial", "16", "bold"),
                                padx=10, pady=10,
                                bg=background_colour)
        self.quiz_label.grid(row=0)

        # Question Text
        self.question_label = Label(self.quiz_frame, text="[Insert Question]",
                                    font=("Arial", "12"), bg=background_colour, padx=10, pady=10)
        self.question_label.grid(row=1)

        # Answer Box
        self.answer_box = OptionMenu(self.quiz_frame, answer, "Pick an Answer", *answers)
        self.answer_box.grid(row=2, pady=5, padx=10)

        self.answer_box.config(width=20)

        # Submit Button
        self.submit_button = Button(self.quiz_frame, text="Submit", font=("Arial", "14"), bg=button_colour)
        self.submit_button.grid(row=3)

        # Frame for the help and answer history buttons
        self.help_history_frame = Frame(self.quiz_frame, width=600, height=600, bg=background_colour, pady=10)
        self.help_history_frame.grid(row=4)

        # Help Button
        self.help_button = Button(self.help_history_frame,
                                  text="Help",
                                  font=("Arial", "14"), bg=button_colour)
        self.help_button.grid(row=0)

        # History Button
        self.history_button = Button(self.help_history_frame,
                                     text="History",
                                     font=("Arial", "14"), bg=button_colour)
        self.history_button.grid(row=0, column=1)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Quiz(root)
    root.mainloop()

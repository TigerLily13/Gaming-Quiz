from tkinter import *
from functools import partial
import random


class Quiz:
    def __init__(self, parent):

        # Formatting Variables:
        background_colour = "#A4C2F4"
        button_colour = "#CFE2F3"
        answer = StringVar()
        answers = ["A Car Racing Game", "A Popular Game", "A Game made by a Small Company",
                   "A Game made by a Large Company"]
        submit_state = "Submit"
        question_list = ["What is an Indy Game?", "Hollow Knight was made by what team?",
                         "When was Undertale released?"]

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
        self.question_label = Label(self.quiz_frame, text=question_list[0],
                                    font=("Arial", "12"), bg=background_colour, padx=10, pady=10)
        self.question_label.grid(row=1)

        # Answer Box
        self.answer_box = OptionMenu(self.quiz_frame, answer, *answers)
        self.answer_box.grid(row=2, pady=5, padx=10)

        self.answer_box.config(width=30)

        # Submit Button
        self.submit_button = Button(self.quiz_frame, text=submit_state, font=("Arial", "14"), bg=button_colour,
                                    command=partial(self.next, answer, answers))
        self.submit_button.grid(row=3)

        # Frame for the help and answer history buttons
        self.help_history_frame = Frame(self.quiz_frame, width=600, height=600, bg=background_colour, pady=10)
        self.help_history_frame.grid(row=4)

        # Help Button
        self.help_button = Button(self.help_history_frame,
                                  text="Help", command=self.help,
                                  font=("Arial", "14"), bg=button_colour)
        self.help_button.grid(row=0)

        # History Button
        self.history_button = Button(self.help_history_frame,
                                     text="History",
                                     font=("Arial", "14"), bg=button_colour)
        self.history_button.grid(row=0, column=1)

    def next(self, answer, answers):

        answer = answer.get()

        if answer == answers[2]:
            print("Correct!")
        else:
            print("Sorry, That's Wrong.")

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="In order to start the quiz, click the start button. Then select the"
                                          " answer you think is correct and click submit.\n\nThe Answer History"
                                          " page shows your results for the session.\n\nYou can export your results"
                                          " to a .txt file if desired.")


class Help:
    def __init__(self, partner):

        # Formatting Variables
        background_colour = "#A4C2F4"
        button_colour = "#CFE2F3"

        # Disable Help Button
        partner.help_button.config(state=DISABLED)

        # Set up child window (help box)
        self.help_box = Toplevel()

        # Release Help Button if cross is used
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background_colour, width=300)
        self.help_frame.grid()

        # Help Heading
        self.help_heading = Label(self.help_frame, text="Help | Instructions",
                                  font=("Arial", "10", "bold"), bg=background_colour)
        self.help_heading.grid(row=0)

        # Help Text
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background_colour, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button
        self.dismiss_button = Button(self.help_frame, text="Dismiss", width=10, bg=button_colour,
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, pady=10)

    def close_help(self, partner):

        # Put Help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Quiz(root)
    root.mainloop()

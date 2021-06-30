from tkinter import *
from functools import partial
import random


class Quiz:
    def __init__(self):

        # Formatting Variables:
        background_colour = "#A4C2F4"
        button_colour = "#CFE2F3"
        answer = StringVar()
        answers_1 = ["A Car Racing Game", "A Popular Game", "A Game made by a Small Company",
                     "A Game made by a Large Company"]
        answers_2 = ["Team Cherry", "Team Plum", "Team Apricot", "Team Nectarine"]
        answers_3 = ["2014", "2015", "2016", "2017"]
        answers_4 = ["five", "six", "eight", "nine"]
        answers_5 = ["Chaotic Goose", "Goose Simulator", "Untitled Goose Game", "That Goose Game"]
        question_list = ["What is an Indie Game?", "Hollow Knight was made by what team?",
                         "When was Undertale released?", "How many games are there in the FNAF main series?",
                         "What is the name of the game where you control a horrible goose"]

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

        # Answer Boxes (Starts from last question because of stacking)
        self.answer_5_box = OptionMenu(self.quiz_frame, answer, *answers_5)
        self.answer_5_box.grid(row=2, pady=5, padx=10)

        self.answer_5_box.config(width=15)

        self.answer_4_box = OptionMenu(self.quiz_frame, answer, *answers_4)
        self.answer_4_box.grid(row=2, pady=5, padx=10)

        self.answer_4_box.config(width=15)

        self.answer_3_box = OptionMenu(self.quiz_frame, answer, *answers_3)
        self.answer_3_box.grid(row=2, pady=5, padx=10)

        self.answer_3_box.config(width=15)

        self.answer_2_box = OptionMenu(self.quiz_frame, answer, *answers_2)
        self.answer_2_box.grid(row=2, pady=5, padx=10)

        self.answer_2_box.config(width=35)

        self.answer_1_box = OptionMenu(self.quiz_frame, answer, *answers_1)
        self.answer_1_box.grid(row=2, pady=5, padx=10)

        self.answer_1_box.config(width=35)

        # Submit Button
        self.submit_button = Button(self.quiz_frame, text="Submit", font=("Arial", "14"), bg=button_colour,
                                    command=partial(self.answer_checker, answer, question_list, answers_1, answers_2,
                                                    answers_3, answers_4, answers_5))
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

    # Check if the answer's correct or not
    def answer_checker(self, answer, question_list, answers_1, answers_2, answers_3, answers_4, answers_5):

        # Get the selected answer
        answer = answer.get()

        # Checks an answer is selected
        if answer == "":
            print("Please Select an Answer.")
        # Makes sure the answer box exists, destroys the box after to stop the user spamming submit
        elif self.answer_1_box.winfo_exists():
            if answer == answers_1[2]:
                print("Correct!")
                self.question_label.config(text=question_list[1])
                self.answer_1_box.destroy()
            else:
                print('Sorry, the answer is "A Game made by a Small Company".')
                self.question_label.config(text=question_list[1])
                self.answer_1_box.destroy()
        elif self.answer_2_box.winfo_exists():
            if answer == answers_2[0]:
                print("Correct!")
                self.question_label.config(text=question_list[2])
                self.answer_2_box.destroy()
            # Makes sure a new answer has been selected
            elif answer in answers_1:
                print("Please Select a New Answer")
            else:
                print('Sorry, the answer is "Team Cherry".')
                self.question_label.config(text=question_list[2])
                self.answer_2_box.destroy()
        elif self.answer_3_box.winfo_exists():
            if answer == answers_3[1]:
                print("Correct!")
                self.question_label.config(text=question_list[3])
                self.answer_3_box.destroy()
            # Makes sure a new answer has been selected
            elif answer in answers_2:
                print("Please Select a New Answer")
            else:
                print('Sorry, the answer is "2015".')
                self.question_label.config(text=question_list[3])
                self.answer_3_box.destroy()
        elif self.answer_4_box.winfo_exists():
            if answer == answers_4[3]:
                print("Correct!")
                self.question_label.config(text=question_list[4])
                self.answer_4_box.destroy()
                self.answer_5_box.config(width=35)
            # Makes sure a new answer has been selected
            elif answer in answers_3:
                print("Please Select a New Answer")
            else:
                print('Sorry, the answer is "Nine".')
                self.question_label.config(text=question_list[4])
                self.answer_4_box.destroy()
                self.answer_5_box.config(width=35)
        elif self.answer_5_box.winfo_exists():
            if answer == answers_5[2]:
                print("Correct!")
                print("")
                self.question_label.config(text="Thanks for playing!!!")
                self.answer_5_box.destroy()
                self.submit_button.destroy()
            elif answer in answers_4:
                print("Please Select a New Answer")
            else:
                print('Sorry, the answer is "Untitled Goose Game".')
                print("")
                self.question_label.config(text="Thanks for playing!!!")
                self.answer_5_box.destroy()
                self.submit_button.destroy()

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
                                  font=("Arial", "12", "bold"), bg=background_colour)
        self.help_heading.grid(row=0)

        # Help Text
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background_colour, wrap=250,
                               font=("Arial", "10"))
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
    root.title("Indie Quiz")
    something = Quiz()
    root.mainloop()

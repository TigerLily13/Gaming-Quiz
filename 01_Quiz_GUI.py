from tkinter import *
from functools import partial

# Variables are outside the Classes in order to easily pass them into functions
user_answers = []
correct_incorrect = []
correct_answers = ["A Game made by a Small Company", "Team Cherry", "2015", "Nine"]
answers_1 = ["A Car Racing Game", "A Popular Game", "A Game made by a Small Company",
             "A Game made by a Large Company"]
answers_2 = ["Team Cherry", "Team Plum", "Team Apricot", "Team Nectarine"]
answers_3 = ["2014", "2015", "2016", "2017"]
answers_4 = ["Five", "Six", "Eight", "Nine"]
answers_5 = ["Chaotic Goose", "Goose Simulator", "Untitled Goose Game", "That Goose Game"]
question_list = ["What is an Indie Game?", "Hollow Knight was made by what team?",
                 "When was Undertale released?", "How many games are there in the FNAF main series?",
                 "What is the name of the game where you control a horrible goose"]


class Quiz:
    def __init__(self):

        # Formatting Variables:
        background_colour = "#A4C2F4"
        button_colour = "#CFE2F3"
        answer = StringVar()

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
                                    command=partial(self.answer_checker, answer))
        self.submit_button.grid(row=3)

        # Label for answer feedback
        self.answer_label = Label(self.quiz_frame, text="", font=("Arial", "12"), bg=background_colour,
                                  padx=10, pady=10)
        self.answer_label.grid(row=4)

        # Frame for the help and answer history buttons
        self.help_history_frame = Frame(self.quiz_frame, width=600, height=600, bg=background_colour, pady=10)
        self.help_history_frame.grid(row=5)

        # Help Button
        self.help_button = Button(self.help_history_frame,
                                  text="Help", command=self.help,
                                  font=("Arial", "14"), bg=button_colour)
        self.help_button.grid(row=0)

        # History Button
        self.history_button = Button(self.help_history_frame,
                                     text="History", command=self.history,
                                     font=("Arial", "14"), bg=button_colour, state=DISABLED)
        self.history_button.grid(row=0, column=1)

    # Check if the answer's correct or not
    def answer_checker(self, answer):

        # Get the selected answer
        answer = answer.get()

        # Checks an answer is selected
        if answer == "":
            self.answer_label.config(text="Please Select an Answer.")
        # Makes sure the answer box exists, destroys the box after to stop the user spamming submit
        elif self.answer_1_box.winfo_exists():
            if answer == answers_1[2]:
                self.answer_label.config(text="Correct!", bg="#93C47D")
                self.question_label.config(text=question_list[1])
                self.answer_1_box.destroy()
                user_answers.append(answer)
                correct_incorrect.append("correct")
                self.history_button.config(state=NORMAL)
            else:
                self.answer_label.config(text='Sorry, the answer is "A Game made by a Small Company".',
                                         bg="#ffafaf")
                self.question_label.config(text=question_list[1])
                self.answer_1_box.destroy()
                user_answers.append(answer)
                correct_incorrect.append("incorrect")
                self.history_button.config(state=NORMAL)
        elif self.answer_2_box.winfo_exists():
            if answer == answers_2[0]:
                self.answer_label.config(text="Correct!", bg="#93C47D")
                self.question_label.config(text=question_list[2])
                self.answer_2_box.destroy()
                user_answers.append(answer)
                correct_incorrect.append("correct")
            # Makes sure a new answer has been selected
            elif answer in answers_1:
                self.answer_label.config(text="Please Select a New Answer.")
            else:
                self.answer_label.config(text='Sorry, the answer is "Team Cherry".',
                                         bg="#ffafaf")
                self.question_label.config(text=question_list[2])
                self.answer_2_box.destroy()
                user_answers.append(answer)
                correct_incorrect.append("incorrect")
        elif self.answer_3_box.winfo_exists():
            if answer == answers_3[1]:
                self.answer_label.config(text="Correct!", bg="#93C47D")
                self.question_label.config(text=question_list[3])
                self.answer_3_box.destroy()
                user_answers.append(answer)
                correct_incorrect.append("correct")
            # Makes sure a new answer has been selected
            elif answer in answers_2:
                self.answer_label.config(text="Please Select a New Answer.")
            else:
                self.answer_label.config(text='Sorry, the answer is "2015".',
                                         bg="#ffafaf")
                self.question_label.config(text=question_list[3])
                self.answer_3_box.destroy()
                user_answers.append(answer)
                correct_incorrect.append("incorrect")
        elif self.answer_4_box.winfo_exists():
            if answer == answers_4[3]:
                self.answer_label.config(text="Correct!", bg="#93C47D")
                self.question_label.config(text=question_list[4])
                self.answer_4_box.destroy()
                user_answers.append(answer)
                correct_incorrect.append("correct")
                self.answer_5_box.config(width=35)
            # Makes sure a new answer has been selected
            elif answer in answers_3:
                self.answer_label.config(text="Please Select a New Answer.")
            else:
                self.answer_label.config(text='Sorry, the answer is "Nine".',
                                         bg="#ffafaf")
                self.question_label.config(text=question_list[4])
                self.answer_4_box.destroy()
                user_answers.append(answer)
                correct_incorrect.append("incorrect")
                self.answer_5_box.config(width=35)
        elif self.answer_5_box.winfo_exists():
            if answer == answers_5[2]:
                self.answer_label.config(text="Correct!", bg="#93C47D")
                user_answers.append(answer)
                correct_incorrect.append("correct")
                self.question_label.config(text="Thanks for playing!!!",
                                           font=("Arial", "16", "italic"))
                self.answer_5_box.destroy()
                self.submit_button.destroy()
            elif answer in answers_4:
                self.answer_label.config(text="Please Select a New Answer.")
            else:
                self.answer_label.config(text='Sorry, the answer is "Untitled Goose Game".',
                                         bg="#ffafaf")
                user_answers.append(answer)
                correct_incorrect.append("incorrect")
                self.question_label.config(text="Thanks for playing!!!",
                                           font=("Arial", "16", "italic"))
                self.answer_5_box.config(state=DISABLED)
                self.submit_button.destroy()

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="In order to start the quiz, click the start button. Then select the"
                                          " answer you think is correct and click submit.\n\nThe Answer History"
                                          " page shows your results for the session.\n\nYou can export your results"
                                          " to a .txt file if desired.")

    def history(self):
        History(self)


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


class History:
    def __init__(self, partner):

        # Formatting Variables
        background_colour = "#A4C2F4"
        button_colour = "#CFE2F3"

        # Disable History Button
        partner.history_button.config(state=DISABLED)

        # Set up child window (history box)
        self.history_box = Toplevel()

        # Release History Button if cross is used
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background_colour, width=300)
        self.history_frame.grid()

        # History Heading
        self.history_heading = Label(self.history_frame, text="Answer Statistics",
                                     font=("Arial", "10", "bold"), bg=background_colour)
        self.history_heading.grid(row=0)

        # History Text
        self.history_text = Label(self.history_frame, text="Here are your answer statistics. "
                                                           "Use the export button to create a txt file of all "
                                                           "your statistics for this session.", wrap=250,
                                  font=("arial", "10", "italic"), justify=LEFT, width=40, bg=background_colour)
        self.history_text.grid(row=1)

        stats = ""
        question_number = 0
        not_answered = 5

        if len(correct_incorrect) == 5:
            for answer in correct_incorrect:
                question_number += 1
                stats += "Question {}: {}\n".format(question_number, answer.title())
        else:
            for answer in correct_incorrect:
                question_number += 1
                stats += "Question {}: {}\n".format(question_number, answer.title())
            not_answered -= len(correct_incorrect)
            for question in range(not_answered):
                question_number += 1
                stats += "Question {}: Not Answered\n".format(question_number)

        # Display Answer History
        self.stat_label = Label(self.history_frame, text=stats, bg=background_colour,
                                font=("arial", "12"), justify=LEFT)
        self.stat_label.grid(row=2)

        # Export / Dismiss Button Frame
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export", font=("arial", "12", "bold"),
                                    bg=button_colour, command=self.export)
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss", font=("arial", "12", "bold"),
                                     command=partial(self.close_history, partner), bg=button_colour)
        self.dismiss_button.grid(row=0, column=1)

    def export(self):
        Export(self)

    def close_history(self, partner):
        # Put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


class Export:
    def __init__(self, partner,):

        background_colour = "#A4C2F4"
        button_colour = "#CFE2F3"

        # Disable Export Button
        partner.export_button.config(state=DISABLED)

        # Set up child window (export box)
        self.export_box = Toplevel()

        # Release Export Button if cross is used
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, bg=background_colour, width=300)
        self.export_frame.grid()

        # Export Heading
        self.export_heading = Label(self.export_frame, text="Export History",
                                    font=("Arial", "10", "bold"), bg=background_colour)
        self.export_heading.grid(row=0)

        # Export Text
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below and press the save button "
                                                         "to save your calculation history in a text file",
                                 justify=LEFT, width=40, bg=background_colour, wrap=250)
        self.export_text.grid(row=1)

        self.export_text = Label(self.export_frame, text="If the filename you entered below already exists, its "
                                                         "contents will be replaced with your calculation history.",
                                 justify=LEFT, bg="#ffafaf", fg="maroon", wrap=225, padx=10)
        self.export_text.grid(row=2)

        # Filename entry box
        self.filename_entry = Entry(self.export_frame, width=20, font=("Arial", "14", "bold"), justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message
        self.save_error_label = Label(self.export_frame, text="", fg="maroon", bg=background_colour)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save Button
        self.save_button = Button(self.save_cancel_frame, text="Save", font=("Arial", "10", "bold"),
                                  command=partial(lambda: self.save_history(partner)), bg=button_colour)
        self.save_button.grid(row=0, column=0)

        # Cancel button
        self.dismiss_button = Button(self.save_cancel_frame, text="Dismiss", width=10, font=("Arial", "10", "bold"),
                                     command=partial(self.close_export, partner), bg=button_colour)
        self.dismiss_button.grid(row=0, column=1)

    def save_history(self, partner):

        valid_char = "[A-Za-z0-9]"
        has_error = "no"
        problem = ""

        filename = self.filename_entry.get()

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "No spaces allowed"

            else:
                problem = ("No {} allowed".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "Can't be blank"

            has_error = "yes"

        if has_error == "yes":
            self.save_error_label.config(text="Invalid filename - {}" .format(problem))
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # Add .txt prefix
            filename = filename + ".txt"

            # Create file
            f = open(filename, "w+")

            # Add new line for each item
            question_number = 0
            not_answered = 5
            write = ""

            if len(user_answers) == 5:
                for answer in user_answers:
                    incorrect_correct = question_number
                    question_number += 1
                    write += "Question {}: You answered: {}. This was {}\n".format(question_number,
                                                                                   answer,
                                                                                   correct_incorrect[incorrect_correct])
            else:
                for answer in user_answers:
                    incorrect_correct = question_number
                    question_number += 1
                    write += "Question {}: You answered: {}. This was {}\n".format(question_number,
                                                                                   answer,
                                                                                   correct_incorrect[incorrect_correct])
                not_answered -= len(correct_incorrect)
                for question in range(not_answered):
                    question_number += 1
                    write += "Question {}: Not Answered\n".format(question_number)
            f.write(write)

            # Close file
            f.close()

            self.close_export(partner)

    def close_export(self, partner):

        # Put Export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Indie Quiz")
    something = Quiz()
    root.mainloop()

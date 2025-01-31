from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    question1 = simpledialog.askstring(title='Question 1', prompt="What is 15 x 17")
    #      // 3.  Use an if statement to check if their answer is correct
    if question1 == "255":
        score = score + 1
    else:
        score = score - 1
    print(score)
    question2 = simpledialog.askstring(title='Question 2', prompt="What is 1633 / 71")
    if question2 == "23":
        score = score + 1
    else:
        score = score - 1
    print(score)
    if score > 0:
        messagebox.showinfo(message="Good job! You passed!")
        print("User passed")
    else:
        messagebox.showinfo(message="Uh oh! You failed! Try again next time!")
        print("User failed")
    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method

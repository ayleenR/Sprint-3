""" Integration Project: Digital College Assistant """
__author__ = "Ayleen Roque"
def calculate_study_hours(credit_hours):  # New fruitful function
    """The purpose of this function is to calculate the amount of time you
    should spend studying for a class depending on the amount of credits of
    that same class"""
    study_hours = credit_hours ** 2        # Used in line 26
    return study_hours

your_name = input("Hello! What is your name? ")
print("Welcome", your_name)
print("This is your digital college assistant. Nice to meet you!")
full_year = 365
full_year //= 2  # ives the answer of the division
rest_of_year = full_year % 93  # approximate days of summer(remainder)
print("A small reminder that fall and spring have around", full_year, "days")
print("You can rest or work on the remaining approximate", rest_of_year)
print("First, start by finding the credits you are taking this semester")
amount_of_classes = int(input("How many classes do you have this term?: "))
total_credit = 0
for x in range(amount_of_classes):
    credit_per_class = int(input("Enter credit for class: "))
    total_credit += credit_per_class
print("The total amount of credit is:", total_credit)
print("This information keeps your financial aid in check!")
print("Now let's find how much you will need to study per week")
print("To find how long to study per week, enter credit hours of one class")
credit_hours = int(input("Put credit hours of one class here: "))
print("You should study for", calculate_study_hours(credit_hours), "hours")
print("We also have other resources that you can use")
print("For budget assistance: print '101' \nFor calculator: print '202'")
print("If you don't want these resources, print 'no'")
you_decide = input("Put your decision here: ")
if you_decide == "101":
    print("Awesome! Let me help. \nWhat is your budget?")
    budget = float(input())
    print("How much are you planning to spend?")
    spending_amount = float(input())
    print("Your budget is: $", format(budget))
    print("You are planning to spend: $", format(spending_amount))
    percent_kept = int((budget - spending_amount)/budget * 100)
    print("You will keep: $", format(percent_kept, "d"), "%", sep="")  # It
    # formats the number as a percentage, sep = '' takes away space.
    if percent_kept >= 90:
        print("You should be good to spend this! \nTreat yourself!")
    elif percent_kept >= 80:
        print("You can spend it, although it is more reasonable to save it!")
    elif percent_kept >= 70:
        print("Is it absolutely necessary? \nOtherwise, save it!")
    elif percent_kept <= 60:
        print("Save it!")
    else:
        print("Sorry, there must be an error")
elif you_decide == "202":  # chooses calculator
    print("Choose what you need: \n'1' to sum\n'2' to Subtract")
    print("'3' to Multiply \n'4' to Divide")
    choose_one = int(input("Put your choice here: "))
    print("Choose two numbers to perform your chosen operation")
    num1 = int(input("Put your first number here: "))
    num2 = int(input("Put your second number here: "))
    if choose_one == 1:         # addition
        print(num1 + num2)
    elif choose_one == 2:       # subtraction
        print(num1 - num2)
    elif choose_one == 3:       # multiplication
        print(num1 * num2)
    elif choose_one == 4:       # division
        print(num1/num2)
    else:
        print("Sorry, there must be an error!")
elif you_decide == "no":
    print("That's perfectly fine! Look at our other resources")
while you_decide != "101" and you_decide != "202" and you_decide != "no":
    you_decide = 0
    print("Sorry! There must be an error!")
    break
print("We can also provide you with a journal")
print("Would you like to use a journal?")
want_journal = input("Enter 'yes' or 'no': ")
print("Do you want a new journal?")
new_journal = input("Enter 'yes' or 'no': ")
if not want_journal == "yes" and not new_journal == "yes":
    print("That's okay! Feel free to use our other resources")
elif not want_journal == "yes" and new_journal == "yes":
    print("That's okay! Use it whenever you wish")
elif want_journal == "yes" and new_journal == "yes":
    journal_name = input("Name your journal: ")
    todays_Date = input("Enter today's date: ")
    full_Name = input("Enter your full name: ")
    entry_journal = input("Enter your journal entry: ")

    your_File = open(journal_name, 'w')  # Makes a new file
    your_File.write("Name: " + full_Name)
    your_File.write("\nDate: " + todays_Date)
    your_File.write("\nEntry: " + entry_journal)
    your_File.write("\n")
    your_File.close()
    print("Great! It has been saved!")
elif want_journal == "yes" and new_journal == "no":
    journal_name = input("Name your journal: ")
    todays_Date = input("Enter today's date: ")
    full_Name = input("Enter your full name: ")
    entry_journal = input("Enter your journal entry: ")

    your_File = open(journal_name, 'a')  # Saves to existing file
    your_File.write("Name: " + full_Name)
    your_File.write("\nDate: " + todays_Date)
    your_File.write("\nEntry: " + entry_journal)
    your_File.write("\n")
    your_File.close()
    print("Great! It has been saved!")
else:
    print("Sorry, there must be an error!")
print("Lastly, we would like to know how you are feeling")
print("Options are 'happy'\n'excited'\n'stressed'\n'sad'\n'bored'")
your_feelings = input("Enter answer here: ")
if your_feelings == "happy" or your_feelings == "excited":
    print("Great! Keep doing what you are doing")
elif your_feelings == "stressed" or your_feelings == "sad":
    print("Take sometime for yourself! It's important to be happy")
elif your_feelings == "bored":
    print("Do something that you like: take a walk, listen to music, etc...")
else:
    print("There must be an error!")
print("This is the end of the program", your_name, end=' ')
print("Done!" * 5)  # says 'Done!'five times
print("Thank you" + " " + "so much for using the program!")

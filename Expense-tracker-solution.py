import re
#Expense Tracker
#-t: adds a new transaction to log, with the given note and the specified amount
#-d: displays the last n transactions in the log file
#-q: quit & save

def get_balance():
    balance = 0
    try:
        with open("mylog.txt", 'r') as my_file: #open a file to read and assigns it to variable my_file
            for line in my_file:
                for match in re.finditer(r'(-?\d+\.?\d*)\s(\w*)', line): #using re.finditer to search for re in each line
                        balance += float(match.group(1)) # balance = balance + transaction
    except:
        print("The balance hasn't been found.")
    return balance #(float)

def get_amount_of_transaction():
    counter = 0
    try:
        with open("mylog.txt", 'r') as my_file: #open a file to read and assigns it to variable my_file
            for line in my_file: #going through a document line by line
                    counter += 1
    except:
        print(f'Your transactions have not been found.')
    return counter #(int)

def welcome_message():
    try:
        print(f'Welcome Madam/Sir! Currently, your balance is {get_balance()} Euros. There are {get_amount_of_transaction()} transactions in your log file.')
    except:
        print(f'There is an error in welcome message.')

def run_programme():
    welcome_message() #runs welcome_message function
    try:
        run = True #bool
        while run: #runs until run equals to False
            user_input = input("Please enter an input: " + "\n" + "Instructions:" + "\n" "-t: adds a new transaction to log, with the specified amount and given note" + "\n" + "-d: displays the last n transactions in the log file" + "\n" + "-q: quit & save" + "\n")
            if re.match(r"(-t)\s(-?\d+\.?\d*)\s(\w*)", user_input): #checks if re equals to user_input
                amount = float(user_input.split()[1]) # using string.split() method to get "amount" and convert "amount" to float
                note = "" # empty string - note
                for n in range(2, len(user_input.split())):
                    note = note + user_input.split()[n] + " " # goes through all notes (more words)
                with open("mylog.txt", 'a+') as my_file: #opens file to read and append/write at the end of file and assigns it to variable my_file
                    if get_balance() + amount >= 0: # check if there is enough money to make a transaction(ex. balance = 50 + amount = (-70) < 0)
                        my_file.write(str(amount) + ' ' + note + '\n')   #if so, a transaction(float) + new line is appended to file
                        my_file.close() #to save and close file, then we can get updated balance
                        print(f'OK, your balance is now {get_balance()} Euros') #calling get_balance() function
                    else:
                        print(f'Not enough money on your account, your balance is {get_balance()} Euros.') #in case of not having enough money for a transaction

            elif re.match(r"(-d)\s(\d+)", user_input): #checks if re equals to user_input
                counter = 0
                number = int(user_input.split()[1]) # using string.split() method to get "number" and convert "number" to integer
                for line in reversed(open("mylog.txt").readlines()): # reads lines from bottom to top(reversed)
                    counter += 1
                    if number == 0:
                        print("You have entered wrong amount of transactions.")
                        break
                    elif counter <= number:
                        print(line.rstrip()) #all whitespaces on the right are removed from string
                    else:
                        print(f'You have asked for last {number} transaction(s), but there are {get_amount_of_transaction()} transaction(s) all together in your log file.')
                        break

            elif re.match(r"-q", user_input): #checks if re equals to user_input
                    print("Saved status to mylog.txt! Bye!")
                    run = False

            else:
                print(f'You have typed a wrong input! \n-t amount "note": adds a new transaction to log, with the given note and the specified amount \n'
                      f'-d number: displays the last number of transactions in the log file\n-q: save & quit the programme')
    except:
        print(f'En error occurred in the programme.')

run_programme()

# data should be saved after every transaction just in case the programme crashes. Although a file is automatically closed when your program ends it is still a good style to explicitly close your file as soon as the program is done with it.

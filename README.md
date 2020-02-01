# Expense-tracker
Uni task

Write a Python program, which enables the user to keep track of the amount of money available to him/her at a given point in time. The user interacts with the program through a text-based console. The user can add new transactions and view old transactions. Use a text file to save all the transactions carried out by the user. For each transaction save a “note” and an “amount” associated with it. At program start, the text file is loaded and some information is displayed as shown below. The system then runs in an infinite loop and processes user commands. Break your program in reusable functions, wherever it is meaningful to do so.

Three “commands” are known to the system:
 -t amount “note” Adds a new transaction to log, with the given note and the specified amount. Negative amounts denote expenses and positive amounts denote income. Note that the user can only spend the money available. For transactions that would lead to negative balance, display error message “sorry, can’t spend more than you have!”
 -d n Displays the last n transactions in the log file.
 -q Saves data and quits system

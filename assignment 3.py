import csv
with open('questions.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)
    maxtime = 0
    for row in csv_reader:
        hours = int(row[0])
        if hours > maxtime:
            maxtime = hours
# The program starts by reading in all the questions in the questions.csv fil
with open('questions.csv', 'r') as file_handle:
    file_content = csv.reader(file_handle)
    for row in file_content:
        # # Prints them all out to the console, formatted nicely (try playing around with string formatting)
        print('{:<15}  {:<15}'.format(*row))
# Asks the user for a new question to add to the CSV file
with open('C:/Users/relki/Desktop/questions.csv') as file_handle:#
    reader = csv.reader(file_handle)
    next(reader)#
new = input('add a new question to the table: ')
with open('C:/Users/relki/Desktop/questions.csv', 'a', newline='') as fd:
    writer = csv.writer(fd)
    reader = csv.reader(fd)
    # # Generates a unique integer id for that question  ?????
    # # Appends the new question back into the file
    writer.writerow([maxtime+1, new])

# # The program starts by reading in all the answers in the answers.csv file
with open('C:/Users/relki/Desktop/answers.csv', 'r') as file_handle:
    answer_content = csv.reader(file_handle)
    # rows = list(file_content)
    # next(file_content, None)
    # for row in file_content:
    #     print('{:<15}  {:<15}'.format(*row))
# # Prompts the user with every question and reads in the answer.
# Be sure to maintain the question_id relationship with every answer!   ????
name = input('what is your name? :')
with open('C:/Users/relki/Desktop/questions.csv', 'r') as file_handle:
    file_content = csv.reader(file_handle)
    next(file_content, None)
    for row in file_content:
        answer = input(row[1:])
        int_id = row[0]
        with open('C:/Users/relki/Desktop/answers.csv', 'a', newline='') as fd:
            # # Once all questions have been answered, append those answers back out into the answers.csv file
            writer = csv.writer(fd)
            writer.writerow([name, int_id, answer])

# # Reads in all questions in the questions.csv file
# # Reads in all answers in the answers.csv file
# open both files
with open('C:/Users/relki/Desktop/questions.csv') as questions, open('C:/Users/relki/Desktop/answers.csv') as answers:
    # # # Prints out the questions, one at a time, along with the
    # # # corresponding set of answers from all interviewees. Format it nicely!
    # #
    reader = csv.reader(questions)
    next(reader, None)
    reader_a = csv.reader(answers)
    next(reader_a, None)
    for row in reader:
        print(row[1])
        answers.seek(0)
        for line in reader_a:
            if line[1] == row[0]:
                print(line[::2])


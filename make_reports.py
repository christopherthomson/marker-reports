import csv, textwrap

'''
Converts a csv file of student names, essay grades and comments into plain text files to return to students.

The csv file should be formatted as follows:
Surname Firstname Topic Text DateReceived Grade Mark Comment

Notes:
1. Currently it doesn't include Topic, Text or DateReceived in the report.
2. It assumes the existence of a directory 'reports' in which to save the resulting files.
'''
course_name = raw_input('Enter the name of the course: ')
assessment_name = raw_input('Enter the name of the assessment: ')

with open('grades.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        student_name = row[0] + row[1]
        newfile = open("reports/{}.txt".format(student_name), 'wb')
        newfile.write(row[1] + " " + row[0] + "\n")
        newfile.write(course_name + ", " + assessment_name + "\n\n")
        newfile.write(textwrap.fill(row[7]) + "\n\n")
        newfile.write("Grade: " + row[5] + "\n")
        newfile.write("Mark: " + row[6] + "/25\n")
        newfile.close()
        

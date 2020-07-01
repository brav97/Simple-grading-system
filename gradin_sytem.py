

def read_test_scores():
    print("ENTER STUDENT ID: ")
    id = int(input())

    print("ENTER YOUR SCORES: ")
    exam = int(input())

    print("ENTER OTHER SUBJECT SCORES: ")
    score1 = int(input())
    score2 = int(input())
    score3 = int(input())
    score4 = int(input())
    score5 = int(input())
    score6 = int(input())
    score7 = int(input())


    sum = (score1 + score2 + score3 + score4 + score5 + score6 + score7 )

    tavge = sum / 7.0

    return tavge, id, exam

def compute_final_score(tavge, exam):
    final_score = 0.4 * tavge + 0.6 * exam
    return final_score


def get_letter_grade(final_score):
    if 85 <= final_score <= 100:
        grade = 'A'
    elif 80 <= final_score <= 84:
        grade = 'A-'
    elif 75 <= final_score <= 79:
        grade = 'B+'
    elif 70 <= final_score <= 74:
        grade = 'B'
    elif 65 <= final_score <= 69:
        grade = 'B-'
    elif 60 <= final_score <= 64:
        grade = 'C+'
    elif 50 <= final_score <= 59:
        grade = 'C'
    elif 45 <= final_score <= 49:
        grade = 'C-'
    elif 40 <= final_score <= 44:
        grade = 'D+'
    elif 35 <= final_score <= 39:
        grade = 'D'
    elif 30 <= final_score <= 34:
        grade = 'D-'
    elif 0 <= final_score <= 29:
        grade = 'E'
    else:
        grade = 'F'
    return grade


def print_comment(grade):

    if grade == 'A':
        print
        "COMMENT:            Very Good"
    if grade == 'A-':
        print
        "COMMENT:            Very Good"
    elif grade == 'B+':
        print
        "COMMENT:            Good"
    if grade == 'B':
        print
        "COMMENT:            good grades"
    if grade == 'B-':
        print
        "COMMENT:             Good"
    if grade == 'C+':
        print
        "COMMENT:            Good"
    elif grade == 'C':
        print
        "COMMENT:            average grade. Keep working harder"
    if grade == 'C-':
        print
        "COMMENT:            study harder"
    elif grade == 'D+':
        print
        "COMMENT:            Need Improvement"
    if grade == 'D':
        print
        "COMMENT:            improve your grades"
    if grade == 'D-':
        print
        "COMMENT:            Put in more effort"
    elif grade == 'E':
        print
        "COMMENT:            Poor"



tavge, id, exam = read_test_scores()
print("TEST AVERAGE IS:    " + str(tavge))

my_variable = compute_final_score(tavge, exam)
print("FINAL SCORE IS:     " + str(my_variable))

grade = get_letter_grade(my_variable)
print(" CALVIN YOUR AVERAGE GRADE IS:  " + str(grade))

my_reply = print_comment(grade)
print('Hey calvin' + str(my_reply) )


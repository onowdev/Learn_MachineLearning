print("Welcome to GPA Calc")
print("Please enter your latter Grade, one per line")
print("enter the Blank line to designate the end.")

# Map Latter Grade Point Academy
point = {'A+':4.0, 'A':3.90, 'A-':3.89,
        'B+':3.79,'B':3.40,'B-':3.0,
        'C+':2.90, 'C': 2.75, 'C-':2.1,
        'D+':1.90, 'D':1.79, 'D-':1.5,
        'E':0.0
        }
num_course = 0
total_point = 0
done = False

while not done:
    grade = input()
    if grade == '':
        done = True
    elif grade not in point:
        print("Unknown Grade '{0}' being ignored".format(grade))
    else:
        num_course += 1
        total_point += point(grade)
    if num_course > 0:
        print('Your GPA is {0:.3}'.format(total_point/num_course))
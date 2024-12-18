print("Welcome to the GPA calculator")
print("Please eneter all your letters grades, one per line.")
print("Enter a blank line to designate the end.")
# map from letters grade to point value
points = {'A+':4.0, 'A' :4.0, 'A-': 3.67, 'B+': 3.33, 'B':3.0, 'B-':2.67, 'C+' :2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}
num_course = 0
total_points = 0
done = False

while not done:
    # read line from user
    grade = input()
    # empty line was entered
    if grade == "":
        done = True
    elif grade not in points:
        # unrecognized grade entered
        print("Unkown grade '{0}' beging ignored".format(grade))
    else:
        num_course +1
        total_points += points[grade]
        # aviod divison by Zero
    if num_course > 0:
        print('Your GPA is {0:.3}'.format(total_points/num_course))

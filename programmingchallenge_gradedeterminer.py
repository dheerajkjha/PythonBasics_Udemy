var_score = float(input("Please enter the score of the Student."))
if var_score >= 90:
    print("This student's score of " + str(var_score) + " is an A")
else:
    if var_score >= 80:
        print("This student's score of " + str(var_score) + " is a B")
    else:
        if var_score >= 70:
            print("This student's score of " + str(var_score) + " is a C")
        else:
            if var_score >= 60:
                print("This student's score of " + str(var_score) + " is a D")
            else:
                print("This student's score of " + str(var_score) + " is an F")


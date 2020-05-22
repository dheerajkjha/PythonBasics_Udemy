# if else flow control

inp_num = input("Please enter a number.")

if int(inp_num) % 2 == 0:
    print(inp_num + " is an even number.")
else:
    print(inp_num + " is an odd number.")


# Nested if else flow control

gpa = float(input("Please enter the applicant's Grade Point Average."))
inst_app = input("Is the applicant going to be enrolled in an Approved Institution.")

if gpa >= 3.7:
    if inst_app == "yes":
        print("Applicant is eligible for a low APR student loan.")
    else:
        print("Applicant is not enrolled in an Approved Institution.")
else:
    print("Applicant is not approved for a low APR student loan because of low Grade Point Average.")


# elif flow control

user_num_inp = float(input("Please enter an Integer."))

if user_num_inp < 0:
    print("User entered a value less than 0")
elif user_num_inp == 0:
    print("User entered a number equal to 0")
elif 0 < user_num_inp <= 100:
    print("User entered a number between 1 and 100 - " + str(user_num_inp))
else:
    print("User entered the number greater than 100 - " + str(user_num_inp))


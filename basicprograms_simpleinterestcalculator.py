amount = float(input("Please enter the Principal Amount."))
rate = float(input("Please enter the Rate of Interest."))
time = float(input("Please enter the Time Period in Years."))


def simple_interest_cal(para_amo, para_rate, para_time):
    simple_interest = (para_amo * para_rate * para_time) / 100
    print("The Simple Interest amount for {0} at {1}% rate for {2} years is : {3}".format(para_amo, para_rate, para_time, simple_interest))
    return simple_interest


simple_interest_cal(amount, rate, time)
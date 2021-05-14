x=eval(input("Enter Numerator:\n"))
y=eval(input("Enter Denominator:\n"))
try:
    div=x/y
    print(div)
except ZeroDivisionError:
    print("You have entered zero as denominator")

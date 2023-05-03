### if, elif, else statements, with and & or conditional statements

## Grade score outputs
# User input
#score = int(input("score: "))

# Return values - if elif else & and/or statements 
#if score >= 90 and score <= 100:
#    print("Grade: A")
#elif score >= 80 and score < 90:
#    print("Grade: B")
#elif score >= 70 and score < 80:
#    print("Grade: C")
#elif score >= 60 and score < 70:
#    print("Grade: D")
#else:
#    print("Grade: F")\

## Grade score outputs condensed
#User input
#score = int(input("score: "))
# return values
#if 90 <= score <= 100:
#    print("Grade: A")
#elif 80 <= score < 90:
#    print("Grade: B")
#elif 70 <= score < 80:
#    print("Grade: C")
#elif 60 <= score < 70:
#    print("Grade: D")
#else:
#    print("Grade: F")

## Grade score outputs condensed more efficiently
# User input
score = int(input("score: "))

# Grade score outputs
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
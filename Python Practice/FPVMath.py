## Floating Point Value basics

# User input numeric and/or Decimal
#x = float(input("What is x?"))
#y = float(input("What is y?"))

# Print Result
#print(x + y)

## FPV Round to nearest int

# User Input
#x = float(input("What is x? "))
#y = float(input("What is y? "))

# Create rounded result
#z = round(x + y)

# Print result
#print(z)

## Number formatting

# User Input
#x = float(input("What is x?"))
#y = float(input("What is y?"))

# Round result
#z = round(x + y)

# Print formatted result
#print(f"{z:,}")

## FPV Division

# User Input
#x = float(input("What is x?"))
#y = float(input("What is y?"))

# Division
#z = x / y

# Print the Result
#print(z)

## FPV Division and Rounding
#x = float(input("What is x?"))
#y = float(input("What is y?"))

# calculate result and round
#z = round(x / y, 2)

# Print result
#print(z)

## FPV Division and Rounding using fstring same result as above
x = float(input("What is x?"))
y = float(input("What is y?"))

# Calculate result
z = x / y

# Print result
print(f"{z:.2f}")
## can be modified as such to print formatted 4 digit + numbers
### print(f"{z:,.2f}")
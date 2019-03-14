largest_number = True

first_number = int(input("Please enter a number: "))
while first_number < 0 or first_number > 10000:
    print("Please enter a number greater than 0 and less than 10000.")
    first_number = int(input("Please enter a number: "))
    
second_number = int(input("Please enter another number: "))
while second_number < 0 or second_number > 10000:
    print("Please enter a number greater than 0 and less than 10000.")
    second_number = int(input("Please enter another number: "))
    
third_number = int(input("Please enter another number: "))
while third_number < 0 or third_number > 10000:
    print("Please enter a number greater than 0 and less than 10000.")
    third_number = int(input("Please enter another number: "))
    
fourth_number = int(input("Please enter yet another number: "))
while fourth_number < 0 or fourth_number > 10000:
    print("Please enter a number greater than 0 and less than 10000.")
    fourth_number = int(input("Please enter yet another number: "))

fifth_number = int(input("Please enter a final number: "))
while fifth_number < 0 or fifth_number > 10000:
    print("Please enter a number greater than 0 and less than 10000.")
    fourth_number = int(input("Please enter a final number: "))

if first_number > second_number and first_number > third_number and first_number > fourth_number and first_number > fifth_number:
    print("The largest number is", first_number,".")
elif second_number > third_number and second_number > fourth_number and second_number > fifth_number:
    print("The largest number is", second_number,".")
elif third_number > fourth_number and third_number > fifth_number:
    print("The largest number is", third_number,".")
elif fourth_number > fifth_number:
    print("The largest number is", fourth_number,".")
else:
    print("The largest number is", fifth_number,".")


if first_number < second_number and first_number < third_number and first_number < fourth_number and first_number < fifth_number:
    print("The smallest number is", first_number,".")
elif second_number < third_number and second_number < fourth_number and second_number < fifth_number:
    print("The smallest number is", second_number,".")
elif third_number < fourth_number and third_number < fifth_number:
    print("The smallest number is", third_number,".")
elif fourth_number < fifth_number:
    print("The smallest number is", fourth_number,".")
else:
    print("The smallest number is", fifth_number,".")

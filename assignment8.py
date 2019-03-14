largest_number = True
first_number = int(input("Please enter a number: "))
second_number = int(input("Please enter another number: "))
third_number = int(input("Please enter another number: "))
fourth_number = int(input("Please enter yet another number: "))
fifth_number = int(input("Please enter a final number: "))


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

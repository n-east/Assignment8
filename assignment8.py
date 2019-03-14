largest_number = True
first_number = int(input("Please enter a number: "))
second_number = int(input("Please enter another number: "))
third_number = int(input("Please enter another number: "))
fourth_number = int(input("Please enter yet another number: "))
fifth_number = int(input("Please enter yet another number: "))
sixth_number = int(input("Please enter a sixth number: "))
seventh_number = int(input("Please enter a seventh number: "))
eigth_number = int(input("Please enter an eigth number: "))
ninth_number = int(input("Please enter a ninth number: "))
tenth_number = int(input("Please enter a tenth number: "))

def print_results():
    if (first_number > second_number and first_number > third_number and first_number > fourth_number and first_number > fifth_number
            and first_number > sixth_number and first_number > seventh_number and first_number > eigth_number and first_number > ninth_number and first_number > tenth_number):
        print("The largest number is", first_number,".")
    elif (second_number > third_number and second_number > fourth_number and second_number > fifth_number
            and second_number > sixth_number and second_number > seventh_number and second_number > eigth_number and second_number > ninth_number and second_number > tenth_number):
        print("The largest number is", second_number,".")
    elif (third_number > fourth_number and third_number > fifth_number
            and third_number > sixth_number and third_number > seventh_number and third_number > eigth_number and third_number > ninth_number and third_number > tenth_number):
        print("The largest number is", third_number,".")
    elif (fourth_number > fifth_number and fourth_number > sixth_number and fourth_number > seventh_number and fourth_number > eigth_number
            and fourth_number > ninth_number and fourth_number > tenth_number):
        print("The largest number is", fourth_number,".")
    elif (fifth_number > sixth_number and fifth_number > seventh_number and fifth_number > eigth_number
            and fifth_number > ninth_number and fifth_number > tenth_number):
        print("The largest number is", fifth_number,".")
    elif (sixth_number > seventh_number and sixth_number > eigth_number
            and sixth_number > ninth_number and sixth_number > tenth_number):
        print("The largest number is", sixth_number,".")
    elif (seventh_number > eigth_number and sixth_number > ninth_number and sixth_number > tenth_number):
        print("The largest number is", seventh_number,".")
    elif (eigth_number > ninth_number and eigth_number > tenth_number):
        print("The largest number is", eigth_number,".")
    elif ninth_number > tenth_number:
        print("The largest number is", ninth_number)
    else:
        print("The largest number is", tenth_number)


    if (first_number < second_number and first_number < third_number and first_number < fourth_number and first_number < fifth_number
            and first_number < sixth_number and first_number < seventh_number and first_number < eigth_number and first_number < ninth_number and first_number < tenth_number):
        print("The smallest number is", first_number,".")
    elif (second_number < third_number and second_number < fourth_number and second_number < fifth_number
            and second_number < sixth_number and second_number < seventh_number and second_number < eigth_number and second_number < ninth_number and second_number > tenth_number):
        print("The smallest number is", second_number,".")
    elif (third_number < fourth_number and third_number < fifth_number
            and third_number < sixth_number and third_number < seventh_number and third_number < eigth_number and third_number < ninth_number and third_number > tenth_number):
        print("The smallest number is", third_number,".")
    elif (fourth_number < fifth_number and fourth_number < sixth_number and fourth_number < seventh_number and fourth_number < eigth_number
            and fourth_number < ninth_number and fourth_number < tenth_number):
        print("The smallest number is", fourth_number,".")
    elif (fifth_number < sixth_number and fifth_number < seventh_number and fifth_number < eigth_number
            and fifth_number < ninth_number and fifth_number < tenth_number):
        print("The smallest number is", fifth_number,".")
    elif (sixth_number < seventh_number and sixth_number < eigth_number
            and sixth_number < ninth_number and sixth_number < tenth_number):
        print("The smallest number is", sixth_number,".")
    elif (seventh_number < eigth_number and sixth_number < ninth_number and sixth_number < tenth_number):
        print("The smallest number is", seventh_number,".")
    elif (eigth_number < ninth_number and eigth_number < tenth_number):
        print("The smallest number is", eigth_number,".")
    elif ninth_number < tenth_number:
        print("The smallest number is", ninth_number)
    else:
        print("The smallest number is", tenth_number)


def main():
    print_results ()

main()
def calculator():
    while True:
        print("Welcome to Pytho Calculator")
        print("Select The Operation")
        print("1. Addition (+) \n"
              "2. Subtraction (-)\n"
              "3.Multiplication (*)\n"
              "4. Division (/)\n"
              "5. Modulus (%)\n"
              "6.Exponentiation (**)\n"
              "7.Floor Division (//)\n"
              "8. Exit")

        #Take Input from user
        choice=input("\n\nEnter Your Choice Operations: \n\n")

        if choice == '8':
            print("Thank You For Using Calculator. Good Day")
            exit()

        elif choice in ('1', '2', '3', '4', '5', '6','7'):
            try:
                print("Enter The  Numbers")
                num1=float(input("Number 1: "))
                num2=float(input("Number 2: "))

                if choice=='1':
                    print(f"\n Addition of two number is:\n {num1+num2}")
                elif choice=='2':
                    print(f"\n Subtraction of Two Number is:\n {num1 - num2}")
                elif choice == '3':
                    print(f"\n Multiplication of two number is:\n {num1 * num2}")
                elif choice=='4':
                    if num2 != 0:
                        print(f"\n Division of two number is:\n {num1 / num2}")
                    else:
                        print("\n Error ! Division by Zero\n")
                elif choice == '5':
                    print(f"\n Modulus of two number is:\n {num1 % num2}")
                elif choice == '6':
                    print(f"\n Exponentiation of two number is:\n {num1 ** num2}")
                elif choice == '7':
                    print(f"\n Floor Division of two number is:\n {num1 // num2}")

            except ValueError:
                print("Invalid Input. Please enter Valid numeric values\n")
        else:
            print("Invalid Choice. Please enter Valid Choice\n")

# Call the calculator function
calculator()

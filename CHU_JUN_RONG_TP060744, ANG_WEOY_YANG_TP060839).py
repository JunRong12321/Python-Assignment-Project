# ANG WEOY YANG
# TP060839
# CHU JUN RONG
# TP060744

# Create Empty List for functions that will be using the list
car_list = []
unique_car_brand_list = []


# Select Car Brands
def car_brand_choice():
    print()
    # Opening car details file and append the data into car_list
    available_car = open("car_details.txt", "r")
    # Appending data into the empty list
    for i in available_car:
        car_list.append(i.strip("\n").split("|"))
        # Check on the car brand list and append to unique_car_brand_list
        for j in car_list:
            if j[0] not in unique_car_brand_list:
                unique_car_brand_list.append(j[0])
    counter = 1
    # Show the car brand with numbering
    for k in unique_car_brand_list:
        print("%s." % counter, k)
        counter = counter + 1
    # Keep looping the search car details until user enter 'X'
    while True:
        choice = str(input("\nEnter your desired car brand:\t"))
        print()
        # Check on the input Error
        if choice.upper() not in unique_car_brand_list:
            print("Invalid Input!!!")
            print("Please try again.")
            cont = input("<Enter> to continue ['X' to exit]:\t")
            # Exit the function
            if cont.upper() == "X":
                print()
                break
            else:
                continue
        # Showing the car details of the car brand entered
        elif choice.upper() in unique_car_brand_list:
            print("The selected car brand is:\t", choice.upper())
            return choice.upper()


# Show Rented Car Details
def show_rented_car():
    # Keep looping the function until user enter 'X' to exit the function
    while True:
        # Call out car_brand_choice function
        car_brand = car_brand_choice()
        print()
        counter = 1
        for i in car_list:
            # Print our function according to the details title
            if (i[0] == car_brand) and (i[4] == "1"):
                print("No.%s" % counter)
                counter = counter + 1
                print("Car Brand        :\t%s" % i[0])
                print("Car Model        :\t%s" % i[1])
                print("Plate Number     :\t%s" % i[2])
                print("Charge Per Hour  :\tRM%s.00" % i[3])
                print("Member           :\t%s" % i[5])
                print("Hours Booked     :\t%s" % i[6])
                print("Payment Status   :\t%s" % i[7])
                print()

            # Telling the user that there is no rented car details for that car brand
            elif (i[0] == car_brand) and (i[4] == "0"):
                while counter < 1:
                    print("There is no", car_brand, "car rented out at the moment.")
        print()
        # For user choose to continue or exit the function
        cont = input("[Press any key to view rented cars for the other brands / 'X' to exit]:\t")

        # Exit
        if cont.upper() == "X":
            print()
            break
        # Continue Function
        else:
            continue


# Show Available Car for Rent Details
def show_car():
    # Keep looping the function until user enter 'X' to exit the function
    while True:
        # Call out car_brand_choice function
        car_brand = car_brand_choice()
        print()
        counter = 0
        for i in car_list:
            # To declare the car is available by looking at the fifth index as '0'
            if (i[0] == car_brand) and (i[4] == "0"):
                counter = counter + 1
                print("No.%s" % counter)
                print("Car Brand        :\t%s" % i[0])
                print("Car Model        :\t%s" % i[1])
                print("Plate Number     :\t%s" % i[2])
                print("Charge Per Hour  :\tRM%s.00" % i[3])
                print()
        # For user choose to continue or exit the function
        cont = input("[Press any key to view available cars for the other brands / 'X' to exit]:\t")

        # Exit
        if cont.upper() == "X":
            print()
            break
        # Continue Function
        else:
            continue


# Show Car Bookings Details
def car_booked():
    # Create empty list for appending details into the list
    car_booked_list = []
    # Opening the car details file
    car_list = open('car_details.txt', 'r')
    # Appending data into the empty list
    for i in car_list:
        car_booked_list.append(i.strip("\n").split("|"))
    counter = 1
    # Print out all booked car details according to fifth index which is '1'
    for j in car_booked_list:
        if j[4] == "1":
            print("No.%s" % counter)
            print("Member        :\t%s" % j[5])
            print("Car Brand     :\t%s" % j[0])
            print("Car Model     :\t%s" % j[1])
            print("Plate Number  :\t%s" % j[2])
            print()
            counter = counter + 1


# Show Member's Username for searching Car Bookings Details
def specific_customer_booking():
    print("-" * 15, "[Customer List]", "-" * 17)
    # Create empty list for appending details into the list
    car_booked_list = []
    # Opening the car details file
    car_list = open('car_details.txt', 'r')
    # Appending data into the empty list
    for i in car_list:
        car_booked_list.append(i.strip("\n").split("|"))
    counter = 1
    # Showing member's username according to which member who has booked car
    for j in car_booked_list:
        # Declaring the fifth index
        if j[4] == "1":
            print("%s.\t" % counter, j[5])
            counter = counter + 1
    print("-" * 49)
    # Open customer details
    search_name = input("Enter Customer Name:\t")
    for k in car_booked_list:
        if k[5].upper() == search_name.upper():
            print("Member           :\t%s" % k[5])
            print("Car Brand        :\t%s" % k[0])
            print("Car Model        :\t%s" % k[1])
            print("Plate Number     :\t%s" % k[2])
            print("Charge Per Hour  :\tRM%s.00" % k[3])
            print()


# Show Customer Payment Details
def customer_payment():
    # Create empty list for appending details into the list
    car_paid_list = []
    # Opening the car details file
    car_booked_list = open('car_details.txt', 'r')
    # Appending data into the empty list
    for i in car_booked_list:
        car_paid_list.append(i.strip("\n").split("|"))
    counter = 1
    for j in car_paid_list:
        # Showing the customer payment details which sixth index have customer name
        if j[5] != "-":
            print("No.%s" % counter)
            counter = counter + 1
            print("Member        :\t%s" % j[5])
            print("Car Brand     :\t%s" % j[0])
            print("Car Model     :\t%s" % j[1])
            print("Plate Number  :\t%s" % j[2])
            payment = int(int(j[6])*int((j[3])))
            print("Payment       :\tRM%.2f" % payment)
            print("Payment Status:\t%s" % j[7])
            print()


# Show Rented Cars Details within the Entered Rental Hours
def specific_customer_payment():
    # Create empty list for appending details into the list
    car_paid_list = []
    # Opening the car details file
    car_booked_list = open('car_details.txt', 'r')
    # Appending data into the empty list
    for i in car_booked_list:
        car_paid_list.append(i.strip("\n").split("|"))
    # Keep looping the function until user enter 'X' to exit the function
    while True:
        print("-" * 15, "[Rental Hour(s)]", "-" * 16)
        # Enter the Rental Hours to check on car details that were booked within the Rental Hour
        search_choice = input("Enter Rental Hour(s) ['x' to exit]:\t")
        try:
            search_choice = int(search_choice)
            counter = 1
            # Show car details which were booked within the Rental Hour
            for j in car_paid_list:
                if j[5] != "-":
                    if int(j[6]) <= search_choice:
                        print("No.%s" % counter)
                        print("Member        :\t%s" % j[5])
                        print("Car Brand     :\t%s" % j[0])
                        print("Car Model     :\t%s" % j[1])
                        print("Plate Number  :\t%s" % j[2])
                        print("Rental Hour(s):\t%s hour(s)" % j[6])
                        payment = int(int(j[6])*int((j[3])))
                        print("Payment       :\tRM%.2f" % payment)
                        print()
                        counter = counter + 1
                        continue

        except:  # Declare the input whether it is an invalid input
            if (search_choice == str) and (search_choice.upper() != 'X'):
                print()
                print("Invalid Input!!!")
                print("Try Again.")
                continue
            # Exit
            elif search_choice.upper() == 'X':
                print()
                print("Return to Records List.")
                print("-" * 49)
                break


# Add New Cars to be Rent Out Details
def add_rent_out_car():
    car_quantity = int(input("How Many Cars to Add:\t"))
    # Keep looping the function until user enter 'X' to exit the function
    while True:
        try:
            counter = 1
            # Loop the function based on the number entered by user
            while counter <= car_quantity:
                print()
                print("Car", counter, ":")
                # Opening car details file and append data into the last in the file
                add_car = open("car_details.txt", "a+")
                car_brand = input("Enter Car Brand:\t")
                car_type = input("Enter Car Model  :\t")
                car_plate = input("Enter Plate Number:\t")
                charge_per_hour = input("Enter Charge Per Hour:\t")
                availability = "0"
                member_booked = "-"
                hours = "0"
                payment_status = "UNPAID"
                # ways of data were stored in the file
                add_car_details = (car_brand.upper(), "|", car_type.upper(), "|", car_plate.upper(), "|", charge_per_hour, "|", availability, "|", member_booked.upper(), "|", hours, "|", payment_status.upper() + "\n")
                add_car.writelines(add_car_details)
                add_car.close()
                counter = counter + 1

            # Print comment when the car quantity is 1
            if (counter - 1) == 1:
                print((counter - 1), "car is added into available list successfully.")
                print()
            # Print comment when the car quantity is more than 1
            elif (counter - 1) > 1:
                print(counter, "cars are added into available list successfully.")
                print()
            else:
                print()
                print("Invalid Input!!!")
                print("Try Again.")
            break
        except:  # Declare the input whether it is an invalid input
            if type(car_quantity) == str:
                print()
                print("Invalid Input!!!")
                print("Try Again.")
            continue


# Modify Car's Details
def modify_car_details():
    # Keep looping the function until user enter 'X' to exit the function
    while True:
        print("-" * 13, "[Modify Car Details]", "-" * 14)
        print("1  - Modification")
        print("'x' - Exit to Admin Page")
        print()
        # Giving option for user to enter the Modify Car Details Number
        modify_details = input("Enter Modify Number ['x' to exit]:\t")
        print()
        try:
            modify_details = int(modify_details)
            if modify_details == 1:
                counter = 1
                # Opening the car details file
                file = open('car_details.txt', 'r')
                # Print out the data in car details
                data = file.readlines()
                print("Car Records: ")
                print()
                # Numbering
                for i in data:
                    if counter < 10:
                        print("0%s." % counter, i, end='')
                        counter = counter + 1
                    else:
                        print("%s." % counter, i, end='')
                        counter = counter + 1
                print()
                # Enter the Numbering to modify details
                n = int(input("Which record do you want to modify:\t"))
                print()
                print("Record before modification                 :\t" + data[n-1])
                print("Format                                     :\tCAR BRAND|CAR MODEL|PLATE NUMBER|CHARGE PER HOUR|AVAILABILITY|MEMBER BOOKED|HOURS OF BOOKING|PAYMENT STATUS")
                print()
                print("Modification:")
                # Enter the new details and re-enter the details which should be kept
                car_brand = str(input("Enter the new car brand                    :\t"))
                car_type = str(input("Enter the new car model                    :\t"))
                car_plate = str(input("Enter the new plate number                 :\t"))
                charge_per_hour = str(input("Enter the new charge per hour (RM)         :\t"))
                member_booked = str(input("Enter the new member booked ['-' if null]  :\t"))

                # Define the data as available car
                if len(member_booked) < 1:
                    member_booked = "-"
                    availability = "0"
                    hours = "0"
                    payment_status = "UNPAID"
                elif member_booked == "-":
                    availability = "0"
                    hours = "0"
                    payment_status = "UNPAID"
                # Define the data as booked car
                else:
                    availability = "1"
                    hours = str(input("Enter the new total hours of booking       :\t"))
                    payment_status = str(input("Enter the new payment status (PAID/UNPAID) :\t"))

                # Ways of data will be stored in files
                data[n-1] = (car_brand.upper() + "|" + car_type.upper() + "|" + car_plate.upper() + "|" + charge_per_hour + "|" + availability + "|" + member_booked.upper() + "|" + hours + "|" + payment_status.upper()) + "\n"

                print()
                print("Record after modifications:\n" + data[n-1])
                # Opening the car details file
                file = open('car_details.txt', 'w')
                file.writelines(data)

            else:  # Declare the input whether it is an invalid input
                print()
                print("Invalid Input!!!")
                print("Try Again.")
                continue
        except:  # Declare the input whether it is an invalid input
            if type(modify_details) == str and (modify_details.upper() != 'X'):
                print()
                print("Invalid Input!!!")
                print("Try Again.")
                continue
            # Exit
            elif modify_details.upper() == 'X':
                print()
                print("Return to Admin Page.")
                print("-" * 49)
                break
            # Showing as an Error to user on no file can be open
            else:
                print("File cannot be opened.")
                break


# Display All Related Car's Records
def display_car_records():
    # Keep looping the function until user enter 'X' to exit the function
    while True:
        print("-" * 15, "[Records List]", "-" * 18)
        print(" 1  - Rented Car Details")
        print(" 2  - View Available Car")
        print(" 3  - Customer Booking")
        print(" 4  - Customer Payment")
        print("'x' - Exit to Admin Page")
        print()
        # Giving option for user to enter the Records Number
        search_records = input("Enter Records Number ['x' to exit]:\t")
        try:
            search_records = int(search_records)
            if search_records == 1:
                print()
                print("-" * 13, "[Rented Out Cars]", "-" * 17)
                # Call out show rented car function
                show_rented_car()
                continue
            elif search_records == 2:
                print()
                print("-" * 14, "[Available Car]", "-" * 18)
                # Call out available car details function
                show_car()
                continue
            elif search_records == 3:
                print()
                print("-" * 11, "[Customer Booked Car]", "-" * 15)
                # Call out booked car details function
                car_booked()
                continue
            elif search_records == 4:
                print()
                print("-" * 9, "[Customer Payment Details]", "-" * 12)
                # Call out customer payment details function
                customer_payment()
                continue
            elif search_records > 4:
                # Declare the input whether it is an invalid input
                print()
                print("Invalid Input!!!")
                print("Try Again.")
                continue

        except:  # Declare the input whether it is an invalid input
            if (type(search_records) == str) and (search_records.upper() != 'X'):
                print()
                print("Invalid Input!!!")
                print("Try Again.")
                continue
            # Exit
            elif search_records.upper() == 'X':
                print()
                print("Return to Admin Page.")
                print("-" * 49)
                break


# Search Functions on Customer Booking and Customer Payment
def search():
    # Keep looping the function until user enter 'X' to exit the function
    while True:
        print("-" * 13, "[Search for Details]", "-" * 14)
        print(" 1  - Customer Booking")
        print(" 2  - Customer Payment")
        print("'x' - Exit to Admin Page")
        # Giving option for user to enter the Search Details Number
        search_details = input("Enter Search Number ['x' to exit]:\t")
        try:
            search_details = int(search_details)
            if search_details == 1:
                print()
                print("-" * 13, "[Booked Car Details]", "-" * 14)
                print()
                # Call out specific customer booking function
                specific_customer_booking()
                continue
            elif search_details == 2:
                print()
                print("-" * 10, "[Customer Payment Details]", "-" * 11)
                # Call out specific customer payment function
                specific_customer_payment()
                continue

            else:  # Declare the input whether it is an invalid input
                print()
                print("Invalid Input!!!")
                print("Try Again.")
                continue

        except:  # Declare the input whether it is an invalid input
            if type(search_details) == str and (search_details.upper() != 'X'):
                print()
                print("Invalid Input!!!")
                print("Try Again.")
                continue
            # Exit
            elif search_details.upper() == 'X':
                print()
                print("Return to Admin Page.")
                print("-" * 49)
                break


# Return Rented Car's Details
def return_rented_car():
    print()
    # Create empty list for appending details into the list
    car_paid_list = []
    # Opening the car details file
    car_booked_list = open('car_details.txt', 'r')
    # Appending data into the empty list
    for i in car_booked_list:
        car_paid_list.append(i.strip("\n").split("|"))
    # Showing booked car details and paid car details
    for j in car_paid_list:
        if i[4] == "1":
            print("Member Booked :\t", j[5])
            print("Plate Number  :\t", j[2])
            print()
    while True:
        # Entering the Plate Number of the car to return
        return_choice = input("Enter Plate Number to return car:\t")
        for k in car_paid_list:
            if k[2] == return_choice.upper():
                # Print out the entered car details
                print()
                print("Member        :\t%s" % k[5])
                print("Car Brand     :\t%s" % k[0])
                print("Car Model     :\t%s" % k[1])
                print("Plate Number  :\t%s" % k[2])
                # Calculate the payment amount
                payment = int(int(k[6])*int((k[3])))
                print("Payment       :\tRM%.2f" % payment)
                print("Payment Status:\t%s" % k[7])
                print()
                # Option for user on continue the progress
                cont = input("<Enter> to continue progress ['X' to cancel]:\t")
                if cont.upper() != "X":
                    # Change the data and store it into list
                    k[4] = '0'
                    k[5] = '-'
                    k[6] = '0'
                    k[7] = 'UNPAID'
                    # Open file and rewrite the data into file
                    car_details = open("car_details.txt", "w")
                    for details in car_paid_list:
                        for rewrite in details:
                            # Write each data of the car
                            car_details.write(rewrite)
                            car_details.write("|")
                        # Write each car details into the file
                        car_details.write("\n")
                    car_details.close()
                    break
                # Cancel the return process
                elif cont.upper() == "X":
                    print("You have cancelled the progress.")
                    break
            else:  # Error
                print("Invalid Input!!!")
                print("Please Try Again.")
                continue


# Admin Page
def admin():
    # Keep looping the function until user enter 'X' to exit the function
    while True:
        print("-" * 17, "[Admin Page]", "-" * 18)
        print(" 1  - Add Rent Out Car")
        print(" 2  - Modify Car Details")
        print(" 3  - Display Car's Records")
        print(" 4  - Search")
        print(" 5  - Return Rented Car")
        print("'x' - Exit")
        print("-" * 49)
        print()
        # Giving option for user to enter the Admin Page Number
        admin_choice = input("Enter Admin Page Number ['x' to exit]:\t")
        try:
            admin_choice = int(admin_choice)
            if admin_choice == 1:
                print()
                # Call out add rent out car function
                add_rent_out_car()
                continue
            elif admin_choice == 2:
                print()
                # Call out modify car details function
                modify_car_details()
                continue
            elif admin_choice == 3:
                print()
                # Call out display car records function
                display_car_records()
                continue
            elif admin_choice == 4:
                print()
                # Call out search function
                search()
                continue
            elif admin_choice == 5:
                # Call out return rented car function
                return_rented_car()
                continue
            else:  # Declare the input whether it is an invalid input
                print("Invalid Input!!!")
                print("Try Again.")
                continue
        except:  # Declare the input whether it is an invalid input
            if admin_choice.upper() != 'X':
                print()
                print("Invalid Input!!!")
                print("Try Again.")
                continue
            # Exit
            else:
                print("Exit to Home Page.")
                print("-" * 49)
                home_page()


# Opening the login details file
check_login = open("login_details.txt", "r")
# Create empty list for appending details into the list
login_details = []
login_temp = []
# Appending data into the empty list
for i in check_login:
    login_temp.append(i.strip("\n").split("|"))


# Login Function
def login():
    # Opening the login details file
    check_login = open("login_details.txt", "r")
    # Appending data into the empty list
    for i in check_login:
        login_details.append(i.strip("\n").split("|"))
    # Keep looping the function until user enter 'X' to exit the function
    while True:
        try:
            # Requires user to enter username and password to access the function
            input_username = input("Enter Username:\t")
            input_password = input("Enter Password:\t")
            for j in login_details:
                # Searching the username and password in data file
                if j[1].upper() == input_username.upper():
                    if j[2].upper() == input_password.upper():
                        login_details_reference = j[0]
                        username_identity = j[3]
                    # Declare whether the user is admin or member
                        if j[3] == "admin":
                            print("-" * 49)
                            print("Welcome %s." % j[1])
                            print()
                            # Call out admin page function
                            admin()
                            break
                        else:
                            print("-" * 49)
                            print("Welcome %s." % j[1])
                            print()
                            # Call out member page function
                            member(input_username, input_password, login_details_reference, username_identity)
                            break

                    else:  # Declare the input whether it is an invalid input
                        print("Invalid Input!!!")
                        choice = input("Do you wish to continue?<Enter> or 'X'<No>:\t")
                        if choice.upper() == "X":
                            break
                    # Exit
                    break
        except:
            break

# Register as member for new customer
def register_as_member():
    # Create empty list for appending details into the list
    n = []
    for i in login_temp:
        # Appending data into the empty list
        n.append(int(i[0]))
    mem_id = len(n)
    # Keep looping the function until user enter 'X' to exit the function
    while True:
        # Open Registration Page
        print("-" * 13, "[Registration Page]", "-" * 15)
        print("-" * 49)
        # Providing spaces for new customer to enter their username and password
        username_cust_new = str(input("Create Username:\t"))
        password_cust_new = str(input("Create Password:\t"))
        password_cust_confirm = str(input("Confirm your password:\t"))
        # Declare whether the password is the same
        if password_cust_confirm == password_cust_new:
            print("You have successfully become a member.")
            print()
            # Opening login details files and append the data into files
            check_login = open("login_details.txt", "a")
            new_login_details = (str(mem_id), "|", username_cust_new.upper(), "|", password_cust_confirm, "|", "member" + "\n")
            check_login.writelines(new_login_details)
            check_login.close()
            login_details.append(new_login_details)
            break

        # Declare the input whether it is an invalid input
        elif password_cust_confirm != password_cust_new:
            print()
            print("Invalid Input!!!")
            print("Try Again.")
            continue

# Customer Page
def customer():
    # Keep looping the function until user enter 'X' to exit the function
    while True:
        print("-" * 16, "[Customer Page]", "-" * 16)
        print(" 1  - View Available Car")
        print(" 2  - Register as a Member (For New Customer)")
        print("'x' - Back To Home Page")
        print("-" * 49)
        # Giving option for user to enter the Customer Page Number
        customer_choice = input("Enter List Number ['x' to exit]:\t")
        try:
            customer_choice = int(customer_choice)
            if customer_choice == 1:
                print()
                print("-" * 16, "[Available Car]", "-" * 16)
                # Call out available car details function
                show_car()
                continue
            elif customer_choice == 2:
                # Call out registration function
                register_as_member()
                continue
            else:
                # Declare the input whether it is an invalid input
                print()
                print("Invalid Input!!!")
                print("Try Again.")
                continue

        except:
            # Declare the input whether it is an invalid input
            if type(customer_choice) == str and (customer_choice.upper() != 'X'):
                print()
                print("Invalid Input!!!")
                print("Try Again.")
                continue
            # Exit
            else:
                # Call out home page function
                home_page()


# Modifying Personal Details on Member's Username and Password
def modify_member_details(input_username, input_password, login_details_reference, username_identity):
    # Keep looping the function until user enter 'X' to exit the function
    while True:
        # Opening the login details file
        file = open('login_details.txt', 'r')
        # Read data within the file
        data = file.readlines()
        # Confirming the user is accessing their data
        print("Member Name              :\t" + input_username.upper())
        verification = input("Please enter your password to verify your identity :\t")
        # Ensuring the password is correct before modifying
        if verification == input_password:
            print()
            print("Record before modification       :\t" + data[int(login_details_reference)])
            # Showing format of data that were stored in file
            print("Format                           :\tMEMBER NUMBER|MEMBER NAME|MEMBER PASSWORD|MEMBER")
            print()
            print("Modification:")
            # Requires user to enter the new username or new password
            member_name = str(input("Enter the new member name    :\t"))
            member_password = str(input("Enter the new member password:\t"))
            data[int(login_details_reference)] = (login_details_reference + "|" + member_name.upper() + "|" + member_password + "|" + username_identity + "\n")
            print()
            print("Record after modifications       :\t" + data[int(login_details_reference)])
            # Opening the login details file
            file = open('login_details.txt', 'w')
            file.writelines(data)
            break
        else:
            print("WRONG PASSWORD!!!")
            print("Please Try Again.")
            continue


# Show Member's Personal Rental Details
def personal_rental_history(input_username):
    # Create empty list for appending details into the list
    car_list = []
    # Opening the car details file
    available_car_list = open('car_details.txt', 'r')
    # Appending data into the empty list
    for i in available_car_list:
        car_list.append(i.strip("\n").split("|"))
    for j in car_list:
        # Searching User's data
        if j[5] == input_username.upper():
            print("Member        :\t%s" % j[5])
            print("Car Brand     :\t%s" % j[0])
            print("Car Model     :\t%s" % j[1])
            print("Plate Number  :\t%s" % j[2])
            payment_amount = int(int(j[6])*int((j[3])))
            print("Payment       :\tRM%.2f" % payment_amount)
            print("Payment Status:\t%s" % j[7])


# Select Car Function
def select_car(input_username):
    # Keep looping the function until user enter 'X' to exit the function
    while True:
        car_brand = car_brand_choice()
        print()
        # Create empty list for appending details into the list
        car_list = []
        # Opening the car details file
        available_car_list = open('car_details.txt', 'r')
        # Appending data into the empty list
        for i in available_car_list:
            car_list.append(i.strip("\n").split("|"))
        # Show available car details
        for j in car_list:
            if (j[0] == car_brand) and (j[4] == "0"):
                print("Car Brand        :\t%s" % j[0])
                print("Car Model        :\t%s" % j[1])
                print("Plate Number     :\t%s" % j[2])
                print("Charge Per Hour  :\tRM%s.00" % j[3])
                print()
        # Giving option to user to book car or cancel
        book_choice = input("<Enter> to book car ['x' to cancel]:\t")
        try:
            # Proceed to the function if user did not enter 'X' as exit the function
            if book_choice.upper != "X":
                select_choice = input("Enter Car Plate:\t")
                for k in car_list:
                    # Show the car details that users have selected
                    if k[2] == select_choice.upper():
                        print()
                        print("You've booked the car successfully!")
                        print()
                        print("Car Brand        :\t%s" % k[0])
                        print("Car Model        :\t%s" % k[1])
                        print("Plate Number     :\t%s" % k[2])
                        print("Charge Per Hour  :\tRM%s.00" % k[3])
                        # Change data in to booked details
                        k[4] = "1"
                        k[5] = input_username.upper()
                        print("Booking Status   :\tBOOKED")
                        print("Member Booked    :\t%s" % k[5])
                        print()

                # Open file and rewrite the data into file
                car_details = open("car_details.txt", "w")
                for details in car_list:
                    for rewrite in details:
                        # Write each data of the car
                        car_details.write(rewrite)
                        car_details.write("|")
                    # Write each car details into file
                    car_details.write("\n")
                car_details.close()

                # Option on continuing for payment
                proceed_to_payment_choice = input("<Enter> to proceed to payment ['x' to pay later]:\t")
                if proceed_to_payment_choice.upper() != 'X':
                    # Call out payment function
                    payment(input_username)
                else:
                    # Cancel payment
                    break
            # Cancel Booking
            else:
                print("You have cancelled the booking.")
                break
            break
        except:
            # Declare the input whether it is an invalid input
            if type(book_choice) == str and book_choice.upper() != "X":
                print("Invalid Input!!!")
                print("Try Again.")
                continue


# Payment Function
def payment(input_username):
    # Create empty list for appending details into the list
    car_booked_list = []
    # Opening the car details file
    car_list = open('car_details.txt', 'r')
    # Appending data into the empty list
    for i in car_list:
        car_booked_list.append(i.strip("\n").split("|"))
    print()
    print("Member               :\t%s" % input_username)
    # Keep looping the function until user enter 'X' to exit the function
    while True:
        counter = 1
        for j in car_booked_list:
            try:
                # Showing the car details which have paid
                if j[5] == input_username.upper() and j[7] == "PAID":
                    print("-" * 50)
                    print("PAID")
                    print("-" * 50)
                    print("No.%s" % counter)
                    counter = counter + 1
                    print("Car Brand            :\t%s" % j[0])
                    print("Car Model            :\t%s" % j[1])
                    print("Plate Number         :\t%s" % j[2])
                    print("Charge Per Hour      :\tRM%s.00" % j[3])
                    print("Rental Hour(s)       :\t%s" % j[6])
                    payment_amount = int(int(j[3]) * int(j[6]))
                    print("Payment              :\tRM%.2f" % payment_amount)
                    print("Payment Status       :\t%s" % j[7])
                    print()
                # Showing the car details which have not pay
                elif j[5] == input_username.upper() and j[7] == "UNPAID":
                    print("-" * 50)
                    print("UNPAID")
                    print("-" * 50)
                    print("Car Brand            :\t%s" % j[0])
                    print("Car Model            :\t%s" % j[1])
                    print("Plate Number         :\t%s" % j[2])
                    print("Charge Per Hour      :\tRM%s.00" % j[3])
                    # Enter rental hours
                    hour = int(input("Enter Rental Hour(s) :\t"))
                    j[6] = str(hour)
                    payment_amount = int(int(j[6]) * int(j[3]))
                    print("Payment              :\tRM%.2f" % payment_amount)
                    print()
                    # Option on paying now or later
                    payment_choice = input("<Enter> to pay now ['x' to pay later]:\t")
                    if payment_choice.upper != "X":
                        # Change Payment status
                        j[7] = "PAID"
                        print("Payment Status:\t%s" % j[7])
                        # Open file and rewrite the data into file
                        car_details = open("car_details.txt", "w")
                        for details in car_booked_list:
                            for rewrite in details:
                                # Write the each data of the car
                                car_details.write(rewrite)
                                car_details.write("|")
                            # Write each car details into file
                            car_details.write("\n")
                        car_details.close()
                        break

                    else:
                        break

            except:
                print("No record found.")
                break
        break


# Member Page
def member(input_username, input_password, login_details_reference, username_identity):
    # Keep looping the function until user enter 'X' to exit the function
    while True:
        print("-" * 17, "[Member Page]", "-" * 17)
        print(" 1  - Modify Personal Details")
        print(" 2  - Personal Rental History")
        print(" 3  - Cars to be Rented Out Details")
        print(" 4  - Select Car")
        print(" 5  - Payment")
        print("'x' - Exit")
        print("-" * 49)
        # Giving a choice for member to enter the Member Page Number and proceed to respective functions
        member_choice = input("Enter Member Page Number ['x' to exit]:\t")
        try:
            member_choice = int(member_choice)
            if member_choice == 1:
                # Calling out modify personal details function
                modify_member_details(input_username, input_password, login_details_reference, username_identity)
                continue
            elif member_choice == 2:
                # Calling out personal rental history function
                personal_rental_history(input_username)
                continue
            elif member_choice == 3:
                # Calling out available car details function
                print("-" * 17, "[Available Car]", "-" * 17)
                show_car()
                continue
            elif member_choice == 4:
                # Calling out select car function
                select_car(input_username)
                continue
            elif member_choice == 5:
                # Calling out payment function
                payment(input_username)
                continue
        except:
            # Declare the input whether it is an invalid input
            if type(member_choice == str) and (member_choice.upper() != 'X'):
                print()
                print("Invalid Input!!!")
                print("Try Again.")
                continue
            # Exit
            elif type(member_choice) == str and member_choice.upper() == 'X':
                print()
                print("Exit to Home Page.")
                print("-" * 49)
                home_page()


# Login Page
def login_page():
    while True:
        print(" 1 - Admin")
        print(" 2 - Member")
        print("'x' - Exit")
        print()
        login_number_2 = input("Enter the type of login ['X' to exit]:\t")
        try:
            login_number_2 = int(login_number_2)
            if (login_number_2 == 1) or (login_number_2 == 2):
                login()
                break
            elif login_number_2 > 2:
                print("Invalid Input!!!")
                print("Try Again.")
                continue
        except:
            # Error
            if type(login_number_2 == str) and login_number_2.upper() != "X":
                print("Invalid Input!!!")
                print("Try Again.")
                continue
            # Exit
            elif type(login_number_2) == str and login_number_2.upper() == "X":
                break


# Home Page
def home_page():
    while True:
        print("-" * 18, "[Home Page]", "-" * 18)
        print("Welcome To SUPER CAR RENTAL SERVICES (SCRS)")
        print(" 1   - Login [Admin/Member]")
        print(" 2   - View As Customer")
        print("'x'  - Exit")
        print("-" * 49)
        login_number = input("Enter Home Page Number ['x' to exit]:\t")
        try:
            login_number = int(login_number)
            # Admin Page
            if login_number == 1:
                login_page()
                continue

            # Customer Page
            elif login_number == 2:
                print()
                customer()
                continue
            # Error
            else:
                print()
                print("Invalid Home Page Number!!!")
                print("Please Try Again.")
                continue
        except:
            # Error
            if (type(login_number) == str) and (login_number.upper() != 'X'):
                print()
                print("Invalid Home Page Number!!!")
                print("Please Try Again.")
                continue
            # Exit
            elif type(login_number) == str and login_number.upper() == 'X':
                print()
                print("Have a nice day.")
                break
            break


home_page()

import calendar

# Create a dictionary to hold appointments
appointments = {}

# Define a function to add appointments
def add_appointment():
    # Ask the user for the date and time of the appointment
    date = input("Enter the date of the appointment (YYYY-MM-DD): ")
    time = input("Enter the time of the appointment (HH:MM): ")
    
    # Ask the user for the details of the appointment
    details = input("Enter the details of the appointment: ")
    
    # Add the appointment to the dictionary
    appointments[date] = appointments.get(date, []) + [(time, details)]
    
    # Confirm to the user that the appointment has been added
    print("Appointment added.")
    
# Define a function to view appointments
def view_appointments():
    # Ask the user for the date they want to view appointments for
    date = input("Enter the date you want to view appointments for (YYYY-MM-DD): ")
    
    # Get the appointments for the given date, or an empty list if there are none
    appts = appointments.get(date, [])
    
    # Print out the appointments, or a message if there are none
    if appts:
        print("Appointments for {}: ".format(date))
        for appt in appts:
            print("- {} at {}: {}".format(appt[0], date, appt[1]))
    else:
        print("There are no appointments for {}.".format(date))

# Define a function to delete appointments
def delete_appointment():
    # Ask the user for the date and time of the appointment to delete
    date = input("Enter the date of the appointment to delete (YYYY-MM-DD): ")
    time = input("Enter the time of the appointment to delete (HH:MM): ")
    
    # Get the appointments for the given date, or an empty list if there are none
    appts = appointments.get(date, [])
    
    # Find the appointment with the given time, if it exists
    appt = None
    for i in range(len(appts)):
        if appts[i][0] == time:
            appt = i
            break
    
    # If the appointment exists, delete it and confirm to the user that it has been deleted
    if appt is not None:
        del appts[appt]
        appointments[date] = appts
        print("Appointment deleted.")
    else:
        print("There is no appointment at {} on {}.".format(time, date))

# Define a function to display a menu of options
def display_menu():
    print("Appointment Scheduler")
    print("1. Add an appointment")
    print("2. View appointments")
    print("3. Delete an appointment")
    print("4. Exit")

# Define a variable to hold the user's choice
choice = None

# Display the menu and get the user's choice, repeating until they choose to exit
while choice != "4":
    display_menu()
    choice = input("Enter your choice: ")
    
    # Call the appropriate function based on the user's choice
    if choice == "1":
        add_appointment()
    elif choice == "2":
        view_appointments()
    elif choice == "3":
        delete_appointment()
    elif choice == "4":
        print("Exiting...")
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")


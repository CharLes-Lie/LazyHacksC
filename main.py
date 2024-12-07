activities = []

def input_priority():
    valid_priorities = ["High", "Medium", "Low"]
    priority = input("Enter the priority level for this activity (High, Medium, Low): ").capitalize()

    while priority not in valid_priorities:
        print("Invalid priority level! Please enter 'High', 'Medium', or 'Low'.")
        priority = input("Enter the priority level for this activity (High, Medium, Low): ").capitalize()

    return priority

def add_activity():
    for _ in range(int(activity_amount())):
        activity = input("Enter your activity: ")
        time = input("Time for this activity: ")
        activities.append([activity, time])

def activity_amount():
    activity_count = input("How many activities are you participating Today? (Integer)")
    activity_count = test_activities(activity_count)
    
    # Repeat if data provided is invalid
    while not activity_count:
        activity_count = input("How many activities are you participating Today? (Integer)")
        activity_count = test_activities(activity_count)
    
    return activity_count

    
def test_activities(act):

    # Default return to False (invalid entry)
    returnValue = False

    # Check to see if it's empty!
    if act.strip() == "":
        print("SORRY! You forgot to enter your activities!\n")
    # Check to see if it's a number!
    elif not act.isdigit():
        print("SORRY! Your activities should be a positive number above 0.\n")
    elif not (1 <= int(act)):
        print("SORRY! Your grade should be above or equal to 1.\n")
    # If the entry is valid, return the activities
    elif act.isdigit() and int(act) >= 1:
        return int(act)  # Convert to integer before returning


    return returnValue

# def display_activities():
#     print('\nActivities: ')
#     print('Schedule | Activity')
#     print('-------------------')
#     for val, activity in enumerate(activities):
#         print(f'{val + 1} | {activity['Activity']}')

def display_table():
    headers = ['Activity', 'Time']
    print(activities, headers) 
    
def display_table():
    print("Activity       | Time   | Priority")
    print("----------------|--------|---------")
    for activity in activities:
        print(f"{activity[0]:<15}| {activity[1]:<6}| {activity[2]:<8}")
        
'''
while True:
    # print('\n1. Add your activity')
    # print('\n2. Display your activity')
    # print('\n3. Exit')
    activity = input('Enter an activity (or "done" to finish): ')
    if activity.lower() == 'done':
        break
    time = input('Enter the time for the activity: ')
    while time < 1 and time > 12:
        time = input("Enter the time for the activity: ")
    
    add_activitiy(activity, time)
    
    # choice = input('Choose an option: ')
    
    # if choice == '1':
    #     add_activity()
    # elif choice == '2':
    #     display_activities()
    # elif choice '3':
    #     break
    # else:
    #     print('choose a choice from 1-3')
    '''
    
# Function to run the main menu and interact with the user
def main():
    while True:
        print("\n1. Add an activity")
        print("2. Display activities")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            # Ask for activity details
            activity = input("Enter the activity: ")
            time = input("Enter the time for this activity: ")
            priority = input("Enter the priority (High, Medium, Low): ")
            add_activity(activity, time, priority)
        elif choice == '2':
            # Display the list of activities
            display_table()
        elif choice == '3':
            # Exit the program
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
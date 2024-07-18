from datetime import datetime

def display_current_datetime() :
    # Get the current date and time
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print the current date and time
    print("Current date and time:", current_date)

display_current_datetime()

def calculate_future_date():
    number_of_days = int(input('Enter the number of days to add to the current date: '))
     # Get the current date
    current_date = datetime.now().date()
     # Calculate the future date
    future_date = current_date + datetime.timedelta(days=number_of_days)
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f'Future date: {formatted_future_date}')
calculate_future_date()
























# Get the current date and time
##############################
# def display_current_datetime() :
##############################
#     current_date = datetime.datetime.now()
##############################
#     # formatted_current_date

#     # Format the current date and time
#     formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
#     # print(f'Current date and time: {formatted_current_date}')
#     return formatted_current_date

#######################
# display_current_datetime() #done
#######################











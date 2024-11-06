def main():
    # Initialize an empty list to store the daily earnings
    DailyEarn = []
    
    # Loop to get input for each day
    for counter in range(1, 6):
        # Ask the user for the amount earned each day and append it to the list
        amount = float(input(f"Enter the amount earned for day {counter}: "))
        DailyEarn.append(amount)  # Append the input value to the list

    # Print the list of daily earnings
    print(DailyEarn)

# Call the main function to run the program
main()
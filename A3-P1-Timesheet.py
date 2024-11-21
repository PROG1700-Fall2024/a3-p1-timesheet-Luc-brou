#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #W0489720:     
#Student Name: Luc Brousseau 


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    print("Hello! You can use this program to find information about the hours you worked.")

    DailyHours=[] #initializes daily earn variable
    
    for counter in range(1,6): #makes sure only 1-5 are printed for days
       Hours=float(input(f"Enter the hours worked for day {counter}: ")) #input field for daily earnings
       DailyHours.append(Hours) #stores each days earnings 

    for counter in range(5): #checks that number ISN'T negative, ends program if so
        if DailyHours[counter] < 0:
            print("Please enter valid amounts (Cannot be negative).")
            return

    max_hours = DailyHours.index(max(DailyHours)) + 1 #is no "day 0", so adds 1 to initial day value

    print("-------------------------------------------------------------------------------------------------------") 
    print (f"The highest hours worked per day was {max(DailyHours)} hours on day {max_hours}.") #prints highest stored value, and the day associated with it
    print("-------------------------------------------------------------------------------------------------------") 
    
    print (f"All together, you worked {sum(DailyHours)} hours,") #adds all listed values together and prints them
    print(f"With an average of {((sum(DailyHours)) /5)} hours worked per day.") #adds all listed values together and divides them by the amount of days (5)
    print("-------------------------------------------------------------------------------------------------------") 

    print("You worked under 7 hours on:")
    print("")
    for counter in range(5): #prints value in a table list that are lower than 7 dollars
        if DailyHours[counter] <= 7:
            print(f"Day {counter+1}: {(DailyHours[counter])}") #formatted to accept "5.2" (or something like that) hours, otherwise will be rounded to nearest and be wrong.
            found = True
    print("-------------------------------------------------------------------------------------------------------") 
    





    # YOUR CODE ENDS HERE
main()
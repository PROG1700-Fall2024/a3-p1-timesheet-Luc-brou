#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #w0489720:     
#Student Name: Luc Brousseau 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    DailyEarn=[] #initializes daily earn variable
    
    for counter in range(1,6): #makes sure only 1-5 are printed for days
       Earn=float(input(f"Enter the amounter earned for day {counter}: ")) #input field for daily earnings
       DailyEarn.append(Earn) #stores each days earnings 

    for counter in range(5): #checks that number ISN'T negative, ends program if so
        if DailyEarn[counter] < 0:
            print("Please enter valid amounts (Cannot be negative).")
            return

    max_day = DailyEarn.index(max(DailyEarn)) + 1 #is no day 0, so adds 1

    print("-------------------------------------------------------------------------------------------------------") 
    print (f"The highest amount earned per day was ${max(DailyEarn):.2f} dollars on day {max_day}.") #prints highest stored value, and the day associated with it
    print("-------------------------------------------------------------------------------------------------------") 
    
    print (f"All together, you earned ${sum(DailyEarn):.2f} dollars,") #adds all listed values together and prints them
    print(f"With an average of ${(sum(DailyEarn))/5:.2f} dollars earned per day.") #adds all listed values together and divides them by the amount of days (5)
    print("-------------------------------------------------------------------------------------------------------") 

    print("You worked under 7 hours on:")
    print("")
    for counter in range(5): #prints value in a table list that are lower than 7 dollars
        if DailyEarn[counter] <= 7:
            print(f"Day {counter+1}: ${DailyEarn[counter]:.2f}")
            found = True
    print("-------------------------------------------------------------------------------------------------------") 
    





    # YOUR CODE ENDS HERE
main()
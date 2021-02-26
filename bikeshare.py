import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago", "new york city", "washington"]
    months = ["january", "february", "march", "april", "may", "june", "all"]
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]    

    city = input("Please enter a city name. Chose one of these options: chicago, new york city, washington ").lower()
    print(city)
    while city not in cities:

        city = input("The city hasn't been recognized. Please check and type the city input again: ")

    # TO DO: get user input for month (all, january, february, ... , june)

    month = input("Please enter a month from January to June or type All for showing all the content: ").lower()
    print(month)
    while month not in months:
    
        month = input("Try again; please enter a month from January to June or type 'All' for showing all the content: ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
   
    day = input("Please enter a day of the week or type 'all' for showing all the content: ")
    print(day)
    while day not in days:
    
        day = input("Try again; please enter a day from Monday to Sunday or type 'All' for showing all the content: ")
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        
     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]       
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
   
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month    
    if month == "all":
        popular_month = df['month'].mode()[0]
        print('Most Popular Month:', popular_month)
    else:
       print('information not available because you have selected a single month')   

    # TO DO: display the most common day of week
    if day == "all":
        popular_day = df['day_of_week'].mode()[0]
        print('Most popular day of the week:', popular_day) 
    else:
        print('Information not available because you have selected a single day')  

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular hour:', popular_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station    
    print('Most commonly used start station:', df['Start Station'].mode()[0])        

    # TO DO: display most commonly used end station
    print('Most popular destination:', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('Most popular combination of departure and destination station is:',df.groupby(['Start Station','End Station']).size().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = int(df['Trip Duration'].sum() / 60 / 60)
    print("The total travel time is: ", total_travel_time, " hours.")
          
    # TO DO: display mean travel time
    mean_travel_time = int(df['Trip Duration'].mean() / 60)
    print("The mean travel time is: ", mean_travel_time, 'minutes.')
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('this is the counts of user types: ', user_types_count)

    # TO DO: Display counts of gender
    gender_count = df['Gender'].value_counts()
    print('This is the counts of gender: ', gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year_birth = int(df['Birth Year'].min())
    print('This is the earliest year of birth: ', earliest_year_birth)

    most_recent_year_birth = int(df['Birth Year'].max())
    print('This is the most recent year of birth: ', most_recent_year_birth)
   
    most_common_year_birth = int(df['Birth Year'].mode()[0])
    print('This is the most common year of birth: ', most_common_year_birth)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    """Asks user if he wants to view 5 rows of individual trip data. 
    Returns:
    5 rows of individual trip data
    """
    # ask user if he wants to see 5 rows of individual trip data
    view_display = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    # the loop starts here
    while True:        
        # if the user says no the loop end
        if view_display == 'no':
            break
        # if the user says yes 5 rows of individual trip data are displayed
        elif view_display == 'yes' :
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_display = input("Do you wish to continue?: ").lower()
        # if the user doesn't type 'yes' or 'no' he's asked to do so until the correct input is provided
        else:
            view_display = input("Unrecognized answer. Please type 'yes' or 'no'").lower()        


def main():
    """Main function"""
    while True:
        city, month, day = get_filters()        
        df = load_data(city, month, day)
        time_stats(df, month, day)        
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

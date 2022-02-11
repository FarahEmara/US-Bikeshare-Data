import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city = ['washington', 'chicago', 'new york city']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Specify a city. (chicago, new york city, washington)\n").lower()
    
    while city not in CITY_DATA.keys():
        print("Invalid input. Please choose from the specified cities.")
        
        city = input("Specify a city. (chicago, new york city, washington)\n").lower()
    # TO DO: get user input for month (all, january, february, ... , june)    
    month = input("Specify a month (january,february,march,april,may,june) or type all to view data of all months.\n").lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
        
    while month not in months and month != 'all':
        print("Invalid input. Please choose a valid month.")
            
        month = input("Specify a month, or type all to view each month\'s data.\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Specify a day (sunday,monday,tuesday,wednesday,thursday,friday,saturday) or type all to view data of all days.\n").lower()
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    
    while day not in days and day != 'all':
        print("Invalid input. Please choose a valid day.")
            
        day = input("Specify a day (sunday,monday,tuesday,wedensday,thursday,friday,saturday) or type all to view data of all days.\n").lower()   
    
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month']==month]
        
    if day != 'all':
            
        df = df[df['day_of_week'].str.startswith(day.title())]
               
    return df

def raw_data(df):
    current = 4
    while True: 
        ask_user = input('Would you like to display the next 5 lines of data? (yes/no)').lower()
        if ask_user == 'yes':             
            print(df.iloc[current:current+5])
            current+=5
        elif ask_user == 'no': 
            break 
            
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
            
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most commmon month is : {}'.format(df['month'].mode()[0]))  
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of the week for riding is', common_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    
    popular_hour = df['hour'].mode()[0]
    print('Most popular start hour is', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most commonly used start station is', common_start)
    
    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most common end station is', common_end)
    
    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = (df['Start Station'] + df['End Station']).mode()[0]
    print('Most common combination of start and end station is', common_start_end)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print('Total travel time is', total)
    
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time is', mean_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    types_counts = df['User Type'].value_counts()
    print('The counts of user types are:\n', types_counts)
    
    # TO DO: Display counts of gender
    if city == 'washington':
        print('This type of data is not provided for this city.')
        
    else:
        
        gender_counts = df['Gender'].value_counts()
        print('By gender, our users\' counts are:\n', gender_counts) 
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print('This type of data is not provided for this city.')
        
    else:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('The earliest, most recent, and most common year of birth, respectively are: {},{} and {}.'.format(earliest,recent,common_year))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def main():
   while True:
       city, month, day = get_filters()
       print(city, month, day)
       df = load_data(city, month, day)
       print(df.head()) 
       raw_data(df)
       time_stats(df)
       station_stats(df)
       trip_duration_stats(df)
       user_stats(df)

       restart = input('\nWould you like to restart? Enter yes or no.\n')
       if restart.lower() != 'yes':
           break


if __name__ == "__main__":
	main()
       
        
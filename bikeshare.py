import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities=('chicago','new york city','washington')
months=('january','february','march','april','may','june', 'all')
days=('sunday','monday','tuesday','wednesday','thursday','friday','saturday','all')
def get_filters():
   
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Enter a city from those cities (Chicago,New York City,Washington) \n').lower()
        if city not in cities: #check if the input is valid
            print('This input is invalid please enter a valid one')
            continue
        else:
            break
        

    # get user input for month (all, january, february, ... , june)
    while True:
        month=input('Enter a month from January to June or type all to view all months \n').lower()
        if month not in months: #check if the input is valid
            print('This input is invalid please enter a valid one')
            continue
        else:
            break

    #get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Enter a day from Monday to Sunday or type all to view all weeks \n').lower()
        if day not in days: #check if the input is valid
            print('This input is invalid please enter a valid one')
            continue
        else:
            break

    print('-'*40)
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
    #we will load the data into a dataframe
    df=pd.read_csv(CITY_DATA[city])
    #to convert the start time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])
    #extract month from Start Time in order to make new column
    df['month']=df['Start Time'].dt.month
    #extract day_of_week from Start Time in order to make new column
    df['day_of_week']=df['Start Time'].dt.weekday_name
    
    if month != 'all':
        The_months=['january','february','march','april','may', 'june']
        month=The_months.index(month) + 1
        df=df[df['month']==month]

    if day != 'all':
        df=df[df['day_of_week']==day.title()]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month =df['month'].mode()[0]
    print('The most common  month is : ', popular_month)

    # display the most common day of week
    popular_day =df['day_of_week'].mode()[0]
    print('The most common  day is : ',popular_day)


    #display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    popular_hour =df['hour'].mode()[0]
    print('The most common hour of day is : ',popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station =df['Start Station'].mode()[0]
    print('The popular start station is : ', popular_start_station)


    # display most commonly used end station
    popular_end_station =df['End Station'].mode()[0]
    print('The popular end station is : ',popular_end_station )

    # display most frequent combination of start station and end station trip
    popular_start_end_station=(df['Start Station'] + ' and ' + df['End Station']).mode()[0]
    print('The popular start and end station is : ',popular_start_end_station )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=sum(df['Trip Duration'])
    print('Total travel time is :',total_travel_time)


    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean travel time is :',mean_travel_time)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('The Counts of user types is :',df['User Type'].value_counts())


    #  Display counts of gender
    try:
        print('The Counts of Gender is :',df['Gender'].value_counts())
    except:
        print('there is no data for Gender in this city')

    # Display earliest, most recent, and most common year of birth
    try:
        The_earlist_year=df['Birth Year'].min()
        print('The Earlist Year is : ', The_earlist_year)
        The_most_recent_year=df['Birth Year'].max()
        print('The Most Recent Year is : ',The_most_recent_year)
        The_most_common_year=df['Birth Year'].mode()[0]
        print('The Most Common  Year is : ',The_most_common_year)
    except:
        print('there is no data for birth year in this city')
    




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_display(df): #display row data to user if he want
    ans=input('do you want to display 5 rows from the data? (yes/no) \n').lower()
    k=0
    while True :
        if ans == 'no':
            break
        if ans == 'yes':
            print(df[k:k+5])    #to print a slice containing 5 rows from the data frame
            ans=input('do you want to display another 5 rows ? (yes/no) \n').lower()    
            k+=5
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

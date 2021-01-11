import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
Filter_list = ['both','month','day','none']
Months=['january','february','march','april','may','june']
Days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
def get_filters():
    Filter_items=[]
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('Would you like to see data for chicago, new york city, or washington?\n')
    while(city not in CITY_DATA.keys()):
        try:
            print('invalid input, thanks to choose one of these cities:chicago,new york city,washington')
            city=input('Would you like to see data for?\n chicago\n new york city\n washington\n')
            if(city in CITY_DATA.keys()):
                Filter_items.append(city)
                break    
        except KeyboardInterrupt:
            print('wrong type\n the program will continue\n')
    Filter_items.append(city)
    if(len(Filter_items)==2):
        Filter_items.remove(Filter_items[1])  
    Filter=input('Would you like to filter the data by:\n month\n day\n both\n or not at all?enter none for no time filter\n')
    while(Filter not in Filter_list or Filter in Filter_list):
        if(Filter in Filter_list):
            if(Filter== 'both'):
                # TO DO: get user input for month (all, january, february, ... , june)
                month=input('Which month do you want?\njanuary\n february\n march\n april\n may\n june\n , type your choice correctly\n')
                while(month not in Months):
                    try:
                        print('invalid input\n')
                        month=input('Which month do you want?\njanuary\n february\n march\n april\n may\n june\n  type your choice correctly\n')
                        if(month in Months):
                            Filter_items.append(month)
                            break
                    except KeyboardInterrupt:
                        print('wrong type\n the program will continue\n')
                    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
                day=input('Which day do you want?\n monday\n tuesday\n wednesday\n thursday\n friday\n saturday\n sunday\n all\n type your choice correctly\n')
                while(day not in Days):
                    try:
                        print('invalid input\n')
                        day=input('Which day do you want?\n monday\n tuesday\n wednesday\n thursday\n friday\n saturday\n sunday\n all\n type your choice correctly\n')
                        if(day in Days):
                            Filter_items.append(day)
                            break
                    except KeyboardInterrupt:
                        print('wrong type\n the program will continue\n')
                if(month not in Filter_items and day not in Filter_items):
                    Filter_items.extend([month,day])
                elif(month not in Filter_items):
                    Filter_items.insert(1,month)
                elif(day not in Filter_items):
                    Filter_items.append(day)
                break
            elif(Filter== 'month'):
                # TO DO: get user input for month (all, january, february, ... , june)
                month=input('Which month do you want?\njanuary\n february\n march\n april\n may\n june\n all\n type your choice correctly\n')
                while(month not in Months):
                    try:
                        print('invalid input\n')
                        month=input('Which month do you want?\njanuary\n february\n march\n april\n may\n june\n all\n type your choice correctly\n')
                        if(month in Months):
                            Filter_items.append(month)
                            break
                    except KeyboardInterrupt:
                        print('wrong type\n the program will continue\n')        
                day= 'all'
                if(month not in Filter_items):
                    Filter_items.insert(1,month)
                    Filter_items.append(day)
                elif(month in Filter_items):
                    Filter_items.append(day)
                else:
                    Filter_items.extend([month,day])
                break
            elif(Filter== 'day'):
                # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
                month='all'
                day=input('Which day do you want?\n monday\n tuesday\n wednesday\n thursday\n friday\n saturday\n sunday\n all\n type your choice correctly\n')
                while(day not in Days):
                    try:
                        print('invalid input\n')
                        day=input('Which day do you want?\n monday\n tuesday\n wednesday\n thursday\n friday\n saturday\n sunday\n all\n type your choice correctly\n')
                        if(day in Days):
                            Filter_items.append(day)
                            break
                    except KeyboardInterrupt:
                        print('wrong type\n the program will continue\n')        
                if(day not in Filter_items):
                    Filter_items.insert(1,month)
                    Filter_items.append(day)
                elif(day in Filter_items):
                    Filter_items.insert(1,month)
                else:
                    Filter_items.extend([month,day])
                    
                break
            elif(Filter== 'none'):
                month='all'
                day= 'all'
                Filter_items.extend([month,day])
                break
        else:
            print('invalid input\n')
            Filter=input('thanks to type the right type of filter for your data: ')  
    print('-'*40)
    return Filter_items#city, month, day


def load_data(Filter_items):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[ Filter_items[0] ])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name 
    if(Filter_items[1] != 'all'):
            months=['january','february','march','april','may','june']
            Filter_items[1]=months.index(Filter_items[1])+1
            df=df[df['month']==Filter_items[1]]      
    if(Filter_items[2] != 'all'):
            df=df[df['day_of_week']==Filter_items[2].title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months=['january','february','march','april','may','june']
    most_common_month= months[int(df['month'].mode())-1]
    print('the most common month is\n',most_common_month)
    # TO DO: display the most common day of week
    print('the most common day of week is\n',df['day_of_week'].mode()[0])   
    # TO DO: display the most common start hour
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['hour']=df['Start Time'].dt.hour
    print('the most common start hour is\n',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most commonly used start station is \n',df['Start Station'].mode()[0])
    # TO DO: display most commonly used end station
    print('most commonly used end station is \n',df['End Station'].mode()[0])
    # TO DO: display most frequent combination of start station and end station trip
    df['most common trip from start to end'] = df['Start Station'] +' : '+ df['End Station']
    print('most common trip from start to end is \n',df['most common trip from start to end'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    duration=df['Trip Duration'].sum()
    print(duration)
    trip_duration=time_convert(duration)
    print('total travel time is dd:hh:mm:ss\n',trip_duration)

    # TO DO: display mean travel time
    print('mean travel time is dd:hh:mm:ss\n',time_convert(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
      
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    print('counts of user types is\n',df['User Type'].value_counts())
    try:
        # TO DO: Display counts of gender
        print('counts of gender is\n',df['Gender'].value_counts())
        # TO DO: Display earliest, most recent, and most common year of birth
        print('the earliest year of birth is\n',int(df['Birth Year'].min()))
        print('the most common year of birth is\n',int(df['Birth Year'].mode()))
        print('the most recent year of birth is\n',int(df['Birth Year'].max()))
    except KeyError:
        print('the info counts of gender and the most common year of birth are not specified in washington\n')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_row_data(Flter_item):
    choose = input('Do you want to display 5 raw data?\n y or n \n')
    filename=pd.read_csv(CITY_DATA[Flter_item[0]],chunksize=5)
    while(choose=='y'):
        for chunk in (filename):
            print(chunk)
            choose = input('Do you want to display 5 raw data?\n y or n \n')
            if(choose != 'y'):
                break
        break
def time_convert(duration):
    days= duration//(24*3600)
    duration = duration %(24*3600)
    hours=duration//3600
    duration= duration%3600
    minutes=duration//60
    duration=duration%60
    seconds=duration
    total_time= str(days) + ':' + str(hours) + ':' + str(minutes) + ':' + str(seconds)
    return total_time
    
    
def main():
    while True:
        Flter_item = get_filters()
        df = load_data(Flter_item)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_row_data(Flter_item)
        restart = input('\nWould you like to restart? Enter y or n.\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()

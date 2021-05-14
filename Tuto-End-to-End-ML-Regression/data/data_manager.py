import pandas as pd


def get_numeric_state_holidays(df):
    State_holiday_list = df["State_holiday"].map({
        "0": 0,
        "a": 1,
        "b": 2,
        "c": 3,
    })
    State_holiday_list = pd.DataFrame(State_holiday_list)

    return State_holiday_list


## CODE ##

columns = [
    'Store_ID',
    'Day_of_the_week',
    'Date',
    'Nb_customers',
    'Open',
    'Promotion',
    'State_holiday',
    'School_holiday']

# import the data set
df_train = pd.read_csv('store_train.csv', sep=' ',
                       names=columns)  # This is the X

# Get unique data types
print('Unique types of variables in the data set are:', df_train.dtypes.unique())

# Get only numeric data
df_train['State_holiday'] = get_numeric_state_holidays(df_train)

# Write the file
df_train.to_csv('clean_store_train.csv', index=False, sep=' ')

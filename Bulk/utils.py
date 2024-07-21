# utils.py
import datetime
import pandas as pd





import pandas as pd
import datetime



def process_calendar_year(df, product_name):
    def week_to_date(year, week):
        return datetime.datetime.strptime(f'{year} {week} 1', '%G %V %u')

    df['date_1'] = df.apply(lambda row: week_to_date(row['marketingYear'], row['week']), axis=1)
    df['date'] = df['date_1'].dt.to_period('M').dt.to_timestamp()
    monthly_data = df.groupby('date')['kgEquivalent'].sum().reset_index()
    monthly_data['kgEquivalent'] = monthly_data['kgEquivalent'] / 1000
    monthly_data = monthly_data.rename(columns={'kgEquivalent': f'TAXUD_{product_name}'})
    
    return monthly_data




def process_crop_year(df, product_name):
    # Function to map marketing year week to crop year week
    def map_week(marketing_year_week):
        if 1 <= marketing_year_week <= 26:
            return marketing_year_week + 26
        elif 27 <= marketing_year_week <= 52:
            return marketing_year_week - 26
        else:
            return None
    
    # Apply map_week to the 'week' column
    df['week'] = df['week'].apply(lambda x: map_week(int(x)) if pd.notnull(x) else x)
    
    # Function to get calendar year from crop year and week
    def get_calendar_year(crop_year, week):
        if pd.isnull(week):
            return None
        start_year, end_year = map(int, crop_year.split('/'))
        if week <= 26:
            return end_year
        else:
            return start_year
    
    # Apply get_calendar_year to each row
    df['calendarYear'] = df.apply(lambda row: get_calendar_year(row['marketingYear'], row['week']), axis=1)
    
    # Function to convert year and week to date
    def week_to_date(year, week):
        if pd.isnull(year) or pd.isnull(week):
            return None
        return datetime.datetime.strptime(f'{int(year)} {int(week)} 1', '%G %V %u')
    
    # Apply week_to_date to each row
    df['date_1'] = df.apply(lambda row: week_to_date(row['calendarYear'], row['week']), axis=1)
    df['date'] = df['date_1'].dropna().dt.to_period('M').dt.to_timestamp()
    
    # Group by 'date' and sum 'kgEquivalent', then convert to thousands and rename the column
    monthly_data = df.groupby('date')['kgEquivalent'].sum().reset_index()
    monthly_data['kgEquivalent'] = monthly_data['kgEquivalent'] / 1000
    monthly_data = monthly_data.rename(columns={'kgEquivalent': f'TAXUD_{product_name}'})
    
    return monthly_data




years_filtered = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json"
    }

Y_mapping = [
    {
        'name': 'Animal Fats (Other)', 
        'sector': 'Oilseeds', 
        'year': 'calendar', 
        'HS codes': 'cn8ProductCodes=04021011&cn8ProductCodes=04021019&cn8ProductCodes=04021091&cn8ProductCodes=04021099'
    },
    {
        'name': 'Animal Fats & Oils', 
        'sector': 'Oilseeds', 
        'year': 'calendar', 
        'HS codes': 'cn8ProductCodes=04021011&cn8ProductCodes=04021019&cn8ProductCodes=04021091&cn8ProductCodes=04021099'
    },
    {
        'name': 'Animal, Vegetable Fats & Oils', 
        'sector': 'Oilseeds', 
        'year': 'calendar', 
        'HS codes': 'cn8ProductCodes=04021011&cn8ProductCodes=04021019&cn8ProductCodes=04021091&cn8ProductCodes=04021099'
    },

]

X_mapping = [
    {
        'name':'Animal Fats (Other)',
        'X_code': '040210'    
    },
    {
        'name':'Animal Fats & Oils',
        'X_code': '040210'    
    },
    {
        'name':'Animal, Vegetable Fats & Oils'
        'X_code': '040210'    
    }

]


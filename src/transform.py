import pandas as pd
from datetime import datetime, timedelta

def get_value(raw_str: str, sep: list) -> str:
    """
    Finds value searched for
    """
    in_value = False
    value = ''
    
    for char in raw_str:
        if char in sep:
            if in_value:
                break
            else:
                in_value = True
        if in_value:
            value += char
    
    return value[1:]

def get_data(source : str):
    """
    Scraps data wanted from txt source
    """
    trg_columns = ['sort', 'Name', 'PriceDiscount', 'Price', 'Rating', 'EndsIn', 'Started', 'Release']
    df_table = pd.DataFrame(columns = trg_columns)
    game = []

    for i in range(len(source)):
        if source[i:i+9] == 'class="b"':
            game.append(get_value(source[i+11:i+110], ['>', '<']))
        if source[i:i+10] == 'data-sort=':
            game.append(get_value(source[i+10:i+22], ['"']))
        if len(game) == 8:
            df_table = pd.concat([df_table, pd.DataFrame([game], columns = trg_columns)], 
                                axis = 0,
                                ignore_index=True)
            game = []

    df_table = df_table.drop(columns = 'sort')

    return df_table

def calculate_ends_in(x):
    x = datetime.fromtimestamp(int(x)) - datetime.now()
    return str(x.days) + ' days'
    
def calculate_started(x):
    x = datetime.now() - datetime.fromtimestamp(int(x))
    return str(x.days) + ' days'

def calculate_release(x):
    x = datetime.fromtimestamp(int(x)) + timedelta(days=1)
    return str(x.date())

def transform_data(df_table):
    df_table['PriceDiscount'] = df_table['PriceDiscount'].astype(int)
    df_table['Price'] = df_table['Price'].apply(lambda x: float(x)/100)
    df_table['Rating'] = df_table['Rating'].astype(float)
    df_table['EndsIn'] = df_table['EndsIn'].apply(calculate_ends_in)
    df_table['Started'] = df_table['Started'].apply(calculate_started)
    df_table['Release'] = df_table['Release'].apply(calculate_release)

    return df_table
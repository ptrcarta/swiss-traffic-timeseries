import os
import pandas as pd
import numpy as np


DATA_DIR = 'data/'
def extract_data(table):
    is_date = table.applymap(lambda c: type(c) is pd.datetime)
    rows = is_date.idxmax(axis='rows').values
    rows_nonzero = rows[rows != 0]
    # check all are equal
    assert (rows_nonzero[1:] == rows_nonzero[0]).all()
    date_row = rows_nonzero[0]
    data_cols = rows != 0
    dates = table.iloc[date_row, data_cols].values
    # as labels we take the counting station number
    labels = [int(lbl) for lbl in table.iloc[date_row+1:,0].values]
    data = table.iloc[date_row + 1:, data_cols]
    data.set_axis(labels, axis=0, inplace=True)
    data.set_axis(dates, axis=1, inplace=True)
    return data

def load_files():
    tables = []
    for filename in os.listdir(DATA_DIR):
        if '.xls' in filename:
            tables.append(pd.read_excel(DATA_DIR + filename, sheet_name=2))
    return tables

def load_timeseries():
    tables = load_files()
    dfs = [extract_data(table) for table in tables]
    df = dfs[0].join(dfs[1:], how='outer')
    dates = df.columns
    sorted_dates = dates.sort_values()
    return df[sorted_dates].astype(np.float64).T

def load_description():
    ### TODO use metadata file
    table = pd.read_excel(
            DATA_DIR +\
                'meta/2019 01 14 Liste compteurs pour  Swisstopo VDE.xlsx',
            sheet_name=0, index_col = 0, headers = 0
    )
    return table

# TODO check wrong dates

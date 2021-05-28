from pandas.core.frame import DataFrame
import numpy as np
import pandas as pd

def main(df_anon: DataFrame , df_orig: DataFrame, footprint: DataFrame):
    df = df_anon.copy()
    df_original_reduced = df_orig.copy()

    df = df.drop(columns=['longitude', 'latitude'])
    df_original_reduced = df_original_reduced.drop(columns=['longitude', 'latitude'])

    # Convert date to year-week
    df['date'] = df['date'].dt.year.astype(str) + "-" + df['date'].dt.week.astype(str)
    df_original_reduced['date'] = df_original_reduced['date'].dt.year.astype(str) + "-" + df_original_reduced['date'].dt.week.astype(str)


    # Group by user and week number
    df = df.groupby(['id','date']).size().reset_index(name='count')
    df_original_reduced = df_original_reduced.groupby(['id','date']).size().reset_index(name='count')

    # Join the two Dataframes on the number of times an id is found each week
    df = pd.merge(df_original_reduced, df, on=['date', 'count'], how='left')
    df = df.drop(columns=['count'])
    df = df.groupby(['date', 'id_x'])['id_y'].apply(list)
    weeks = df.reset_index()['date'].unique().tolist()
    df = df.reset_index().set_index(['id_x', 'date']).unstack('date')
    df.columns = weeks

    # Compare the two footprints and create score
    df = (df == footprint)
    df = df.astype(int) # convert true and falses to 1/0
    score = df.to_numpy().sum()
    values = footprint.fillna(0).astype('bool').to_numpy().sum() # sum of each non Nan values

    return score / values

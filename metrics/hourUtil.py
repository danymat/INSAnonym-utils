import pandas as pd
import numpy as np

def main(df_anon, df_original, params, nb_orig_lines):
    hourdec = [1, 0.9, 0.8, 0.6, 0.4, 0.2, 0, 0.1, 0.2, 0.3, 0.4, 0.5,
               0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0, 0.2, 0.4, 0.6, 0.8, 0.9]

    df = df_anon.copy()
    df_original_reduced = df_original.copy()

    # Recreate df with relevant values
    df = pd.DataFrame({
        'df_hour': df['date'].dt.hour,
        'df_origin_hour': df_original_reduced['date'].dt.hour
    })

    # Keep only rows that changed hours
    filter = abs(df['df_hour'] - df[ 'df_origin_hour']) >= 1
    df = df.loc[filter] 

    # Substract 0.1 points per hour (even if days are identical)
    df['diff_hour'] = df['df_hour'] - df['df_origin_hour']
    df['score'] = df['diff_hour'].apply(lambda x: hourdec[x])
    score = df['score'].sum()
    return ((nb_orig_lines - len(df)) + score) / nb_orig_lines


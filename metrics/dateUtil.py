from datetime import date

import pandas as pd

def main(df_anon, df_original, params, nb_orig_lines):
    df = df_anon.copy()
    df_original_reduced = df_original.copy()

    # Verify if the weeks are the same
    df_week = df['date'].dt.isocalendar().week 
    df_original_week = df_original_reduced['date'].dt.isocalendar().week
    if not pd.Series(df_week == df_original_week).all():
        raise Exception("Weeks must be the same")

    # Recreating playground dataframe with only relevant values
    df = pd.DataFrame({
        'df_day': df['date'].dt.day,
        'df_origin_day': df_original_reduced['date'].dt.day
    })
    df['df_diff_day'] = abs(df['df_day'] - df['df_origin_day'])

    # Creating score
    max = df[['df_day', 'df_origin_day']].max(axis=1)
    min = df[['df_day', 'df_origin_day']].min(axis=1)
    df['calculus'] = abs(max - min + 7)
    df['score'] = 1 - df[['df_diff_day', 'calculus']].min(axis=1) / 3
    score = df['score'].sum()
    return ((nb_orig_lines - len(df)) + score) / nb_orig_lines

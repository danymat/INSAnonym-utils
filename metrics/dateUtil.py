import pandas as pd

def main(df_anon, df_original, params, nb_orig_lines):
    df = df_anon.copy()
    df_original_reduced = df_original.copy()
    
    # Verify if the weeks are the same
    if not (df['date'].dt.isocalendar().week == df_original_reduced['date'].dt.isocalendar().week).all():
        raise Exception("Weeks must be the same")

    df_score = 3 - abs(df.date.dt.dayofweek - df_original_reduced.date.dt.dayofweek)

    return df_score.loc[df_score > 0].sum() / 3 / nb_orig_line

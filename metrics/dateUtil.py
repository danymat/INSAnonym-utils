import pandas as pd

def main(df_anon, df_original, params, nb_orig_lines):
    # Verify if the weeks are the same
    if not (df_anon['date'].dt.isocalendar().week == df_original['date'].dt.isocalendar().week).all():
        raise Exception("Weeks must be the same")

    df_score = 3 - abs(df_anon.date.dt.dayofweek - df_original.date.dt.dayofweek)

    return df_score.loc[df_score > 0].sum() / 3 / nb_orig_line

import dateUtil
import hourUtil
import utility_distance
import utility_meet
import utility_POI
import utility_tuile

import pandas as pd
import subprocess
import argparse

def remove_del(df):
    df.loc[df['id'] != "DEL"]
    # self.df_origin_del = self.df_origin.loc[self.df_anon.index]
    return df


def open_dataframe(arg):
    file = open(arg)
    df = pd.read_csv(file, delimiter='\t', header=None)
    # Change types
    df.columns = ['id', 'date', 'latitude', 'longitude' ]
    df['date'] = pd.to_datetime(df['date'])
    df['id'] = df['id'].astype('category')
    df['latitude'] = df['latitude'].astype('category')
    df['longitude'] = df['longitude'].astype('category')
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("anonymized", help="Anonymized Dataframe filename")
    parser.add_argument("original", help="Original Dataframe filename")
    parser.add_argument("script", help="Script to use for testing",
        choices=['dateUtil', 'hourUtil', 'utility_distance', 'utility_meet', 'utility_POI', 'utility_tuile'] )
    args = parser.parse_args()

    df_origin = open_dataframe(args.original)
    df_anon = open_dataframe(args.anonymized)
    size_df = len(df_origin)

    df_anon = df_anon.loc[df_anon['id'] != "DEL"]
    if args.script in ["utility_tuile", "utility_POI"]:
        df_origin = df_origin.loc[df_anon.index]

    score = 0

    if (args.script == "dateUtil"):
        score = dateUtil.main(df_anon, df_origin, {}, size_df)
    elif args.script == "hourUtil":
        score = hourUtil.main(df_anon, df_origin, {}, size_df)
    elif args.script == "utility_distance":
        score = utility_distance.main(df_anon, df_origin, {"dx":0.1}, size_df)
    elif args.script == "utility_meet":
        score = utility_meet.main(df_anon, df_origin, {"size":2, "pt":0.1}, size_df)
    elif args.script == "utility_POI":
        score = utility_POI.main(df_anon, df_origin, {"size":2,"nbPOI":3,"night_start":22,"night_end":6,"work_start":9,"work_end":16,"weekend_start":10,"weekend_end":18} , size_df)
    elif args.script == "utility_tuile":
        score = utility_tuile.main(df_anon, df_origin, {"size":2}, size_df)
    else:
        print("No script run. Exiting...")
        exit()

    print(score)

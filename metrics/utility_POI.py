import pandas as pd
import numpy as np


#######################################
# --- Taille des points d'intérêts ---#
#######################################
# size = 2
# 4 : cellule au mètre
# 3 : cellule à la rue
# 2 : cellule au quartier
# 1 : cellule à la ville
# 0 : cellule à la région
# -1 : cellule au pays

######################################
# --- Nb de POI à vérifier par ID ---#
######################################
# nbPOI = 3
# 3: Vérification des 3 POI les plus fréquentés en terme de temps de présence.

################################
# --- Définition des heures ---#
################################
# Détection des POI -nuit, travail et weekend- durant les heures suivantes:
# night_start, night_end = 22, 6
# De 22h00 à 6h00
# work_start, work_end = 9, 16
# De 9h00 à 16h00
# weekend_start, weekend_end = 10, 18

def main(df_anon, df_original, params, nb_orig_lines):
    global size, nbPOI, night_start, night_end, work_start, work_end, weekend_start, weekend_end
    size = params['size']
    nbPOI = params['nbPOI']
    night_start = pd.to_datetime(params['night_start'], format="%H").strftime("%H:%M")
    night_end = pd.to_datetime(params['night_end'], format="%H").strftime("%H:%M")
    work_start = pd.to_datetime(params['work_start'], format="%H").strftime("%H:%M")
    work_end = pd.to_datetime(params['work_end'], format="%H").strftime("%H:%M")
    weekend_start = pd.to_datetime(params['weekend_start'], format="%H").strftime("%H:%M")
    weekend_end = pd.to_datetime(params['weekend_end'], format="%H").strftime("%H:%M")
    ids = df_original['id'].unique()
    df = df_anon.copy()
    df_orig = df_original.copy()

    # Need to set index as date to use between_time
    df_orig.index = pd.DatetimeIndex(df_orig['date']) 
    df.index = pd.DatetimeIndex(df['date']) 

    def conditions(df):
        return [
            (df['date'].dt.dayofweek < 4) & (df.index.isin(df.between_time(night_start, night_end, include_start=False, include_end=False).index)),
            (df['date'].dt.dayofweek < 4) & (df.index.isin(df.between_time(work_start, work_end, include_start=False, include_end=False).index )),
            (df['date'].dt.dayofweek >= 4) & (df.index.isin(df.between_time(weekend_start, weekend_end, include_start=False, include_end=False).index ))
        ]

    # Add metadata for days and drop non special rows
    values = ['NIGHT', 'WORK', 'WEEKEND']
    df_orig['time'] = np.select(conditions(df_orig), values, None)
    df['time'] = np.select(conditions(df), values, None)
    df = df.dropna(subset=['time'])
    df_orig = df_orig.dropna(subset=['time'])

    # Converting longitude and latitude as float 
    df = df.astype({'longitude': 'float64', 'latitude': 'float64', 'id': 'int64'})
    df_orig = df_orig.astype({'longitude': 'float64', 'latitude': 'float64', 'id': 'int64'})
   
    # Round lat,long with size
    df['latitude'] = df['latitude'].round(size)
    df['longitude'] = df['longitude'].round(size)
    df_orig['latitude'] = df_orig['latitude'].round(size)
    df_orig['longitude'] = df_orig['longitude'].round(size)

    # Sum the time spend on each unique in marked territory location
    # Based on https://stackoverflow.com/questions/64177814/how-to-find-time-spent-at-each-location-in-a-panda-dataframe
    df,df_orig = sumTimeLocations([df, df_orig])
    # Retrieve the 3 greatest POI for each ID for each type
    df,df_orig = getGreatestPOIs([df, df_orig], values)

    df,df_orig = changeType([df, df_orig])
    
    df = pd.merge(df,df_orig, on=['id', 'latitude', 'longitude', 'time'], how='right')

    # Create score between 0 and 1 for each POI
    df['score'] = df.apply(createScore, axis=1)

    score = df['score'].sum()
    return score / len(df)


def sumTimeLocations(dfs):
    for i,df in enumerate(dfs):
        df['moved'] = (df['latitude']!=df['latitude'].shift())&(df['longitude']!=df['longitude'].shift()) 
        df['segment'] = df['moved'].cumsum() # true, false, false,... true is one segment
        df = pd.concat([df, df.groupby('segment').transform('first')[['date']].rename(columns={'date': 'date_start'})], axis=1)
        df['delta'] = df['date']-df['date_start']
        df = df.groupby(by='segment').max().loc[:, ['id', 'latitude', 'longitude', 'delta', 'time']]
        df = df.groupby(['id', 'latitude', 'longitude', 'time']).agg({ 'delta': 'sum'}).reset_index()
        dfs[i] = df
    return dfs

def getGreatestPOIs(dfs, values):
    for i,df in enumerate(dfs):
        results = pd.DataFrame()
        ids = df['id'].unique()
        for id in ids:
            for metadata in values:
                group = df.groupby('id').get_group(id).groupby('time')
                if metadata in group.groups.keys():
                    df_metadata = group.get_group(metadata).nlargest(size, 'delta')
                    results = results.append(df_metadata)
        dfs[i] = results
    return dfs

def createScore(row):
    if pd.isnull(row['delta_x']) or pd.isnull(row['delta_y']): 
        score = 0
    elif row['delta_x'] == pd.Timedelta(0) and row['delta_y'] == pd.Timedelta(0) :
        score = 1
    elif row['delta_y'] - row['delta_x'] > pd.Timedelta(0):
        score = row['delta_x'] / row['delta_y']
    else:
        score = row['delta_y'] / row['delta_x']
    return score

def changeType(dfs):
    for i,df in enumerate(dfs):
        df['id'] = df['id'].astype(str)
        dfs[i] = df
    return dfs

import pandas as pd

def main(df_anon, df_original, params, nb_orig_lines):
    size = params['size']

    df = df_anon.copy()
    df_orig = df_original.copy()

    # Converting longitude and latitude as float 
    df = df.astype({'longitude': 'float64', 'latitude': 'float64', 'id': 'int64' })
    df_orig = df_orig.astype({'longitude': 'float64', 'latitude': 'float64', 'id': 'int64'})

    # Round lat,long with size
    df['latitude'] = df['latitude'].round(size)
    df['longitude'] = df['longitude'].round(size)
    df_orig['latitude'] = df_orig['latitude'].round(size)
    df_orig['longitude'] = df_orig['longitude'].round(size)

    # Group each position for ids and retrieve the count of unique position
    df = df.groupby(['id','latitude','longitude']).size().reset_index(name='count')
    df_orig = df_orig.groupby(['id','latitude','longitude']).size().reset_index(name='count')
    df = df.groupby(['id']).size().reset_index(name='count')
    df_orig = df_orig.groupby(['id']).size().reset_index(name='count')

    df = pd.merge(df_orig, df, on=['id'], how='left')
    df['score'] = df.apply(createScore, axis=1)
    score = df['score'].sum()
    return score / len(df)

def createScore(row):
    if pd.isnull(row['count_x']) or pd.isnull(row['count_y']): 
        score = 0
    elif row['count_x'] > row['count_y']:
        score = row['count_y'] / row['count_x']
    else:
        score = row['count_x'] / row['count_y']
    return score

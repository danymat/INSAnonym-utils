def calcul_utility(diff):
    score = diff*(-1/dx) + 1
    if(score < 0):
        return 0
    return score

def main(df_anon, df_original, params, nb_orig_lines):
    global dx
    dx = params['dx']

    df = df_anon.copy()
    df_original_reduced = df_original.copy()

    # Converting longitude and latitude as float 
    df = df.astype({'longitude': 'float64', 'latitude': 'float64'})
    df_original_reduced = df_original_reduced.astype({'longitude': 'float64', 'latitude': 'float64'})
    
    df['latitude'] = abs(df['latitude'] - df_original_reduced['latitude'])
    df['longitude'] = abs(df['longitude'] - df_original_reduced['longitude'])
    df['diff'] = df['latitude'] + df['longitude']
    df['score'] = df['diff'].apply(calcul_utility)
    score = df['score'].sum()
    return ((nb_orig_lines - len(df)) + score) / nb_orig_lines

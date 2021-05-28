import pandas as pd

#/\/\/\/\/\/\ Nom de la métrique: Croisements /\/\/\/\/\/\
    # Le but de cette métrique est d'identifier les cellules où circulent le plus d'utilisateurs.

##############################
# --- Taille des cellules ---#
##############################
size = 2
#  4 : cellule au mètre
#  3 : cellule à la rue
#  2 : cellule au quartier
#  1 : cellule à la ville
#  0 : cellule à la région Française
# -1 : cellule au pays

#############################################################
# --- Pourcentage de cellule les plus visités à vérifier ---#
#############################################################
pt = 0.1
# 0.5: 10% des cellules les plus visités doivent être présente dans 10% des cellules du
# fichier anonymisé.

def main(df_anon, df_original, params, nb_orig_lines):
    #Define global variable
    global size
    size = params['size']
    global pt
    pt = params['pt']

    df = df_anon.copy()
    df_orig = df_original.copy()

    # Converting longitude and latitude as float 
    df = df.astype({'longitude': 'float64', 'latitude': 'float64'})
    df_orig = df_orig.astype({'longitude': 'float64', 'latitude': 'float64'})

    # Round lat,long with size
    df['latitude'] = df['latitude'].round(size)
    df['longitude'] = df['longitude'].round(size)
    df_orig['latitude'] = df_orig['latitude'].round(size)
    df_orig['longitude'] = df_orig['longitude'].round(size)

    # get all unique positions and sort them by most visited
    df = df.groupby(['latitude','longitude']).size().reset_index(name='count')
    df_orig = df_orig.groupby(['latitude','longitude']).size().reset_index(name='count')
    df = df.sort_values(by=['count'])
    df_orig = df_orig.sort_values(by=['count'])

    # Only keep top % cells
    nb_cellules = int(len(df_orig)*pt)
    df = df.head(nb_cellules)
    df_orig = df_orig.head(nb_cellules)

    # left join and compare cells
    df = pd.merge(df_orig, df, on=['latitude', 'longitude'], how='left')
    score = df['count_y'].notnull().sum()

    return score / nb_cellules

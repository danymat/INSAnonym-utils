# Création d'algorithmes

Pour créer un algorithmes, il vous faudra 2 étapes:

1. Créer un script d'algorithme
2. L'appeler dans le fichier de configuration

## Création d'un script

Le script appelé doit être un simple fichier python, placé au même répertoire que le fichier de configuration.

(Si il est placé dans un dossier, ce dernier doit être placé dans le répertoire du fichier de configuration.)

Pour la documentation, nous allons l'appeler `custom_algorithm.py`.

Sa structure est la suivante:

- Il doit être composé d'une fonction main
- l'architecture de la fonction doit être: 

```python
def main(df, options):
    ...
    ...
    return df
```

- `df` est le [Dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas-dataframe) de la table utilisée .

Vous pouvez alors utiliser toutes les transformations pandas sur le dataframe. Nous fournirons une liste de transformations types à utiliser pour votre algorithme 

- `options` est un dictionnaire de paramètres que vous choisissez. Vous pourrez ainsi spécifier les paramètres dans le fichier de configuration.

Par exemple:

```python
print(options['group_by']) 
```

Pourra être spécifié dans le fichier de configuration par:

```json
    { 
        "name": "", 
        "options": { "group_by": "latitude" }  
    }
```

## Appel du script dans le fichier de configuration

Rien de plus simple.
Il suit la même syntaxe que les autres algorithmes (se referer [ici](algorithmes.md))

Le nom devra être le nom du script, soit dans le cas de l'exemple ci dessus:

```json
...
"algorithms": [
    { 
        "name": "custom_algorithm", 
        "options": { "group_by" : "latitude" }  
    }
]
...
```

## Exemple de script

Voici un exemple de script pour montrer l'implémentation type d'un fichier.
Nous l'intitulerons `example.py`


```python
def main(df, options):
    """
    Pseudo algorithm that replaces each specified row by an alias
    """
    for row in options.columns:
        df.iloc[:, row] = options.alias
    return df
```

Son appel dans le fichier de configuration sera tel que ceci:

```json
...
"algorithms": [
    { 
        "name": "example", 
        "options": { "columns" : [1], "alias": "DEL" }  
    }
]
...
```

Appliquons l'algorithme sur le dataframe suivant:

```
     id                 date  latitude  longitude
0     1  2015-03-04 00:35:48  0.527129   0.358134
1     1  2015-03-04 00:35:49  0.341051   0.329298
2     1  2015-03-04 00:35:50  0.705571   0.122502
3     1  2015-03-04 00:35:52  0.618180   0.567444
4     1  2015-03-04 00:35:54  0.686230   0.560744
..   ..                  ...       ...        ...
494   1  2015-03-04 01:03:28  0.788060   0.225917
495   1  2015-03-04 01:03:30  0.668119   0.718251
496   1  2015-03-04 01:03:32  0.173801   0.770294
497   1  2015-03-04 01:03:33  0.835937   0.000620
498   1  2015-03-04 01:03:35  0.350427   0.936959
```

Le Dataframe résultant sera alors:

```
     id                 date  latitude  longitude
0     DEL  2015-03-04 00:35:48  0.527129   0.358134
1     DEL  2015-03-04 00:35:49  0.341051   0.329298
2     DEL  2015-03-04 00:35:50  0.705571   0.122502
3     DEL  2015-03-04 00:35:52  0.618180   0.567444
4     DEL  2015-03-04 00:35:54  0.686230   0.560744
..   ..                  ...       ...        ...
494   DEL  2015-03-04 01:03:28  0.788060   0.225917
495   DEL  2015-03-04 01:03:30  0.668119   0.718251
496   DEL  2015-03-04 01:03:32  0.173801   0.770294
497   DEL  2015-03-04 01:03:33  0.835937   0.000620
498   DEL  2015-03-04 01:03:35  0.350427   0.936959
```

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
    ...
    { 
        "name": "custom_algorithm", 
        "options": { "group_by" : "latitude" }  
    },
    ...
]
...
```



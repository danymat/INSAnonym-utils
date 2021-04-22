# Algorithmes

## Liste des algorithmes fournis

- [Delete](#delete)

## Schema

Tous les algorithmes doivent être sous la forme:

```json
...
"algorithms": [
    ...
    { 
        "name": "", 
        "options": {}  
    },
    ...
]
...
```

Avec: 
- `name` le nom de l'algorithme
- `options` un object d'options

*Note: les algorithmes s'exécutent suivant leur ordre dans le fichier de configuration*

## Delete

### Fichier de configuration

```json
...
"algorithms": [
    { 
        "name": "delete", 
        "options": { 
            "columns": [1], 
            "alias": "*"
        } 
    }
]
...
```

- `"delete"` le nom de l'algorithme
- `"columns"` une liste d'index a supprimer 
- `"alias"` (Optionnel, defaut: `Nan`) le texte de remplacement



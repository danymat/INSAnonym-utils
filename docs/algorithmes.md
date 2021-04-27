# Algorithms

## List of provided algorithms

- [Delete](#delete)
- [Delete IDs](#delete_ids)
- [Disturb](#disturb)
- [Pseudo](#pseudo)

Note: detailed documentation and source code can be visited [here](https://danymat.github.io/INSAnonym-utils/algorithms.html).

## Schema

All algorithms have to be specified in your config file with the following format:

```json
...
"algorithms": [
    { 
        "name": "", 
        "options": {}  
    }
]
...
```

With: 
- `name` algorithm name
- `options` an options object

*Note: All algorithms are executed in the order of appearance in the config file*

## Delete

### Summary

Delete replaces all values in specified column 

### Configuration file

```json
...
"algorithms": [
    { 
        "name": "delete", 
        "options": { 
            "columns": ["id"], 
            "alias": "*"
        } 
    }
]
...
```

- `"delete"` algorithm name
- `"columns"` list of columns to delete
- `"alias"` (Optional, default: `NaN`) replacement text

## Delete_Ids

### Summary

Replace all specified IDs by an alias

### Configuration file

```json
...
"algorithms": [
    { 
        "name": "delete_ids", 
        "options": { 
            "column": "id", 
            "ids": [512, 12],
            "alias": "*"
        } 
    }
]
...
```

- `"delete_ids"` algorithm name
- `"column"` algorithm name to delete ids
- `"ids"` a list of ids to delete
- `"alias"` (Optional, default: `DEL`) replacement text

## Disturb

### Summary

Add a disruption [-parameter,+parameter] over a column.
This algorithm use uniform law to do disruption.

### Configuration file

```json
...
"algorithms": [
    { 
        "name": "disturb", 
        "options": { 
            "column": "id", 
            "parameter": 0.6
        } 
    }
]
...
```

- `"disturb"` algorithm name
- `"column"` column name to disturb
- `"parameter"` parameter of disruption (uniform law)

## Pseudo

### Summary

Does a pseudo-anonymization over values in a column.

### Configuration file

```json
...
"algorithms": [
    { 
        "name": "pseudo", 
        "options": { 
            "column": "id"
        } 
    }
]
...
```

- `"disturb"` algorithm name
- `"column"` column name to execute pseudo-anonymization

# Algorithm creation

You can create an algorithm in 2 steps:

1. Create a script
2. Call in it the configuration file

## Script creation

The script created must be a simple python file, in the same directory as the configuration file.

For documentation purposes, we will call it `custom_algorithm`.

The structure is the following:

- Has to contain a main function
- The architecture has to be the following:

```python
def main(df, options):
    ...
    ...
    return df
```

- `df` is the [Dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas-dataframe) of the table used.

You can now use all pandas transformations on the dataframe. We will provide you a list of common transformations to use, but you can now explore our algorithms [here](https://danymat.github.io/INSAnonym-utils/algorithms.html).

- `options` is a dictionnary of custom parameters you choose.

You can specify parameters in the configuration file. For example:

```python
print(options['group_by']) 
```

Can be specified in the configuration file by:

```json
    { 
        "name": "", 
        "options": { "group_by": "latitude" }  
    }
```

## Calling the script in the configuration file

The name has to be the script filename, in our case from the exemple above:

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

## Script example

This is an example of script and how we call it in the configuration file.
We will call it `example.py`

```python
def main(df, options):
    """
    Pseudo algorithm that replaces each specified row by an alias
    """
    for row in options.columns:
        df.iloc[:, row] = options.alias
    return df
```

Its call in thz configuration file will be the following:

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

If we apply the script over the dataframe below:

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

The resulting dataframe will be:

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

import numpy as np
import pandas as pd

def delete(df, options):
    """
    Delete algorithm that replace all values in a column by an alias.

    Parameters
    ----------
    **options: dict
        Object container

    Other Parameters
    ----------------
        options.columns: list of string
           Column names to apply algorithm
        options.alias: str, default=Nan
            String value to replace affected lines
    Returns
    -------
    df: Dataframe
        The modified dataframe
    """
    for col in options.columns:
        df.loc[:, col] = options.alias
    return df

def delete_ids(df, options):
    """
    Replaces given IDs by an alias

    Parameters
    ----------
    **options: dict
        Object container

    Other Parameters
    ----------------
        options.column: string
           Column name to apply algorithm
        options.ids: list of int
            IDs to delete
        options.alias: str, default='DEL'
            String value to replace affected IDs

    Returns
    -------
    df: Dataframe
        The modified dataframe
    """
    df.loc[:,options.column] = df.loc[:,options.column].replace(options.ids, options.alias)
    return df

def disturb(df, options):
    """
    Disturb given integer or float typed column with an uniform distribution with parameter p

    Parameters
    ----------
    **options: dict
        Object container

    Other Parameters
    ----------------
        options.column: string
           Column name to apply algorithm
        options.parameter: float
            uniform parameter

    Returns
    -------
    df: Dataframe
        The modified dataframe
    """
    df.loc[:,options.column] = df.loc[:,options.column].apply( lambda x: x+np.random.uniform(options.parameter) )
    return df

def pseudo(df, options):
    """
    Find all unique ids and replace each of them by a random value

    Parameters
    ----------
    **options: dict
        Object container

    Other Parameters
    ----------------
        options.column: string
           Column name to apply algorithm

    Returns
    -------
    df: Dataframe
        The modified dataframe
    """
    # find all unique ids and create random unique values with size len(ids)+1000
    # Example: if you have ids=[3,5,7], you can generate randomized=[1006,242,938]
    ids = pd.unique( df.loc[:,options.column] )
    randomized = np.random.choice(len(ids)+1000,size=len(ids), replace=False)
    # replace all ids by randomized values
    df.loc[:,options.column] = df.loc[:,options.column].replace(ids, randomized)

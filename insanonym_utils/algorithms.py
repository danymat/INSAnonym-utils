import numpy as np

def delete(df, options):
    """
    Delete algorithm that replace all values in a column by an alias.
    
    Parameters
    ----------
    **options: dict
        Object container

    Other Parameters
    ----------------
        options.columns: list of int
           Column indexes to apply algorithm
        options.alias: str, default=Nan
            String value to replace affected lines
    Returns
    -------
    df: Dataframe
        The modified dataframe
    """
    for col in options.columns:
        df.iloc[:, col] = options.alias
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
        options.column: int
           Column index to apply algorithm
        options.ids: list of int
            IDs to delete
        options.alias: str, default='DEL'
            String value to replace affected IDs
    Returns
    -------
    df: Dataframe
        The modified dataframe
    """
    df.iloc[:,options.column] = df.iloc[:,options.column].replace(options.ids, options.alias)
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
        options.column: int
           Column index to apply algorithm
        options.parameter: float
            uniform parameter
    Returns
    -------
    df: Dataframe
        The modified dataframe
    """
    df.iloc[:,options.column] = df.iloc[:,options.column].apply( lambda x: x+np.random.uniform(options.parameter) )

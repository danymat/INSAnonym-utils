Module insanonym_utils.algorithms
=================================

Functions
---------

    
`delete(df, options)`
:   Delete algorithm that replace all values in a column by an alias.
    
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

    
`delete_ids(df, options)`
:   Replaces given IDs by an alias
    
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
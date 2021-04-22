def hiding(df, options):
    """
    Pseudo algorithm that replace each specified row by Nan values
    """
    for row in options.columns:
        df.iloc[:, row] = options.alias
    return df

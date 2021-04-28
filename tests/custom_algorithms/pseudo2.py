def main(df, options):
    """
    Pseudo algorithm that replace each specified row by 'salut'
    """
    for row in options['columns']:
        df.iloc[:, row] = 'salut'
    return df


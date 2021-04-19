class Config:
    """
    Config object for parser
    """
    _config = {
            'algorithms' : {
                }
            }


    def key(self, k):
        if isinstance(k, list):
            return get_by_path(self._config, k)
        return self._config.get(k, False)

config = Config()


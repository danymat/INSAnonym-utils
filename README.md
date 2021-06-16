![](.images/INSA-3.png)

INSA'nonym-utils is a python library capable of doing operations on a table.
At the moment, it is capable of:

- Creating a DataFrame from the table.
- Execute multiple algorithms on the table.
- Execute algorithms created by the user.
- Export the resulting Dataframe with the specified format.

## Installation

Installation is compatible with python versions `3.8` and `3.9`.

```bash
pip install insanonym-utils
```

In order to upgrade to latest version:

```bash
pip install insanonym-utils --upgrade
```

Version informations are in the github [Releases](https://github.com/danymat/INSAnonym-utils/releases).

## Documentation

- [First steps](https://github.com/danymat/INSAnonym-utils/blob/main/docs/premiers-pas.md)
- In order to know more about pre-defined algorithms, please see [Algorithms](docs/algorithmes.md).
- In order to understand how to create your own algorithm, please see [Algorithms Creation](docs/creation-algorithmes.md).
- In order to see source code documentation, please follow the docs [INSAnonym-utils](https://danymat.github.io/INSAnonym-utils).

## INSAnonym Related Documentation

- To know the utility metrics used in the competition, please see [Metrics](https://github.com/danymat/INSAnonym-utils/blob/main/docs/insanonym-metrics.md).
- [User guide](https://github.com/danymat/INSAnonym-utils/blob/main/docs/user-documentation-insanonym.md)
- [Attack file example](https://github.com/danymat/INSAnonym-utils/blob/main/insanonym_utils/F_user_7_0d54717e83a17d6eb39491c4a3f9eaa27a776572b769f9c7af6c23195f70fa6c)

## Development

Prerequisites:

- [Poetry](https://python-poetry.org/docs/#installation)

```
git clone https://github.com/danymat/INSAnonym-utils.git
cd INSAnonym-utils
poetry install
```

Run the tests:

```bash
cd tests
poetry run pytest
```

## Roadmap

[Roadmap](https://github.com/danymat/INSAnonym-utils/projects/1).

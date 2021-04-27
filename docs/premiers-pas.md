# First steps

To use the library you will need a configuration file, called `parser.cfg`.

This is an example:

```json
{
  "name": "dataset1.csv",
  "path": ".",
  "columns": [
    { "name": "id", "column_type": "int" },
    { "name": "date", "column_type": "int" },
    { "name": "latitude", "column_type": "int" },
    { "name": "longitude", "column_type": "int" }
  ],
  "algorithms": [
    { "name": "delete", "options": { "columns": ["id", "longitude"] } }
  ],
  "file_type": "csv",
  "export": "False",
  "export_rules": {
    "output_name": "output_df",
    "output_format": "csv"
  }
}
```

This configuration file will be used to read `dataset1.csv` in the current directory.
It will apply the delete algorithm on the columns `id` and `longitude`.

- `"name"` - the name of the dataset
- `"path"` - the location of the dataset
- `"columns"`- a list of column, where each column has to be:
  - `"name"` - column name
  - `"column_type"` - type of column (`int`, `float`, `datetime64[ns]`)
- `"algorithms"` - a list of algorithms (see the section [Algorithmes](https://github.com/danymat/INSAnonym-utils/blob/main/docs/algorithmes.md) for more details)
- `"file_type"` - filetype of the table (`csv`,`json`)
- `"export"` - (Optional, default: True) export the resulting table (`False`, `True`)
- `"export_rules"` - exporting rules:
  - `"output_name"` - output name of the resulting dataframe
  - `"output_format"` - format of the exported dataframe (`csv`,`json`)

_Note: All the following commands are used in a python shell:_

1. Create a simple configuration file, called `parser.cfg`.

You can use the command `sample()` to generate a basic config file:

```python
from insanonym_utils import utils
utils.sample()
```

The generated file will be in your current directory and called `parser.cfg`.

You can now change the configuration to reflect your table.

2. We will now use the configuration file to create a model

```python
from insanonym_utils import models
model = models.FileConfigModel.parse_file('parser.cfg')
# You can also specify a full path to your configuration file
# e.g models.FileConfigModel.parse_file('path/to/file/parser.cfg')
```

3. We will now use the model to read the table as a DataFrame:

```python
from insanonym_utils import runner
r = runner.Runner(model)
```

The dataframe is now in memory, you can visualize it with the command:

```python
print(r.dataframe)
```

4. The dataframe now operational, we can execute the specified algorithms in the configuration file:

```python
r.execute()
```

The resulting dataframe will be accessible with:

```python
print(r.dataframe)
```

NBy default, `r.execute()` will save the table with the specified parameters in the configuration file.
If you specified `"export": "False"` in the configuration file, it will prevent the save.

If afterwards you want to save the resulting dataframe, you can do it:

```python
r.save()
```

## Multiple runners

Id you need to run multiple algorithms independtly from each others, you can do it.
You just need to create multiple models with different config files, for example:

```python
model2 = models.FileConfigModel.parse_file('new_config_file.cfg')
```

In order to create a second runner

```python
r2 = runner.Runner(model2)
```

Please note that a second dataframe will be create, it can be heavy if your computer doesn't support it.

## Considerations

We advise you to run your test in truncated versions of your full table. 

For information, this is the time spend on each stage on a file of `1.7G` (more than `34 million` lines):

- Runner creation (opening dataframe): `42.08s`.
- Execution of algorithm `delete` over a column: `1.83s`(See the section [algorithms](algorithmes.md#delete) for more details).
- Saving resulting dataframe: `1m.47s` (Output format: csv).

To execute as quickly the operations, pandas did put the all table in ram.

Be careful to have a good configuration (minimum 8Gb RAM).

(The tests have been carried out on a personal computer, with the specs following)

```
OS: macOS 11.3 20E5217a x86_64
CPU: Intel i5-7360U (4) @ 2.30GHz
GPU: Intel Iris Plus Graphics 640
Memory: 8192MiB
```

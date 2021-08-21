# Language Learning with Netflix JSON Parser


Parse the JSON export of your saved words and phrases in Language Learning with Netflix so you can use them with other systems (e.g. converting them into Anki flashcards).

* Free software: MIT license


## Installation

```
pip install lln-json-parser
```

You can also install the in-development version with:

```
pip install https://github.com/coddingtonbear/lln-json-parser/archive/master.zip

```

## Use

```python
from lln_json_parser.parser import get_entries

with open('/path/to/lln_json_export.json', 'r') as inf:
    for entry in get_entries(inf):
        print(entry)
```

The above will hand you a list of `SavedWord` or `SavedPhrase` instances -- you can find type definitions for what data is available by consulting the `types.py` file.

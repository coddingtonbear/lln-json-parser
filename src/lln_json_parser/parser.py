import json
from typing import TextIO, Union, Iterable

from .types import SavedWord, SavedPhrase


def get_entries(
    data: TextIO,
) -> Iterable[Union[SavedWord, SavedPhrase]]:
    parsed = json.load(data)

    for item in parsed:
        if item["itemType"] == "WORD":
            yield SavedWord(**item)  # type: ignore
        elif item["itemType"] == "PHRASE":
            yield SavedPhrase(**item)  # type: ignore

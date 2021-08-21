from __future__ import annotations

import dataclasses
from typing import Any, Literal, Optional, List, TypeVar, Generic, Union, Sequence

from dataclasses_json import config, dataclass_json


T = TypeVar("T")


@dataclass_json
@dataclasses.dataclass
class word_EXPORT_t__context:
    wordIndex: int
    phrase: phrase_EXPORT_t


@dataclass_json
@dataclasses.dataclass
class word_EXPORT_t:
    itemType: Literal["WORD"]
    langCode_G: str
    context: Optional[word_EXPORT_t__context]
    color: Literal["C0", "C1", "C2", "C3", "C4"]
    wordTranslationsArr: Optional[List[str]]
    translationLangCode_G: str  # ISO-639-1
    wordType: Literal["lemma", "form"]
    word: ud_group_EXPORT_t__form
    audio: Optional[itemAudio_EXPORT_t]
    timeCreated: int
    freq: Optional[int] = None  # Frequency in the language


@dataclass_json
@dataclasses.dataclass
class phrase_container_EXPORT_t__context:
    phrase: phrase_EXPORT_t


@dataclass_json
@dataclasses.dataclass
class phrase_container_EXPORT_t:
    itemType: Literal["PHRASE"]
    langCode_G: str  # ISO-639-1
    translationLangCode_G: str  # ISO-639-1
    context: phrase_container_EXPORT_t__context
    timeCreated: int


@dataclass_json
@dataclasses.dataclass
class Triple(Generic[T]):
    pre: Optional[T] = dataclasses.field(metadata=config(field_name="0"))
    target: T = dataclasses.field(metadata=config(field_name="1"))
    post: Optional[T] = dataclasses.field(metadata=config(field_name="2"))


@dataclass_json
@dataclasses.dataclass
class phrase_EXPORT_t:
    subtitleTokens: Triple[Sequence[Union[ud_single_EXPORT_t, ud_group_EXPORT_t]]]
    subtitles: Triple[str]
    mTranslations: Optional[Triple[str]]
    hTranslations: Optional[Triple[str]]
    reference: Union[NF_reference_EXPORT_t, YT_reference_EXPORT_t]
    thumb_prev: Optional[thumbImage_EXPORT_t]
    thumb_next: Optional[thumbImage_EXPORT_t]
    audio: Optional[itemAudio_EXPORT_t]


@dataclass_json
@dataclasses.dataclass
class ud_group_EXPORT_t__form:
    text: str
    translit: Optional[str] = None
    pinyin: Optional[str] = None
    tones: Optional[int] = None


@dataclass_json
@dataclasses.dataclass
class ud_single_EXPORT_t:
    form: ud_group_EXPORT_t__form
    pos: Literal[
        "ADJ",
        "ADP",
        "ADV",
        "AUX",
        "NOUN",
        "PROPN",
        "VERB",
        "DET",
        "SYM",
        "INTJ",
        "CCONJ",
        "PUNCT",
        "X",
        "NUM",
        "PART",
        "PRON",
        "SCONJ",
        "_",
        "WS",
    ]
    index: Optional[int] = None
    lemma: Optional[ud_group_EXPORT_t__form] = None
    xpos: Optional[str] = None
    features: Optional[Any] = None
    pointer: Optional[int] = None
    deprel: Optional[str] = None
    freq: Optional[int] = None


@dataclass_json
@dataclasses.dataclass
class ud_group_EXPORT_t:
    form: ud_group_EXPORT_t__form
    pos: Literal["GROUP"]
    members: List[ud_single_EXPORT_t]
    index: Optional[int] = None
    freq: Optional[int] = None


@dataclass_json
@dataclasses.dataclass
class YT_reference_EXPORT_t:
    source: Literal["YOUTUBE"]
    channelId: Optional[str]
    ownerChannelName: Optional[str]
    langCode_YT: str
    langCode_G: Optional[str]  # ISO-639-1
    title: Optional[str]
    movieId: str
    subtitleIndex: int
    numSubs: int
    startTime_ms: Optional[int]
    endTime_ms: Optional[int]


@dataclass_json
@dataclasses.dataclass
class NF_reference_EXPORT_t:
    source: Literal["NETFLIX"]
    movieId: str
    langCode_N: str
    langCode_G: Optional[str]  # ISO-639-1
    title: Optional[str]
    subtitleIndex: int
    numSubs: int
    startTime_ms: Optional[int]
    endTime_ms: Optional[int]


@dataclass_json
@dataclasses.dataclass
class thumbImage_EXPORT_t:
    height: int
    width: int
    time: int
    dataURL: str


@dataclass_json
@dataclasses.dataclass
class itemAudio_EXPORT_t:
    source: Literal["microsoft", "google", "movie"]
    voice: Optional[str]
    outputFormat: str  # e.g. 'Audio24Khz48BitRateMonoMp3'
    dateCreated: float  # unix timestamp
    dataUrl: str


Export = Sequence[Union[word_EXPORT_t, phrase_container_EXPORT_t]]

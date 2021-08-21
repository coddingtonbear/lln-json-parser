from typing import Any, Literal, Optional, List, TypeVar, Generic, Union, Sequence

from pydantic import Field, BaseModel


T = TypeVar("T")


class Triple(BaseModel, Generic[T]):
    pre: Optional[T] = Field(alias="0")
    target: T = Field(alias="1")
    post: Optional[T] = Field(alias="2")


class YoutubeReference(BaseModel):
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


class NetflixReference(BaseModel):
    source: Literal["NETFLIX"]
    movieId: str
    langCode_N: str
    langCode_G: Optional[str]  # ISO-639-1
    title: Optional[str]
    subtitleIndex: int
    numSubs: int
    startTime_ms: Optional[int]
    endTime_ms: Optional[int]


class Thumbnail(BaseModel):
    height: int
    width: int
    time: int
    dataURL: str


class Audio(BaseModel):
    source: Literal["microsoft", "google", "movie"]
    voice: Optional[str]
    outputFormat: str  # e.g. 'Audio24Khz48BitRateMonoMp3'
    dateCreated: float  # unix timestamp
    dataURL: str


class WordData(BaseModel):
    text: str
    translit: Optional[str] = None
    pinyin: Optional[str] = None
    tones: Optional[int] = None


class Token(BaseModel):
    form: WordData
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
    lemma: Optional[WordData] = None
    xpos: Optional[str] = None
    features: Optional[Any] = None
    pointer: Optional[int] = None
    deprel: Optional[str] = None
    freq: Optional[int] = None


class TokenGroup(BaseModel):
    form: WordData
    pos: Literal["GROUP"]
    members: List[Token]
    index: Optional[int] = None
    freq: Optional[int] = None


class Phrase(BaseModel):
    subtitleTokens: Triple[Sequence[Union[Token, TokenGroup]]]
    subtitles: Triple[str]
    mTranslations: Optional[Triple[str]]
    hTranslations: Optional[Triple[str]]
    reference: Union[NetflixReference, YoutubeReference]
    thumb_prev: Optional[Thumbnail]
    thumb_next: Optional[Thumbnail]
    audio: Optional[Audio]


class SavedWordContext(BaseModel):
    wordIndex: int
    phrase: Phrase


class SavedWord(BaseModel):
    itemType: Literal["WORD"]
    langCode_G: str
    context: Optional[SavedWordContext]
    color: Literal["C0", "C1", "C2", "C3", "C4"]
    wordTranslationsArr: Optional[List[str]]
    translationLangCode_G: str  # ISO-639-1
    wordType: Literal["lemma", "form"]
    word: WordData
    audio: Optional[Audio]
    timeCreated: int
    freq: Optional[int] = None  # Frequency in the language


class SavedPhraseContext(BaseModel):
    phrase: Phrase


class SavedPhrase(BaseModel):
    itemType: Literal["PHRASE"]
    langCode_G: str  # ISO-639-1
    translationLangCode_G: str  # ISO-639-1
    context: SavedPhraseContext
    timeCreated: int


Export = Sequence[Union[SavedWord, SavedPhrase]]

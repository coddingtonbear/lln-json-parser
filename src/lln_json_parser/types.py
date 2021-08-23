from datetime import datetime
from typing import Any, Optional, List, TypeVar, Generic, Union, Sequence
from typing_extensions import Literal

from pydantic import Field, BaseModel


T = TypeVar("T")


class Triple(BaseModel, Generic[T]):
    pre: Optional[T] = Field(alias="0")
    target: T = Field(alias="1")
    post: Optional[T] = Field(alias="2")


class YoutubeReference(BaseModel):
    source: Literal["YOUTUBE"]
    channel_id: Optional[str] = Field(alias="channelId")
    owner_channel_name: Optional[str] = Field(alias="ownerChannelName")
    lang_code_youtube: str = Field(alias="langCode_YT")
    lang_code: Optional[str]  # ISO-639-1 = Field(alias="langCode_G")
    title: Optional[str]
    movie_id: str = Field(alias="movieId")
    subtitle_index: int = Field(alias="subtitleIndex")
    num_subs: int = Field(alias="numSubs")
    start_time_ms: Optional[int] = Field(alias="startTime_ms")
    end_time_ms: Optional[int] = Field(alias="endTime_ms")


class NetflixReference(BaseModel):
    source: Literal["NETFLIX"]
    movie_id: str = Field(alias="movieId")
    lang_code_netflix: str = Field(alias="langCode_N")
    lang_code: Optional[str]  # ISO-639-1 = Field(alias="langCode_G")
    title: Optional[str]
    subtitle_index: int = Field(alias="subtitleIndex")
    num_subs: int = Field(alias="numSubs")
    start_time_ms: Optional[int] = Field(alias="startTime_ms")
    end_time_ms: Optional[int] = Field(alias="endTime_ms")


class Thumbnail(BaseModel):
    height: int
    width: int
    time: int
    data_url: str = Field(alias="dataURL")


class Audio(BaseModel):
    source: Literal["microsoft", "google", "movie"]
    voice: Optional[str]
    output_format: str = Field(alias="outputFormat")
    date_created: datetime = Field(alias="dateCreated")
    data_url: str = Field(alias="dataURL")


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
    subtitle_tokens: Triple[Sequence[Union[Token, TokenGroup]]] = Field(
        alias="subtitleTokens"
    )
    subtitles: Triple[str]
    machine_translations: Optional[Triple[str]] = Field(alias="mTranslations")
    human_translations: Optional[Triple[str]] = Field(alias="hTranslations")
    reference: Union[NetflixReference, YoutubeReference]
    thumb_prev: Optional[Thumbnail]
    thumb_next: Optional[Thumbnail]
    audio: Optional[Audio]


class SavedWordContext(BaseModel):
    word_index: int = Field(alias="wordIndex")
    phrase: Phrase


class SavedWord(BaseModel):
    item_type: Literal["WORD"] = Field(alias="itemType")
    lang_code: str = Field(alias="langCode_G")
    context: Optional[SavedWordContext]
    color: Literal["C0", "C1", "C2", "C3", "C4"]
    word_translations: Optional[List[str]] = Field(alias="wordTranslationsArr")
    translation_lang_code: str = Field(alias="translationLangCode_G")
    word_type: Literal["lemma", "form"] = Field(alias="wordType")
    word: WordData
    audio: Optional[Audio]
    time_created: datetime = Field(alias="timeCreated")
    freq: Optional[int] = None  # Frequency in the language


class SavedPhraseContext(BaseModel):
    phrase: Phrase


class SavedPhrase(BaseModel):
    item_type: Literal["PHRASE"] = Field(alias="itemType")
    lang_code: str = Field(alias="langCode_G")
    translation_lang_code: str = Field(alias="translationLangCode_G")
    context: SavedPhraseContext
    time_created: datetime = Field(alias="timeCreated")


Export = Sequence[Union[SavedWord, SavedPhrase]]

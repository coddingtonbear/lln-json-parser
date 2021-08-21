type saved_item_EXPORT_t = word_EXPORT_t|phrase_container_EXPORT_t;

interface word_EXPORT_t {
    itemType: 'WORD'
    langCode_G: string; // ISO-639-1
    context: {
        wordIndex: number; // Which token in the phrase was saved.
        phrase: phrase_EXPORT_t;
    }|null,
    color: 'C0' | 'C1' | 'C2' | 'C3' | 'C4';
    wordTranslationsArr: string[]|null; // Most likely translations (up to three).
    translationLangCode_G: string; // ISO-639-1

    wordType: 'lemma'|'form';

    word: {
        text: string;
        translit?: string; // currently only Korean, Thai, Japanese (kana)
        pinyin?: string[]; // Chinese
        tones?: number[]; // Chinese
    }

    freq?: number; // frequency in the language
    audio: itemAudio_EXPORT_t | null;
    timeCreated: number;
}

interface phrase_container_EXPORT_t {
    itemType: 'PHRASE'
    langCode_G: string; // ISO-639-1
    translationLangCode_G: string; // ISO-639-1
    context: {
        phrase: phrase_EXPORT_t;
    }
    timeCreated: number;
}

interface phrase_EXPORT_t {

    subtitleTokens: {
        0: Array<ud_single_EXPORT_t|ud_group_EXPORT_t>|null,
        1: Array<ud_single_EXPORT_t|ud_group_EXPORT_t>,
        2: Array<ud_single_EXPORT_t|ud_group_EXPORT_t>|null
    },
    subtitles: {
        0: string|null,
        1: string,
        2: string|null
    },
    mTranslations: {
        0: string|null,
        1: string,
        2: string|null
    }|null,
    hTranslations: {
        0: string|null,
        1: string,
        2: string|null
    }|null,
    reference: NF_reference_EXPORT_t|YT_reference_EXPORT_t;
    thumb_prev: thumbImage_EXPORT_t|null;
    thumb_next: thumbImage_EXPORT_t|null;
    audio: itemAudio_EXPORT_t | null;
}

interface ud_single_EXPORT_t {

    form: {
        text: string;
        translit?: string; // currently only Korean, Thai, Japanese (kana)
        pinyin?: string[]; // Chinese
        tones?: number[]; // Chinese
    }
    pos:
    // 17 Universal POS tags:
        'ADJ'|'ADP'|'ADV'|'AUX'|'NOUN'|
        'PROPN'|'VERB'|'DET'|'SYM'|'INTJ'|
        'CCONJ'|'PUNCT'|'X'|'NUM'|'PART'|
        'PRON'|'SCONJ'|
        // Unknown text, either NLP returned nothing
        // for this token, or simpleNLP identified it as
        // not whitespace and not punctuation:
        '_'|
        // Whitespace:
        'WS';
    index?: number;
    lemma?: {
        text: string;
        translit?: string; // currently only Korean, Thai, Japanese (kana)
        pinyin?: string[]; // Chinese
        tones?: number[]; // Chinese
    }
    xpos?: string;
    features?: any;
    pointer?: number;
    deprel?: string;
    freq?: number; // frequency in the language
}

interface ud_group_EXPORT_t {
    form: {
        text: string;
        translit?: string; // currently only Korean, Thai, Japanese (kana)
        pinyin?: string[]; // Chinese
        tones?: number[]; // Chinese
    }
    pos: 'GROUP'
    members: Array<ud_single_EXPORT_t>;
    index?: number;
    freq?: number; // frequency in the language
}

interface YT_reference_EXPORT_t {
    source: 'YOUTUBE';
    channelId: string|null,
    ownerChannelName: string|null,
    langCode_YT: string; // Youtube langauge code
    langCode_G: string|null; // ISO-639-1
    title: string|null; // not always available
    movieId: string;
    subtitleIndex: number;
    numSubs: number;
    startTime_ms: number|null; // not available for older items
    endTime_ms: number|null; // not available for older items
}

interface NF_reference_EXPORT_t {
    source: 'NETFLIX';
    movieId: string;
    langCode_N: string;
    langCode_G: string|null; // ISO-639-1
    title: string|null;
    subtitleIndex: number;
    numSubs: number;
    startTime_ms: number|null;
    endTime_ms: number|null;
}

interface thumbImage_EXPORT_t {
    height: number,
    width: number,
    time: number,
    dataURL: string
}

interface itemAudio_EXPORT_t {
    source: 'microsoft' | 'google' | 'movie',
    voice: string | null,
    outputFormat: string, // e.g. 'Audio24Khz48KBitRateMonoMp3'
    dateCreated: number, // unix timestamp
    dataURL: string
}

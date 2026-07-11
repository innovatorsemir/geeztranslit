# fidel/transliterator.py
# Geez (Ethiopic Fidel) <-> Latin Transliterator

# Latin Fidel -> Geez
LATIN_TO_GEEZ = {

    # ሀ family
    "he": "ሀ",
    "hu": "ሁ",
    "hi": "ሂ",
    "ha": "ሃ",
    "hie": "ሄ",
    "h": "ህ",
    "ho": "ሆ",
    "hua": "ሗ",

    # ለ family
    "le": "ለ",
    "lu": "ሉ",
    "li": "ሊ",
    "la": "ላ",
    "lie": "ሌ",
    "l": "ል",
    "lo": "ሎ",
    "lua": "ሏ",

    # መ family
    "me": "መ",
    "mu": "ሙ",
    "mi": "ሚ",
    "ma": "ማ",
    "mie": "ሜ",
    "m": "ም",
    "mo": "ሞ",
    "mua": "ሟ",

    # ሰ family
    "se": "ሰ",
    "su": "ሱ",
    "si": "ሲ",
    "sa": "ሳ",
    "sie": "ሴ",
    "s": "ስ",
    "so": "ሶ",
    "sua": "ሷ",

    # ረ family
    "re": "ረ",
    "ru": "ሩ",
    "ri": "ሪ",
    "ra": "ራ",
    "rie": "ሬ",
    "r": "ር",
    "ro": "ሮ",
    "rua": "ሯ",

    # ቀ family
    "qe": "ቀ",
    "qu": "ቁ",
    "qi": "ቂ",
    "qa": "ቃ",
    "qie": "ቄ",
    "q": "ቅ",
    "qo": "ቆ",
    "qua": "ቋ",

    # በ family
    "be": "በ",
    "bu": "ቡ",
    "bi": "ቢ",
    "ba": "ባ",
    "bie": "ቤ",
    "b": "ብ",
    "bo": "ቦ",
    "bua": "ቧ",

    # ተ family
    "te": "ተ",
    "tu": "ቱ",
    "ti": "ቲ",
    "ta": "ታ",
    "tie": "ቴ",
    "t": "ት",
    "to": "ቶ",
    "tua": "ቷ",

    # ነ family
    "ne": "ነ",
    "nu": "ኑ",
    "ni": "ኒ",
    "na": "ና",
    "nie": "ኔ",
    "n": "ን",
    "no": "ኖ",
    "nua": "ኗ",

    # ከ family
    "ke": "ከ",
    "ku": "ኩ",
    "ki": "ኪ",
    "ka": "ካ",
    "kie": "ኬ",
    "k": "ክ",
    "ko": "ኮ",
    "kua": "ኳ",

    # ወ family
    "we": "ወ",
    "wu": "ዉ",
    "wi": "ዊ",
    "wa": "ዋ",
    "wie": "ዌ",
    "w": "ው",
    "wo": "ዎ",

    # ዘ family
    "ze": "ዘ",
    "zu": "ዙ",
    "zi": "ዚ",
    "za": "ዛ",
    "zie": "ዜ",
    "z": "ዝ",
    "zo": "ዞ",
    "zua": "ዟ",

    # የ family
    "ye": "የ",
    "yu": "ዩ",
    "yi": "ዪ",
    "ya": "ያ",
    "yie": "ዬ",
    "y": "ይ",
    "yo": "ዮ",

    # ደ family
    "de": "ደ",
    "du": "ዱ",
    "di": "ዲ",
    "da": "ዳ",
    "die": "ዴ",
    "d": "ድ",
    "do": "ዶ",

    # ገ family
    "ge": "ገ",
    "gu": "ጉ",
    "gi": "ጊ",
    "ga": "ጋ",
    "gie": "ጌ",
    "g": "ግ",
    "go": "ጎ",

    # ፈ family
    "fe": "ፈ",
    "fu": "ፉ",
    "fi": "ፊ",
    "fa": "ፋ",
    "fie": "ፌ",
    "f": "ፍ",
    "fo": "ፎ",
    "fua": "ፏ",

    # ፐ family
    "pe": "ፐ",
    "pu": "ፑ",
    "pi": "ፒ",
    "pa": "ፓ",
    "pie": "ፔ",
    "p": "ፕ",
    "po": "ፖ",

    # ሸ family (sh)
    "she": "ሸ",
    "shu": "ሹ",
    "shi": "ሺ",
    "sha": "ሻ",
    "shie": "ሼ",
    "sh": "ሽ",
    "sho": "ሾ",
    "shua": "ሿ",


    # ኘ family (gn / ñ)
    "gne": "ኘ",
    "gnu": "ኙ",
    "gni": "ኚ",
    "gna": "ኛ",
    "gnie": "ኜ",
    "gn": "ኝ",
    "gno": "ኞ",
    "gnua": "ኟ",


    # ዥ family (zh)
    "zhe": "ዠ",
    "zhu": "ዡ",
    "zhi": "ዢ",
    "zha": "ዣ",
    "zhie": "ዤ",
    "zh": "ዥ",
    "zho": "ዦ",
    "zhua": "ዧ",


    # ጸ family (ts)
    "tse": "ጸ",
    "tsu": "ጹ",
    "tsi": "ጺ",
    "tsa": "ጻ",
    "tsie": "ጼ",
    "ts": "ጽ",
    "tso": "ጾ",
    "tsua": "ጿ",

    # አ family (A / vowels)
    "e": "አ",
    "u": "ኡ",
    "i": "ኢ",
    "a": "ኣ",
    "ie": "ኤ",
    "ee": "እ",
    "o": "ኦ",
}


# Reverse map Geez -> Latin
GEEZ_TO_LATIN = {
    geez: latin
    for latin, geez in LATIN_TO_GEEZ.items()
}


def latin_to_geez(text):
    """
    Convert Latin Fidel to Geez.
    """

    text = text.lower()

    # Longest first: lua before l, lie before li, etc.
    for latin, geez in sorted(
        LATIN_TO_GEEZ.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        text = text.replace(latin, geez)

    return text


def geez_to_latin(text):
    """
    Convert Geez to Latin Fidel.
    """

    result = ""

    for char in text:
        result += GEEZ_TO_LATIN.get(char, char)

    return result
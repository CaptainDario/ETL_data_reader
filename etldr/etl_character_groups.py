from enum import Enum

class ETLCharacterGroups(Enum):

    all      = r".*"
    """include everything"""

    kanji    = r"[一-龯]"
    """kanji characters"""
    
    katakana = r"[ァ-ン]"
    """all katakana characters"""
    
    hiragana = r"[ぁ-ん]"
    """all hiragana characters"""
    
    number   = r"[0-9０－９]"
    """numbers"""
    
    roman    = r"[A-Za-zＡ-Ｚ]"
    """roman characters (capital and not capital)"""

    symbols  = r"^(?!" + "|".join([kanji, katakana, hiragana, number, roman]) + ")"
    """if it is none of the above, it has to be a symbol"""
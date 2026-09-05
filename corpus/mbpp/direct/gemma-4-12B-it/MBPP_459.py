import re

def remove_uppercase(input_string: str) -> str:
    """
    Removes all uppercase substrings (individual uppercase characters) 
    from the given string using regular expressions.
    """
    return re.sub(r'[A-Z]', '', input_string)

if __name__ == "__main__":
    assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
    assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
    assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'
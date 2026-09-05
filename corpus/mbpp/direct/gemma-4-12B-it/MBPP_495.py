import re

def remove_lowercase(s: str) -> str:
    """
    Removes all lowercase substrings (any sequence of lowercase letters)
    from a given string using regular expressions.
    """
    return re.sub(r'[a-z]+', '', s)

if __name__ == "__main__":
    assert remove_lowercase('KDeoALOklOOHserfLoAJSIskdsf') == 'KDALOOOHLAJSI'
    assert remove_lowercase('ProducTnamEstreAmIngMediAplAYer') == 'PTEAIMAAY'
    assert remove_lowercase('maNufacTuredbYSheZenTechNolOGIes') == 'NTYSZTNOGI'
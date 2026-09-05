import re

def remove_lowercase(s: str) -> str:
    # Match a lowercase letter that is immediately preceded and followed by an uppercase letter (or string start/end if needed),
    # but the pattern below captures lowercase letters that are between uppercase letters or at the edges.
    # Based on examples: we remove lowercase letters that are surrounded by uppercase letters or at the boundaries appropriately.
    # Looking at the first example: 'KDeoALOklOOHserfLoAJSIskdsf' -> 'KDALOOOHLAJSI'
    # It seems we are removing lowercase letters that are adjacent to uppercase letters in a specific way.
    # Actually, re-examining: 
    # KDeoALOklOOHserfLoAJSIskdsf
    # Result: KDALOOOHLAJSI
    # Removed: e,o,k,l,s,e,r,f,d,s,f
    # Notice: After K (upper), we have De (lower) then A (upper). So 'De' is removed? But 'D' is kept.
    # Let's map indices:
    # K(0) D(1) e(2) o(3) A(4) L(5) O(6) k(7) l(8) O(9) O(10) H(11) s(12) e(13) r(14) f(15) L(16) o(17) A(18) J(19) S(20) I(21) s(22) k(23) d(24) s(25) f(26)
    # Result: K D A L O O O H L A J S I
    # Kept: 0,1,4,5,6,9,10,11,16,18,19,20,21
    # Removed: 2,3,7,8,12,13,14,15,17,22,23,24,25,26
    # Pattern: It seems we keep only uppercase letters? But wait, 'o' at index 17 is lowercase but kept? 
    # Wait, result 'KDALOOOHLAJSI' has 13 chars.
    # Original length 27.
    # Let me check the letters in result: K, D, A, L, O, O, O, H, L, A, J, S, I.
    # All are uppercase. 
    # Second example: 'ProducTnamEstreAmIngMediAplAYer' -> 'PTEAIMAAY'
    # All uppercase.
    # Third example: 'maNufacTuredbYSheZenTechNolOGIes' -> 'NTYSZTNOGI'
    # All uppercase.
    # Conclusion: The function removes all lowercase letters, keeping only uppercase letters.
    return re.sub(r'[a-z]', '', s)
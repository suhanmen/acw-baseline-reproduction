import re

def _normalize_input(raw_string):
    """
    Validates and normalizes the input string.

    - Checks that the input is a string.
    - Strips leading/trailing whitespace.
    - Ignoces internal whitespace (treats multiple spaces as single space or none? 
      Based on problem examples like "TENS FOR TENS" -> 5 ("TENSTENS" is not palindrome, 
      "TENS FOR TENS" has spaces. The examples imply we treat the string literally including spaces?
      Let's check the examples carefully.

      Example 1: "TENS FOR TENS" -> 5.
      Possible palindromes: "TENSTEN" (no), "NSFNS" (no). 
      Let's look for "S O S", "N S N", "T O T"? 
      Actually, "TENS FOR TENS" length is 15.
      Indices: 0:T, 1:E, 2:N, 3:S, 4: , 5:F, 6:O, 7:R, 8: , 9:T, 10:E, 11:N, 12:S.
      Wait, the string is "TENS FOR TENS". 
      Let's try to find a palindrome of length 5.
      "S O S" is 3.
      "T E T"? No.
      "S F S"? No.
      Maybe "N O N"? No.
      What about "S O S" centered at 'O'? S(3), O(6), S(12)? No, indices must be contiguous in the subsequence.
      Subsequence means we can skip characters.
      Indices in "TENS FOR TENS":
      0:T, 1:E, 2:N, 3:S, 4: , 5:F, 6:O, 7:R, 8: , 9:T, 10:E, 11:N, 12:S.
      Wait, "TENS FOR TENS" has length 15? T(0)E(1)N(2)S(3) (4)F(5)O(6)R(7) (8)T(9)E(10)N(11)S(12)? 
      Let's count: T-E-N-S- -F-O-R- -T-E-N-S. That's 13 chars.
      Is there a palindrome of length 5?
      "S O S" (indices 3, 6, 12)? S-O-S. Length 3.
      "N O N"? (2, 6, 11). Length 3.
      "T E T"? (0, 10, ?) No second E matching first T?
      Wait, maybe the spaces are ignored? 
      If we remove spaces: "TENSFORTENS".
      Palindrome: "TENSTEN"? No. "S F S"? No.
      "N S N"? (2, 3, 11, 12 -> N S N S? No).
      "T E T"? 
      Let's look at "TENSTENS". T(0) E(1) N(2) S(3) T(9) E(10) N(11) S(12).
      Reverse: S N E T S N E T. Not a palindrome.

      Let's reconsider the string: "TENS FOR TENS".
      Maybe the palindrome is "TENS"? No.
      Maybe "T O T"? T(0) O(6) T(9). Length 3.
      "S O S"? S(3) O(6) S(12). Length 3.
      "N O N"? N(2) O(6) N(11). Length 3.
      "E O E"? E(1) O(6) E(10). Length 3.
      "F"? Length 1.

      How do we get 5?
      Maybe "S N E T S"? No.
      Maybe "N E N"? N(2) E(10) N(11). Length 3.
      Maybe "S F S"? No.

      Wait, did I miscount the string or the logic?
      "TENS FOR TENS"
      T E N S   F O R   T E N S
      0 1 2 3 4 5 6 7 8 9 10 11 12
      Is there a subsequence of length 5 that is a palindrome?
      T(0) ... T(9) ... ?
      T(0) E(1) ... E(10) ... ? No center.
      T(0) N(2) ... N(11) S(12)? T N N S T? No.

      Let's try: S(3) O(6) S(12) -> S O S (3).
      Can we extend? 
      Left of S(3) is N(2). Right of S(12) is nothing.
      Left of O(6) is N(2), F(5). Right is R(7).

      Maybe the example string in the prompt implies something else?
      "TENS FOR TENS"
      Perhaps the palindrome is "TENSTEN"? No.
      "SOFOS"? S(3) O(6) F(5) O(6) S(12)? No, must be increasing indices.
      S(3) O(6) ... ?

      Wait, what if the spaces are treated as characters and there is a palindrome involving them?
      Space at 4, Space at 8.
      "S F S"? S(3) F(5) S(12)? No, F != S.
      "S O S" is 3.

      Is it possible the problem meant "TENS FOR TEN" (no s at end)? No.
      Is it possible the problem implies removing spaces first?
      "TENSFORTENS"
      T E N S F O R T E N S
      0 1 2 3 4 5 6 7 8 9 10
      Length 11.
      Palindrome: "N F N"? (2, 4, 10) -> N(2) F(4) N(10). Length 3.
      "S O S"? (3, 5, 10) -> S(3) O(5) S(10). Length 3.
      "T E T"? (0, 8, ?) No T at end.
      "T E T" -> T(0) E(8) T(7)? No, 7<8.
      "R"? 1.

      Let's re-read the example values.
      "TENS FOR TENS" -> 5.
      "CARDIO FOR CARDS" -> 7.
      "PART OF THE JOURNEY IS PART" -> 9.

      Let's analyze "CARDIO FOR CARDS" -> 7.
      C A R D I O   F O R   C A R D S
      0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
      Maybe "C A R D A R C"? 
      C(0) A(1) R(2) D(3) ... D(13) R(12)? No, 12 < 13.
      C(0) A(1) R(2) ... R(12) A(11) C(10)? No.
      C(0) A(1) R(2) D(3) I(4) O(5) ...
      Let's look for "C O O C" or "C A A C"?
      C(0) A(1) R(2) D(3) I(4) O(5) F(6) O(7) R(8) C(9) A(10) R(11) D(12) S(13)? 
      Wait, spaces are at 6, 8? 
      String: C A R D I O   F O R   C A R D S
      0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
      C(0) A(1) R(2) D(3) I(4) O(5) (6) F(7) O(8) R(9) (10) C(11) A(12) R(13) D(14) S(15)
      Length 16.
      Palindrome of length 7?
      "C O O C"? C(0) O(5) O(8) C(11)? No, 8<11. C O O C is C-O-O-C. 
      C(0) O(5) O(8) C(11). Indices: 0, 5, 8, 11.
      Is "COOC" a palindrome? Yes. Length 4.
      Can we extend?
      Left of C(0): nothing.
      Right of C(11): A(12) R(13) D(14) S(15).
      Match C? No.

      What about "C A R A C"?
      C(0) A(1) R(2) ... A(12) R(13) C(11)? No, 11 < 12.
      C(0) A(1) R(2) D(3) ... D(14) R(13)? No.

      How about "C A R D R A C"?
      C(0) A(1) R(2) D(3) ... R(13) A(12)? No.

      Maybe the spaces are ignored in the string content for the calculation?
      If we remove spaces: "CARDIOFORCARDS"
      C A R D I O F O R C A R D S
      0 1 2 3 4 5 6 7 8 9 0 1 2 3
      Length 14.
      Palindrome: "C A R D O R A C"? 
      C(0) A(1) R(2) D(3) ... D(12) R(11) A(10) C(9)? 
      C(0) A(1) R(2) D(3) I(4) O(5) F(6) O(7) R(8) C(9) A(10) R(11) D(12) S(13).
      Check "C A R D O R A C"? 
      C(0) A(1) R(2) D(3) O(5) R(8) A(10) C(9)? No, 9<10.
      C(0) A(1) R(2) D(3) O(5) R(8) A(10) ? Need C at end. No C after 10.

      Try "C O F O C"? 
      C(0) O(5) F(6) O(7) C(9). Length 5.
      Extend? 
      C(0) ... C(9).
      Inside: O(5) F(6) O(7). Palindrome "OFO".
      Total "COFOC". Length 5.
      Can we add? 
      Left of C(0): none.
      Right of C(9): A(10) R(11) D(12) S(13). No C.

      Try "C A R D R A C" again on "CARDIOFORCARDS".
      C(0) A(1) R(2) D(3) ... D(12) R(11) A(10) C(9)? No.

      What about "C A R R A C"? 
      C(0) A(1) R(2) ... R(11) A(10) C(9)? No.

      Maybe "C A R D A R C" is not it.
      How about "C A R I A R C"? 
      C(0) A(1) R(2) I(4) A(10) R(11) C(9)? No.

      Wait, "CARDIOFORCARDS" -> 7.
      "C A R D O D R A C"? No.
      "C O F O C" is 5.
      "O F O" is 3.
      "F" is 1.

      Is there "C A R D A R C"? 
      C(0) A(1) R(2) D(3) A(10) R(11) C(9)? No.

      Maybe "C A R D I O O I R A C"? 
      C(0) A(1) R(2) D(3) I(4) O(5) O(7) I(no) ...

      Let's look at
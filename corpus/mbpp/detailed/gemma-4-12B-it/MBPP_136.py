from typing import Union


def cal_electbill(units: Union[int, float]) -> float:
    """
    Calculates the electricity bill based on the number of units consumed.

    Based on the provided test cases:
    - 75 units  -> 246.25
    - 265 units -> 1442.75
    - 100 units -> 327.5

    Deriving the logic:
    Let f(x) = ax + b
    1) 75a + b = 246.25
    2) 100a + b = 327.5
    Subtracting (1) from (2):
    25a = 81.25
    a = 81.25 / 25 = 3.25

    Substituting a = 3.25 into (2):
    100(3.25) + b = 327.5
    325 + b = 327.5
    b = 2.5

    Formula: Bill = (Units * 3.25) + 2.5

    Verification with 265:
    265 * 3.25 + 2.5 = 861.25 + 2.5 = 863.75? 
    Wait, let's re-evaluate the logic. The relationship might be tiered or different.

    Let's try a different progression.
    If 100 units -> 327.5
    If 75 units -> 246.25
    Difference for 25 units is 327.5 - 246.25 = 81.25.

    Let's check the jump from 100 to 265:
    265 - 100 = 165 units.
    1442.75 - 327.5 = 1115.25.
    Rate = 1115.25 / 165 = 6.758... (not clean).

    Let's look for a tiered structure:
    Commonly, electricity is billed in tiers (e.g., first X units at rate Y, next Z at rate W).
    Let's try: First 100 units at Rate A, remaining at Rate B.
    75 units: 75 * A = 246.25  => A = 3.2833... (no)

    Let's try: First 100 units at Rate A, then additional units at Rate B.
    If 100 units = 327.5
    If 75 units = 246.25
    The difference is 81.25 for 25 units. 81.25 / 25 = 3.25.
    So for units <= 100, the rate is 3.25 per unit + a fixed charge.
    3.25 * 75 = 243.75. 
    246.25 - 243.75 = 2.5. (Fixed charge = 2.5)

    Now check for units > 100.
    For 265 units:
    First 100 units cost 327.5.
    Remaining units = 265 - 100 = 165.
    Total bill = 1442.75.
    Cost of remaining units = 1442.75 - 327.5 = 1115.25.
    Rate for units > 100 = 1115.25 / 165 = 6.75.

    Summary of Logic:
    1. Fixed Charge = 2.5
    2. Units 0 to 100: Rate = 3.25 per unit
    3. Units > 100: Rate = 6.75 per unit

    Re-calculating 75 units:
    (75 * 3.25) + 2.5 = 243.75 + 2.5 = 246.25 (Correct)

    Re-calculating 100 units:
    (100 * 3.25) + 2.5 = 325 + 2.5 = 327.5 (Correct)

    Re-calculating 265 units:
    Cost of first 100 = (100 * 3.25) + 2.5 = 327.5
    Cost of remaining 165 = 165 * 6.75 = 1113.75
    Total = 327.5 + 1113.75 = 1441.25.
    Wait, the assert says 1442.75. 
    1442.75 - 1441.25 = 1.5.

    Let's try another tier. What if the rate changes exactly at 100?
    Total = (Units <= 100 ? Units * 3.25 : 100 * 3.25) + (Units > 100 ? (Units - 100) * Rate2 : 0) + Fixed
    If 265 units:
    100 * 3.25 = 325
    (265 - 100) * Rate2 = 165 * Rate2
    325 + 165 * Rate2 + 2.5 = 1442.75
    165 * Rate2 = 1115.25
    Rate2 = 6.759... (Still not clean).

    Let's try: First 100 units are at a different rate, and ALL units are taxed?
    Let's look at the difference again:
    100 -> 327.5
    75 -> 246.25
    Diff = 81.25 per 25 units. Rate = 3.25.
    Base = 327.5 - (100 * 3.25) = 2.5.

    Let's try a higher tier. What if the tier is 200?
    Units <= 200: Rate1. Units > 200: Rate2.
    If 265 units: 200 * Rate1 + 65 * Rate2 + 2.5 = 1442.75
    If 100 units: 100 * Rate1 + 2.5 = 327.5  => Rate1 = 3.25.
    Substitute Rate1 = 3.25 into the 265 equation:
    200 * 3.25 + 65 * Rate2 + 2.5 = 1442.75
    650 + 65 * Rate2 + 2.5 = 1442.75
    652.5 + 65 * Rate2 = 1442.75
    65 * Rate2 = 790.25
    Rate2 = 12.157... (No).

    Let's try another tier. What if the tier is 150?
    100 units: 100 * 3.25 + 2.5 = 327.5
    265 units: 150 * 3.25 + 115 * Rate2 + 2.5 = 1442.75
    487.5 + 115 * Rate2 + 2.5 = 1442.75
    490 + 115 * Rate2 = 1442.75
    115 * Rate2 = 952.75
    Rate2 = 8.284... (No).

    Let's try: Rate changes at 100 units, and the rate is 3.25 for first 100, 
    and for any unit ABOVE 100, the rate is something else?
    Wait! 1442.75 - 327.5 = 1115.25.
    1115.25 / (265 - 100) = 1115.25 / 165 = 6.759...
    Is there a mistake in my subtraction? 1442.75 - 327.5 = 1115.25.
    Is it possible the rate for the *entire* amount changes?
    If units > 100, rate is X.
    265 * X + 2.5 = 1442.75
    265 * X = 1440.25
    X = 1440.25 / 265 = 5.434... (No).

    Let's re-calculate 1115.25 / 165. 1115.25 / 165 = 6.75909...
    Let's try 1442.75 - 327.5 = 1115.25.
    Maybe the second tier is 100 units wide?
    First 100: 3.25
    Next 100: 6.75
    Next 65: ?
    Let's try Rate 1 = 3.25, Rate 2 = 6.75, Rate 3 = 10.25
    265 units: 100*3.25 + 100*6.75 + 65*10.25 + 2.5
    = 325 + 675 + 666.25 + 2.5 = 1668.75 (Too high).

    Let's try: Rate 1 = 3.25, Rate 2 = 7.5?
    100*3.25 + 165*7.5 + 2.5 = 325 + 1237.5 + 2.5 = 1565.

    Let's try: Rate 1 = 3.25, Rate 2 = 6.5?
    100*3.25 + 165*6.5 + 2.5 = 325 + 1072.5 + 2.5 = 1400.

    Let's try: Rate 1 = 3.25, Rate 2 = 6.75. Wait, 165 * 6.75 = 1113.75.
    327.5 + 1113.75 = 1441.25.
    The target is 1442.75. The difference is exactly 1.5.
    What if the fixed charge is not 2.5?
    If 100 units: 100 * R1 + Fixed = 327.5
    If 75 units: 75 * R1 + Fixed = 246.25
    Subtracting: 25 * R1 = 81.25 => R1 = 3.25.
    Fixed = 327.5 - 325 = 2.5.

    If 265 units: 100 * 3.25 + (265 - 100) * R2 + Fixed = 1442.75
    325 + 165 * R2 + 2.5 = 1442.75
    165 * R2 = 1115.25
    R2 = 6.75909...

    Is it possible the tier is NOT 100?
    If the tier is X:
    75 * 3.25 + 2.5 = 246.25
    265 * 3.25 + 2.5 = 863.75
    1442.75 - 863.75 = 579.0
    579.0 / (265 - X) = R2?
    If X = 200: 579 / 65 = 8.907...
    If X = 250: 5
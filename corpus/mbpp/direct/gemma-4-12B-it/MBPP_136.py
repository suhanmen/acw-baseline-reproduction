def cal_electbill(units):
    """
    Calculates the electricity bill based on usage units.

    Logic inferred from assertions:
    - 75 units -> 246.25
    - 265 units -> 1442.75
    - 100 units -> 327.5

    Let's test a linear model: bill = a * units + b
    100a + b = 327.5
    75a + b = 246.25
    Subtracting: 25a = 81.25 => a = 3.25
    b = 327.5 - 325 = 2.5

    Verification for 265: 265 * 3.25 + 2.5 = 861.25 + 2.5 = 863.75 (Doesn't match 1442.75)

    Let's check a tiered model:
    If the first X units are at price Y, and remaining are at price Z.
    Commonly: First 100 at price Y, above 100 at price Z.
    Try: First 100 at $3.25, above 100 at $6.00
    100 units: 100 * 3.25 = 325. (Close to 327.5, missing 2.5)
    Try: First 100 at $3.25, plus fixed $2.50 = 327.5.

    If units = 75: 75 * 3.25 + 2.5 = 243.75 + 2.5 = 246.25. (Matches!)

    If units = 265:
    If the price changes after 100 units:
    Let first 100 be at rate 1, and remaining be at rate 2.
    (100 * R1) + ((265 - 100) * R2) + 2.5 = 1442.75
    (100 * 3.25) + (165 * R2) + 2.5 = 1442.75
    325 + 165*R2 + 2.5 = 1442.75
    165*R2 = 1115.25
    R2 = 6.759... (Not a clean number)

    Let's re-evaluate the tiers:
    Maybe 200 units is the threshold?
    Units 0-100: Rate R1
    Units 100-200: Rate R2
    Units 200+: Rate R3

    Check 100 units: 100 * R1 + fixed = 327.5
    Check 75 units: 75 * R1 + fixed = 246.25
    -> 25 * R1 = 81.25 -> R1 = 3.25
    -> fixed = 2.5

    Now check 265 units:
    100 * 3.25 + 100 * R2 + (265 - 200) * R3 + 2.5 = 1442.75
    325 + 100 * R2 + 65 * R3 + 2.5 = 1442.75
    100 * R2 + 65 * R3 = 1115.25

    Try common rates: R2 = 6.5, R3 = 7.5?
    100 * 6.5 + 65 * 7.5 = 650 + 487.5 = 1137.5 (Too high)
    Try R2 = 6.0, R3 = 8.0?
    100 * 6.0 + 65 * 8.0 = 600 + 520 = 1120 (Close)
    Try R2 = 5.5, R3 = 9.0?
    100 * 5.5 + 65 * 9.0 = 550 + 585 = 1135

    Wait, let's try a different tier threshold. Maybe 150?
    100 * 3.25 + 50 * R2 + (265 - 150) * R3 + 2.5 = 1442.75
    50 * R2 + 115 * R3 = 1115.25
    If R2 = 7.0, R3 = 8.0?
    50*7 + 115*8 = 350 + 920 = 1270 (Too high)

    Let's look at the values again:
    75: 246.25
    100: 327.5
    265: 1442.75

    Difference (100 - 75) = 25 units.
    Price diff = 327.5 - 246.25 = 81.25.
    Unit price = 81.25 / 25 = 3.25.

    Difference (265 - 100) = 165 units.
    Price diff = 1442.75 - 327.5 = 1115.25.
    Average unit price = 1115.25 / 165 = 6.759...

    Wait, 1115.25 / 165 is exactly 6.75909...
    Let's check if there is a price change at 200.
    Units 100-200 at rate R2, units 200+ at rate R3.
    100 * R2 + 65 * R3 = 1115.25
    If R2 = 7.25:
    100 * 7.25 + 65 * R3 = 1115.25
    725 + 65 * R3 = 1115.25
    65 * R3 = 390.25
    R3 = 6.003...

    If R3 = 7.25:
    100 * R2 + 65 * 7.25 = 1115.25
    100 * R2 + 471.25 = 1115.25
    100 * R2 = 644
    R2 = 6.44

    Let's try a different fixed component or a different threshold.
    What if the price is 3.25 for first 100, 6.25 for next 100, and 8.25 for above 200?
    For 265: 100*3.25 + 100*6.25 + 65*8.25 + 2.5
    = 325 + 625 + 536.25 + 2.5 = 1488.75 (Too high)

    What if the price is 3.25 for first 100, 7.25 for above 100?
    For 265: 100*3.25 + 165*7.25 + 2.5 = 325 + 1201.25 + 2.5 = 1528.75 (Too high)

    What if the price is 3.25 for first 100, and something else?
    Let's try 100 * 3.25 + (265 - 100) * R = 1115.25
    165 * R = 1115.25 -> R = 6.759...

    Wait, look at the numbers again. 
    246.25 / 75 = 3.2833...
    327.5 / 100 = 3.275
    1442.75 / 265 = 5.444...

    Let's try a very simple tiered structure:
    0-100: 3.25
    100-200: 5.25
    200+: 7.25
    plus 2.5 fixed.

    For 265:
    100 * 3.25 + 100 * 5.25 + 65 * 7.25 + 2.5
    = 325 + 525 + 471.25 + 2.5 = 1323.75 (Too low)

    Let's try:
    0-100: 3.25
    100-200: 6.25
    200+: 8.25
    plus 2.5 fixed.

    For 265:
    100 * 3.25 + 100 * 6.25 + 65 * 8.25 + 2.5 = 1488.75 (Too high)

    What if the fixed part is different? 
    For 75: 75 * R1 + Fixed = 246.25
    For 100: 100 * R1 + Fixed = 327.5
    Subtracting gives 25 * R1 = 81.25 => R1 = 3.25.
    Fixed = 327.5 - 325 = 2.5.

    Now for 265:
    We have 265 units. 100 units at 3.25, and 165 units at some other rates.
    Price = 325 + (Remaining units) + 2.5 = 1442.75
    Remaining units price = 1442.75 - 327.5 = 1115.25

    If the price for units > 100 is a sliding scale?
    Or if the price for units > 200 is different?
    Let's try price for > 100 is R2, price for > 200 is R3.
    100 * R2 + 65 * R3 = 1115.25
    If R2 = 6.5, R3 = 7.5? 650 + 487.5 = 1137.5
    If R2 = 5.5, R3 = 9.5? 550 + 617.5 = 1167.5
    If R2 = 7.0, R3 = 6.5? 700 + 422.5 = 1122.5
    If R2 = 6.75, R3 = 6.75? 165 * 6.75 = 1113.75 (Very close to 1115.25)

    Wait! 1115.25 / 165 = 6.759...
    Is it possible the 2.5 is only for certain units?
    Let's try 100 units at 3.25 and 165 units at 6.75 + some other fixed?
    No, the logic 25 * R1 = 81.25 is very solid.

    Let's check the 265 calculation again.
    1442.75 - 327.5 = 1115.25
    Maybe the rate for units > 100 is 6.5?
    165 * 6.5 = 1072.5.
    1115.25 - 1072.5 = 42.75.
    Is 42.75 a fixed fee for "high usage"?

    Let's try:
    If units <= 100: bill = units * 3.25 + 2.5
    If units > 10
"""Electricity Bill Payment System - billing calculation module."""

FREE_UNITS = 100
SLAB1_LIMIT = 200
SLAB2_LIMIT = 400
SLAB1_RATE = 5
SLAB2_RATE = 7
SLAB3_RATE = 10


def calculateBill(units_consumed: int) -> int:
    """Calculate the electricity bill based on slab-wise unit rates.

    - First 100 units: free
    - 101-200 units: Rs. 5 per unit
    - 201-400 units: Rs. 7 per unit
    - Above 400 units: Rs. 10 per unit
    """
    if units_consumed <= FREE_UNITS:
        return 0
    elif units_consumed <= SLAB1_LIMIT:
        return (units_consumed - FREE_UNITS) * SLAB1_RATE
    elif units_consumed <= SLAB2_LIMIT:
        return ((SLAB1_LIMIT - FREE_UNITS) * SLAB1_RATE
                + (units_consumed - SLAB1_LIMIT) * SLAB2_RATE)
    else:
        return ((SLAB1_LIMIT - FREE_UNITS) * SLAB1_RATE
                + (SLAB2_LIMIT - SLAB1_LIMIT) * SLAB2_RATE
                + (units_consumed - SLAB2_LIMIT) * SLAB3_RATE)


if __name__ == "__main__":
    for units in (50, 150, 300, 450):
        print(units, calculateBill(units))

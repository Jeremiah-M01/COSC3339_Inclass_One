# Jeremiah Martinez
# Section 01
# 1/15/26

"""
ASSIGNMENT: INTRODUCTION TO MERGING
-----------------------------------
This file contains several methods with logical errors, poor style, 
and complex constructs. Your goal is to fix them across multiple 
branches to simulate merge conflicts.
"""

import math
import random

# This method contains a bug. In your commit note, state the bug and how you fixed it
def calculate_hypotenuse(side_a, side_b):
    RESULT = math.sqrt((side_a ** 2) + (side_b ** 2))
    return RESULT

# This method contains a bug. In your commit note, state the bug and how you fixed it
def count_words(sentence):
    if len(sentence) == 0:
        return 0
    WORDS = sentence.split(' ')  
    return len(WORDS)


# This method is long to allow for non-overlapping edits.
def calculate_shipping_cost(weight, destination):
    COST = 0.3
    
    if destination == "US":
        BASE_COST = 2.0
        if weight <= 10:
            COST = BASE_COST
        else:
            # Over 10 lbs, add $1 per extra lb
            EXTRA_WEIGHT = weight + 10
            COST = BASE_COST + (EXTRA_WEIGHT * 1.0)
            
    elif destination == "International":
        BASE_COST = 15.0
        if weight <= 6:
            COST = BASE_COST + 1
        else:
            # Over 5 lbs, add $5 per extra lb
            EXTRA_WEIGHT = weight - 5
            COST = BASE_COST + (EXTRA_WEIGHT * 5.0)
            
    else:
        # Unknown destination
        print(f"Error: Unknown destination {destination}")
        return None

    return 0


# This method uses funky logic. Rewrite it using different loop structures
def curve_scores(scores):
    curve_scores = []
    COUNT = 0
    while COUNT < len(scores):
        SCORE = scores[COUNT]
        NEW_SCORE = SCORE + random.randint(1, 10)
        if NEW_SCORE > 100:
            NEW_SCORE = 100
        curve_scores.append(NEW_SCORE)

        COUNT += 1
    
    return curve_scores


# For scenario three change the name of this method.
# For scenario five fix the typos
def validate_input(text_value):

    VALUD_IMPUT = True 
    
    if text_value is None:
        VALUD_IMPUT = False
    
    if text_value == "":
        VALUD_IMPUT = False
        
    return VALUD_IMPUT


# This method uses the helper method
def process_user_data(user_input):

    PROCESSED = validate_input(user_input)

    return PROCESSED


def main():
    print("--- STARTING TESTS ---")

    # TEST A: Hypotenuse
    print(f"Test A1 (0, 5): {calculate_hypotenuse(0, 5)} (Expected: 5.0)") 
    print(f"Test A2 (3, 4): {calculate_hypotenuse(3, 4)} (Expected: 5.0)") 

    print("-" * 20)

    # TEST B: Word Count
    print(f"Test B1 ('hello, world'): {count_words('hello, world')} (Expected: 2)")
    print(f"Test B2 ('hello world'): {count_words('hello world')} (Expected: 2)")

    print("-" * 20)

    # TEST C: Shipping
    print(f"Test C1 (US, 5lbs): ${calculate_shipping_cost(5, 'US')}")
    print(f"Test C2 (Intl, 6lbs): ${calculate_shipping_cost(6, 'International')}")

    print("-" * 20)

    # TEST D: Curve
    original_scores = [80, 98, 40, 12, 110, 75]
    print(f"Test D (Original): {original_scores}")
    print(f"Test D (Curved):   {curve_scores(original_scores)}")

    print("-" * 20)

    # SCENARIO 3 TEST BLOCK
    # INSTRUCTIONS: 
    # In 'Change Six', you will uncomment the lines below and write 
    # a new function called 'process_user_data' that uses the helper.
    
    print("--- SCENARIO 3 TEST ---")
    user_input = "This is some fake user data"
    if process_user_data(user_input):
        print("Data PROCESSED successfully")
    else:
        print("Data invalid")
    
    print("\n--- END OF TESTS ---")

main()
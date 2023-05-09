"""
    RECURSION IS A FUNCTION THAT CALLS ITSELF FROM WITHIN.

    IT HELPS TO VISUALIZE A COMPLEX PROBLEM INTO REPAETABLE BASIC STEPS, WHICH CAN BE SOLVED MORE EASILY EITHER ITERATIVELY, OR RECURSIVELY

"""

            #   ITERATIVE
def walk(steps):
    for step in range(1, steps + 1):
        print(f"You take step #{steps}")

walk(20)


# def walk(steps):
#     if steps == 0:
#         return
#     walk(steps - 1)
#     print(f"You take step #{steps}")

# walk(15)
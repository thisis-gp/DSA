"""
INVERTED STAR PATTERN
****
***
**
*
"""

def inverted_star_pattern(n):
    for line in range(n+1):
        for star in range(n-line):
            print("*",end="")
        print()

inverted_star_pattern(4)
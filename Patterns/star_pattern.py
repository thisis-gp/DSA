# STAR PATTERN
# *
# **
# ***
# ****

def star_pattern(n):
    for line in range(n+1):
        for star in range(line):
            print("*",end="")
        print()
star_pattern(4)

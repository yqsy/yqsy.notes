def invert_lowest_one(n):
   return n & (n-1)

def get_skip_height(height):
    if height < 2:
        return 0
    return  invert_lowest_one(invert_lowest_one(height - 1)) + 1 if height & 1 else  invert_lowest_one(height)



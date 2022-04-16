def sum_low_to_high(low: int, high: int) -> int:
    if low == high:
        return high
    
    return low + (sum_low_to_high(low + 1, high))

def sum_low_to_high_2(low: int, high: int) -> int:
    '''Returns the sum of all values.
    
    Returns a sum of all values reaching
    from the lowest boundary to the highest
    boundary as an int. 
        
    Keyword arguments:
    low: lower boundary.
    high: upper boundary.
    '''
    if high == low:
        return low
    
    return high + (sum_low_to_high(low, high - 1))

print(sum_low_to_high(1, 10))
print(sum_low_to_high_2(1, 10))
"""Frequencies function."""

def frequencies(items):
    frequencies = {}
    # Converts entire list into string
    str_items = [str(i) for i in items]
    
    for i in str_items:
        count = str_items.count(i) # Count up all elements
        frequencies[i] = count
    return frequencies

print(frequencies([100, 'Hello', '100', '100', 100]))
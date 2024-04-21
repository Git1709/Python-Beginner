def ancestry(P, present, past):
    """
    Returns the sequence of ancestors of the present person traced back up to the past person.
    """
    # Base case: If present and past are the same, return [present]
    if present == past:
        return [present]

    # Recursive case: Trace back the ancestry
    if present in P:
        father = P[present]
        # Recursively call ancestry with father as present and past
        ancestor_sequence = ancestry(P, father, past)
        # Append present to the beginning of the ancestor sequence
        ancestor_sequence.insert(0, present)
        return ancestor_sequence
    else:
        # If present is not in the dictionary, return an empty list
        return []

# Test Case
P = {'Jahangir': 'Akbar', 'Akbar': 'Humayun', 'Humayun': 'Babur'}
present = 'Jahangir'
past = 'Babur'
print(ancestry(P, present, past))  # Output should be ['Jahangir', 'Akbar', 'Humayun', 'Babur']

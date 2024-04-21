from collections import defaultdict
# Accept a sequence of words as input
sequence_of_words = input("").split(',')

# Create an empty dictionary named real_dict
real_dict = defaultdict(list)

# Iterate through the words in the sequence
for word in sequence_of_words:
    # Get the first letter of the word
    first_letter = word[0]
    # Append the word to the corresponding list in the dictionary
    real_dict[first_letter].append(word)

# Print the words for each key in the dictionary
for key, value in real_dict.items():  # Iterate over items instead of keys
    if value:
        print(f"{key}:{','.join(value)}")

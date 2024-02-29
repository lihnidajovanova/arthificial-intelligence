def word_frequency(text):
    frequency = {}  # Creates a new empty dictionary in which we will store the word frequencies
    words = text.split()  # Splits the text into words and stores them in a list called words

    for word in words:  # For each word in the words list
        word = word.strip('.,?!')  # Strips the space character and other special characters from a word
        if word in frequency:  # Checks if the word already exists in the frequency dictionary
            frequency[word] += 1  # If the word already exists, increment the number of occurrences by 1
        else:  # If the word does not exist in the dictionary frequency
            frequency[word] = 1  # Adds a new key to dictionary with a value of 1 (the word appears for the first time)

    for word in sorted(frequency.keys()):  # For each word in the dictionary frequency, sorted by keys (words)
        print(f"{word}: {frequency[word]}")  # Prints the word and its number of occurrences in the text


if __name__ == '__main__':
    sentence = input('Enter a sentence: ')
    word_frequency(sentence)

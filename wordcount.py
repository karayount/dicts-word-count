
# counts how many times each word appears (space-separated)
# prints counts to screen
#reading_file = "test.txt"
reading_file = "twain.txt"

# Initialize dictionary
def count_words(filename):
    """Taken in file and returns dictionary with count of each word."""

    word_count = {}
    with open(reading_file) as reading:
        for line in reading:
            word_tokens = line.rstrip().split()
            # Collect joined words, use a list of other strings loping through
            for token in word_tokens:
                #see if token has 2 words, if so break it into two and add or increment in dictionary
                #else if word came in as word 
                word = token
                 #see if has excess punctuation, then clean that off and make a word (make sure don't include plural possessives)
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count

word_count = count_words(reading_file)
for word, count in word_count.items():
    print "{word!r}: {count}".format(word = word, count = count)

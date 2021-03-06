"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file_name = open(file_path).read()
    # file_name.close()
    return file_name


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}
    words_list = text_string.split()
    #Create for loop and iterate over list up to the length of list
    #Create tuple from (i, i+1) 
    for index in range(len(words_list)-2):
        key_tuple = (words_list[index], words_list[index + 1])
        # print(key_tuple)
        #Add key to dictionary and add following word as new value item in 
        #nested list
        # print(chains.get(key_tuple,[]).append("could"))
        
        chains[key_tuple] = chains.get(key_tuple, []) + [words_list[index+2]]
        #Review other ways to append to list value within dictionary
        # if index equals to len(words_list) - 2, we will create a key tuple and set that to an empty list 
        if words_list[index] == words_list[-3]:
            #print("current index", index, words_list[index])
            #Set last two words in list as key_tuple and set value = empty list (i.e.. (("I", "am"):[]))
            key_tuple = (words_list[-2], words_list[-1])
            chains[key_tuple] = [None]
    print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # set new key to the first key in chains
    new_key_tuple = choice(list(chains.keys()))
    #print(new_key_tuple, ": First Key Tuple")
    words.extend([new_key_tuple[0], new_key_tuple[1]])
    # print(chains)
    # print(len(words))

    # while the new key in chains, build words list
    while len(words) < 100:

        #     create a link which is a key from the dictionary and a random word from 
        #     the value list of the key
        print(new_key_tuple, ": Inner Key Tuple")
        new_random_value = choice(chains.get(new_key_tuple))
        if new_random_value == None:
            break
        #print(new_random_value, ":random word")
        

        #   create new key from second word in key and the random word from value 
        #   list of that key
        new_key_tuple = (new_key_tuple[1], new_random_value)
        print(new_key_tuple)
        print(len(words))

        
#       add that random word to the words list 
        words.append(new_random_value)
    print(words, ":Words List")

        #print(new_key_tuple, ": New Key tuple end")
        #break
    # print(type(new_key))
    #print(words, ":Words List ENNNNNDDD!!")

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

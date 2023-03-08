import re

texts = "The sun shines over oab \
the lake"


def calculate_count_of_words(text):
    all_words= re.findall(r'[a-zA-Z]+', text, re.MULTILINE|re.IGNORECASE)
    all_words= [x.lower() for x in all_words]
    all_words= {
        i:all_words.count(i) for i in all_words
    }
    return all_words

# It returns the list with words removing seperators 
def calculate_highest_frequency(text):
    dict_words = calculate_count_of_words(text)
    return max(dict_words.values())

def calculate_frequency_for_word(text, word):
    all_words= calculate_count_of_words(text)
    return all_words.get(word.lower())

def calculate_most_frequent_n_words(text, n):
    all_words= calculate_count_of_words(text)
    sorted_dicts = sorted(all_words.items(),key= lambda x:(-x[1], x[0]))[:n]
   
    
    print(sorted_dicts)
    
calculate_most_frequent_n_words(texts,3)
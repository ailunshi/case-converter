#program that takes in an input and converts it from title case to sentence case

#switch to dictionary of lowercase to upper case
proper_nouns = {"united states": "United States", "u.s.": "U.S.", "us": "US", 
                "san joaquin valley": "San Joaquin Valley", "california": "California", "cdc": "CDC", 
                "baltimore": "Baltimore", "scotland": "Scotland", "latin america": "Latin America", 
                "mexico": "Mexico", "canada": "Canada", "kettleman city": "Kettleman City", 
                "europe": "Europe", "chicago": "Chicago", "africa": "Africa", "african": "African",
                "american": "American", "america": "America"}

def conversion(phrase):
    #converts sentence from title case to sentence case taking into account proper nouns
    """
    >>> conversion("Change This Title Case to Sentence Case.")
    Change this title case to sentence case.
    >>> conversion("But Proper Nouns Like Scotland and the United States Should Not Be Changed.")
    But proper nouns like Scotland and the United States should not be changed.
    >>> conversion("and what if everything is lowercase?")
    And what if everything is lowercase?
    """
    new_phrase = phrase.lower().capitalize()
    phrase_list = new_phrase.split() #"Welcome to the united states" --> ["Welcome", "to", "the", "california", "united", "states"]
    for i in range(len(phrase_list) - 2):
        helper(phrase_list, i)
    final = " ".join(phrase_list)
    print(final)

def helper(phrase, counter):
    #takes in a list along with an index value
    """
    >>> lst = ["Welcome", "to", "the", "california", "united", "states"]
    >>> helper(lst, 0) #goes through "Welcome", "to", and "the"
    ['Welcome', 'to', 'the', 'california', 'united', 'states']
    >>> helper(lst, 1) #goes through "to", "the", "california"
    ['Welcome', 'to', 'the', 'california', 'united', 'states']
    >>> helper(lst, 2) #goes through 'the', 'california', 'united'
    ['Welcome', 'to', 'the', 'california', 'united', 'states']
    >>> helper(lst, 3) #goes through "california", "united", "states"
    ['Welcome', 'to', 'the', 'California', 'United', 'States']
    >>> new_item = ['Go', 'visit', 'latin', 'america', 'and', 'also', 'mexico', 'too.']
    >>> helper(new_item, 2)
    ['Go', 'visit', 'Latin', 'America', 'and', 'also', 'mexico', 'too.']
    >>> helper(new_item, 5)
    ['Go', 'visit', 'Latin', 'America', 'and', 'also', 'Mexico', 'too.']
    """
    if counter + 3 == len(phrase):
        if dict_check(phrase[counter+1]):
            short_list = (capitalize(phrase[counter+1]))
            phrase[counter+1] = short_list[0]
        elif dict_check(phrase[counter+2]):
            short_list = (capitalize(phrase[counter+2]))
            phrase[counter+2] = short_list[0]
        elif dict_check(phrase[counter+1:counter+3]):
            phrase[counter+1:counter+3] = capitalize(phrase[counter+1:counter+3])
    if dict_check(phrase[counter]):
        short_list = (capitalize(phrase[counter]))
        phrase[counter] = short_list[0]
    elif dict_check(phrase[counter:counter+2]):
        phrase[counter:counter+2] = capitalize(phrase[counter:counter+2])
    elif dict_check(phrase[counter:counter+3]):
        phrase[counter:counter+3] = capitalize(phrase[counter:counter+3])
    return phrase

def list_splitter_adder(old_lst, phrase, index):
    #replaces items from phrase one by one into old lst
    """
    >>> lst = ["The", "united", "states", "is", "beautiful."]
    >>> replacement = "United States"
    >>> list_splitter_adder(lst, replacement, 1)
    ['The', 'United', 'States', 'is', 'beautiful.']
    >>> list_splitter_adder(['I', 'once', 'visited', 'latin', 'america', 'in', 'winter.'], "Latin America", 3)
    ['I', 'once', 'visited', 'Latin', 'America', 'in', 'winter.']
    """
    phrase_list = phrase.split()
    for i in range(len(phrase_list)):
        old_lst[index+i] = phrase_list[i]
    return old_lst

def dict_check(words):
    #takes in a list, returns whether the words are in dictionary proper_nouns
    """
    >>> dict_check(["united", "states"])
    True
    >>> dict_check(["cdc"])
    True
    >>> dict_check(["united", "people"])
    False
    """
    if isinstance(words, list):
        words = " ".join(words)
    if words in proper_nouns:
        return True
    else:
        return False

def capitalize(words):
    #takes in a list of words that need to be replaced with their capitalized equivalents
    """
    >>> capitalize(["cdc"])
    ['CDC']
    >>> capitalize(["united", "states"])
    ['United', 'States']
    """
    if not isinstance(words, list):
        return proper_nouns.get(words).split()
    else:
        phrase = " ".join(words)
        return proper_nouns.get(phrase).split()
import random

def main():
    # Generate and print six sentences with different characteristics.
    sentences = [
        make_sentence(1, "past"),    # Single, past
        make_sentence(1, "present"), # Single, present
        make_sentence(1, "future"),  # Single, future
        make_sentence(2, "past"),    # Plural, past
        make_sentence(2, "present"), # Plural, present
        make_sentence(2, "future")   # Plural, future
    ]
    for sentence in sentences:
        print(sentence)

def make_sentence(quantity, tense):
    # Generate a sentence with a determiner, noun, verb, and two prepositional phrases.
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    adjective = get_adjective()
    verb = get_verb(quantity, tense)
    adverb = get_adverb()
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)

    # Combine parts into a full sentence.
    sentence = f"{determiner.capitalize()} {adjective} {noun} {verb} {adverb} {prepositional_phrase1} {prepositional_phrase2}."
    return sentence

def get_determiner(quantity):
    """Return a randomly chosen determiner based on quantity."""
    if quantity == 1:
        determiners = ["a", "the", "one"]
    else:
        determiners = ["some", "many", "the"]
    return random.choice(determiners)

def get_noun(quantity):
    """Return a randomly chosen noun based on quantity."""
    if quantity == 1:
        nouns = ["bird", "child", "car", "dog", "cat", "rabbit", "girl", "boy"]
    else:
        nouns = ["birds", "children", "cars", "dogs", "cats", "rabbits", "girls", "boys"]
    return random.choice(nouns)

def get_verb(quantity, tense):
    """Return a randomly chosen verb based on quantity and tense."""
    if tense == "past":
        verbs = ["talked", "drank", "laughed", "ran"]
    elif tense == "present":
        verbs = ["talks", "drinks", "laughs", "runs"] if quantity == 1 else ["talk", "drink", "laugh", "run"]
    elif tense == "future":
        verbs = ["will talk", "will drink", "will laugh", "will run"]
    return random.choice(verbs)

def get_preposition():
    """Return a randomly chosen preposition."""
    prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    ]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase."""
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    return f"{preposition} {determiner} {noun}"

def get_adjective():
    """Return a randomly chosen adjective."""
    adjectives = ["happy", "blue", "quick", "bright", "lazy", "funny", "curious", "brave"]
    return random.choice(adjectives)

def get_adverb():
    """Return a randomly chosen adverb."""
    adverbs = ["quickly", "happily", "lazily", "brightly", "curiously", "bravely", "quietly", "loudly"]
    return random.choice(adverbs)

if __name__ == "__main__":
    main()

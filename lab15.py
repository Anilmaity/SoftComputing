def make_word_classes(synom):
    # List of classes
    word_classes = []
    for w1, w2 in synom:
        # Go through existing classes
        for wcls in word_classes:
            # If one of the words is already in the current class
            if w1 in wcls or w2 in wcls:
                # Add both words and continue to next pair of words
                wcls.add(w1)
                wcls.add(w2)
                break
        else:  # Note this else goes with the for loop, not the if block
            # If there was no matching class, add a new one
            word_classes.append({w1, w2})
    return word_classes

synom = [("a", "b"), ("a", "c"), ("a", "d"), ("b", "e"), ("f", "e"), ("g", "h")]
word_classes = make_word_classes(synom)
print(word_classes)
# [{'a', 'c', 'b', 'd', 'f', 'e'}, {'h', 'g'}]

def sentences_are_equivalent(s1, s2, word_classes):
    # Split into words
    l1 = s1.split()
    l2 = s2.split()
    # If they have different sizes they are different
    if len(l1) != len(l2):
        return False
    # Go through each pair of corresponding words
    for w1, w2 in zip(l1, l2):
        # If it is the same word then it is okay
        if w1 == w2:
            continue
        # Go through list of word classes
        for wcls in word_classes:
            # If both words are in the same class it is okay
            if w1 in wcls and w2 in wcls:
                # Continue to next pair of words
                break
        else:  # Again, this else goes with the for loop
            # If no class contains the pair of words
            return False
    return True

s1 = "a e g"
s2 = "f c h"
print(sentences_are_equivalent(s1, s2, word_classes))
# True
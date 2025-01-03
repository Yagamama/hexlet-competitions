# https://leetcode.com/problems/sentence-similarity-iii/description/

# You are given two strings sentence1 and sentence2, each representing a sentence 
# composed of words. A sentence is a list of words that are separated by a single 
# space with no leading or trailing spaces. Each word consists of only uppercase and 
# lowercase English characters.

# Two sentences s1 and s2 are considered similar if it is possible to insert an 
# arbitrary sentence (possibly empty) inside one of these sentences such that the 
# two sentences become equal. Note that the inserted sentence must be separated 
# from existing words by spaces.

# For example,

# s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting 
# "my name is" between "Hello" and "Jane" in s1.
# s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there 
# is a sentence "s are" inserted into s1, it is not separated from "Frog" by a space.
# Given two sentences sentence1 and sentence2, return true if sentence1 and 
# sentence2 are similar. Otherwise, return false.

# Example 1:

# Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
# Output: true
# Explanation:
# sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".

# Example 2:

# Input: sentence1 = "of", sentence2 = "A lot of words"
# Output: false
# Explanation:
# No single sentence can be inserted inside one of the sentences to make it equal to the other.

# Example 3:
# Input: sentence1 = "Eating right now", sentence2 = "Eating"
# Output: true
# Explanation:
# sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.


def areSentencesSimilar(sentence1='', sentence2=''):
    if sentence1 == sentence2:
            return True
    if len(sentence1) < len(sentence2):
        if sentence2.startswith(sentence1+" ") or sentence2.endswith(" " + sentence1):
            return True
        s1 = sentence1.split()
        for i in range(1, len(s1)):
            if sentence2.startswith(' '.join(s1[:i])+" ") and sentence2.endswith(" " +' '.join(s1[i:])):
                return True
    else:
        if sentence1.startswith(sentence2+" ") or sentence1.endswith(" " + sentence2):
            return True
        s2 = sentence2.split()
        for i in range(1, len(s2)):
            if sentence1.startswith(' '.join(s2[:i])+' ') and sentence1.endswith(' '+' '.join(s2[i:])):
                return True
    return False


if __name__ == '__main__':
    print(areSentencesSimilar("My name is Haley", "My Haley"))  # True
    print(areSentencesSimilar("of", "A lot of words"))  # False
    print(areSentencesSimilar("Eating right now", "Eating"))  # True
    print(areSentencesSimilar("CwFfRo regR", "CwFfRo H regR"))  # True
    print(areSentencesSimilar("eTUny i b R UFKQJ EZx JBJ Q xXz", "eTUny i R EZx JBJ xXz"))  # False
    print(areSentencesSimilar("IfYgEidlr a QG kUqlcd J", 
                              "IfYgEidlr xFi a B QG kUqlcd J HVbknBM ngNyvJo efrpY"))  # False

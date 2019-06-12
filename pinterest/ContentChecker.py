"""
Imagine we have a blacklist that holds phrases that we want to filter out of the product. 
We maintain this list and use it to check whether pieces of text are considered safe or whether we should remove/scrub them.

Example:
"""
"""
blacklisted_phrases = [
  “machine guns”,
  “free ray bans”,
  “pornography”,
  “world war i”,
  “world war ii”
]
"""
"""
Note that the phrases could be single words or multiple word phrases, assume space delimited.

Questions
1) Given blacklisted_phrases, write a function(s) to mark a given text as safe/unsafe. 


E.g. (using the example blacklist above):

"Collection of my machine guns" - unsafe
"How to get free hotel upgrades" - safe
"Click here for free ray bans" - unsafe
"best pornography sites" - unsafe
"world war is best avoided" - safe
"""
class TrieNode:
    def __init__(self):
        self.child = {}
        self.isWord = True
        self.phrases = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    # o(l)
    def insertWordPhrasePair(self, word, phase):
        node = self.root
        for c in word:
            child = node.child.get(c, TrieNode())
            child.phrases.append(phase)
            node[c] = child
            node = child
            
        node.isWord = True
        
    def insertPhrase(self, phrase):
        for word in phrase.split():
            self.insertWordPhrasePair(word, phrase)
          
    # word length: l
    # O(l)
    def search(self, word):
        node = self.root
        for c in word:
            child = node.child.get(c)
            if not child:
                return False
            node = c
            
        return node.isWord, node.phrases
s
class ContentChecker:
    def __init__(self, blacklist):
        # l: each word average length
        # "word": 4
        # m lines, n words, m * n words, O(m * n * L)
        # context: k words, O(k)
        # O(k*m*n)
        # 100000 phrase
        self.blacklist = {word + str(index): phrase for word in phrase.split() for index, phrase in enumerate(blacklist)}
        
        
    def checkContent(self, context):
        if not self.blacklist:w
            return True
        
        for phraseSet in self.blacklist:
            
            # print('content set', set(context.split()))
            # print('phrase set', phrase.split())
            # if set(context.split()) >= set(phrase.split()):
                # return False
            '''
            if context.lower().find(phrase.lower()) != -1:
                print(phrase)
                return False
            '''
            
        return True

blacklisted_phrases = [
  'machine guns',
  'free ray bans',
  'pornography',
  'world war i',
  'world war ii'
]

# if you blacklist dictionary is all single words
# you want to match text, how to make the matching fast?
# 

contentChecker = ContentChecker(blacklisted_phrases)
print(contentChecker.checkContent('Collection of my machine guns') == False)
print(contentChecker.checkContent('How to get free hotel upgrades') == True)
print(contentChecker.checkContent('Click here for free ray bans') == False)
print(contentChecker.checkContent('best pornography sites') == False)
print(contentChecker.checkContent('world war is best avoided') == True)

import re

def retrieveMostFrequentlyUsedWords(literatureText, wordsToExclude):
    # WRITE YOUR CODE HERE
    if not literatureText:
        return []
        
    separatorPattern = re.compile('\W')
    words = separatorPattern.split(literatureText)
    
    wordFreq = {}
    result = []
    
    for w in words:
        if wordsToExclude and w in wordsToExclude:
            continue
        
        if w not in wordFreq:
            wordFreq[w] = 0
        else:
            wordFreq[w] += 1
            
    hightestFreq = hightestFreq = max(wordFreq.values())
    
    for word, freq in wordFreq.items():
        if freq == hightestFreq:
            result.append(word)
            
    return result


literatureText = "romeo romeo whereforce art thou romeo"
wordsToExclude = ["art", "thou"]
result = retrieveMostFrequentlyUsedWords(literatureText, wordsToExclude)   
print(result) 
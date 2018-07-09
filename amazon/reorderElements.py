import re
def reorderElements(logFileSize, logLines):
    # WRITE YOUR CODE HERE
    # It's super weird, I tested in my editor, it's working fine, but here, it's not, really strange
    if not logFileSize or not logLines:
        return []

    result = []
    wordLogLines, numberLogLines = separateLogLines(logLines)

    wordLogLines = sorted(wordLogLines, key=lambda strlist: ''.join(strlist[1:]))
    numberLogLines = sorted(numberLogLines, key=lambda intlist: ''.join([str(ele) for ele in intlist[1:]]))
    result.extend(wordLogLines)
    result.extend(numberLogLines)

    return result


def is_int(val):
    try:
        int(val)
        return True
    except:
        return False
        
def separateLogLines(logLines):
    if not logLines:
        return []

    wordLogLines = []
    numberLogLines = []

    for line in logLines:
        if len(line) > 1:
            if is_int(line[1]):
                numberLogLines.append(line)
            else:
                wordLogLines.append(line)

    return wordLogLines, numberLogLines


logFileSize = 5
logLines = [
    ['a1', 9, 2, 3, 1],
    ['g1', 'act', 'car'],
    ['zo4', 4, 7],
    ['ab1', 'off', 'key', 'dog'],
    ['a8', 'act', 'zoo']
]

logLines = [
    ['a1', 'alps', 'cow', 'bar'],
    ['mi2', 'jog', 'mid', 'pet'],
    ['wz3', 34, 54, 398],
    ['x4', 45, 21, 7]
]

result = reorderElements(logFileSize, logLines)
for l in result:
    print(l)


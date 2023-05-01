import json

def findAWordInDict(en, dict):
    if (en in dict):
        return dict[en]
    else:
        return ''

def addAWordInDict(key, value, dict):
    if (key not in dict):
        dict[key] = value
    return dict

def removeWordsFromDict(keys, dict):
    keys = keys.split(',')
    for key in keys:
        key = key.strip()
        if (key in dict):
            del dict[key]
    return dict

# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
# It used to store words in English and French pairs
# The words of dictionary is stored as JSON string in words.json file
file = open('words.json','r')
jsonStr = file.read()
file.close()
# dictEnFr = {'one':'une','two':'deux','three':'trois','four':'quatre','five':'cinq','six':'six'}
dictEnFr = json.loads(jsonStr)
print('Here is the current dictionary: ', dictEnFr)
delete = input('Do you want to remove words from the dictionary?(yes/no): ')
if (delete.lower() == 'yes' or delete.lower() == 'y'):
    wordsToRemove = input('Please type the words you want to remove, if you type multiple words, use "," to separate them: ')
    dictEnFr = removeWordsFromDict(wordsToRemove, dictEnFr)
    print('{} has been removed from the dictionary!'.format(wordsToRemove))
    print('Here is the current dictionary: ', dictEnFr)
print('Let''s start learning French: press enter to exist.')
# A while loop is used to wait for user's input, until user press enter
while (True):
    en = input('Please input an English word: ')
    if (en == ''):
        break
    # Call a procedure to return the translation, if not found, return a empty string
    fr = findAWordInDict(en, dictEnFr)
    if (fr != ''):
        print('The French translation for {} is {}.'.format(en , fr))
    else:
        print('No translation found for', en)
        # A while loop is used to wait for a valid French translation input
        while (fr == ''):
            fr = input('Please type the French translation for word {}: '.format(en))
            if (fr == ''):
                print('Invalid input!')
        # Call a procedure to add the new word into the dictionary
        dictEnFr = addAWordInDict(en, fr, dictEnFr)
        print('A new word is added to dictionary')
print('Learning finished.')
print('All words in the dictionary:', dictEnFr)
# Store dictionary in JSON string format into a file
jsonStr = json.dumps(dictEnFr)
file = open('words.json','w')
file.write(jsonStr)
file.close()
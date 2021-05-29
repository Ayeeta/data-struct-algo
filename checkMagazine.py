"""
1. count the number of words in magazine
2. match the word number in notes to the count number in magDict
3. If number of the given word is not equal return no
4. else check for case based on magazine

"""



def checkMagazine(magazine, note):
    magazineDict = {}
    mag = magazine.split()
    rnote = note.split()
    check = all(word in mag for word in rnote)
    if check is True:
        for i in range(len(mag)):
            magazineDict[mag[i]] = mag.count(mag[i])
        for i in range(len(rnote)):        
            if rnote.count(rnote[i]) <= magazineDict[rnote[i]]:
                return 'Yes'
            return 'No'
    return 'No'
   

print(checkMagazine("give me one grand today night", "give one some grand today"))
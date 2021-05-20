"""
1. count the number of words in magazine
2. match the word number in notes to the count number in magDict
3. If number of the given word is not equal return no
4. else check for case based on magazine

"""



def checkMagazine(magazine, note):
    magazineDict = {}
    mag = magazine.split()
    for i in range(len(mag)):
        magazineDict[mag[i]] = mag.count(mag[i])
    return magazineDict

print(checkMagazine("this is a two way street", "this is a two"))
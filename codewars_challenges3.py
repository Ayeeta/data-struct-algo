from urllib.parse import urlparse
import re

def non_repeating(string):  
    x = string.lower()
    for i in range(len(x)):
        if x.count(x[i]) == 1:
            return string[i]   

    

#print(non_repeating('Go hang a salami, I\'m a lasagna hog!'))

def domain_name(url):
    # domain_url = urlparse(url).netloc
    # print(domain_url)
    if url[0:3] == 'www':
        return url.split('.')[1]
    elif url[0:3] != 'http':
        return url.split('.')[0]
    domain_url = urlparse(url).netloc
    if domain_url[0:3] == 'www':
        return domain_url.split('.')[1]
    return domain_url.split('.')[0]


print(domain_name("github.com"))

def format_duration(duration_seconds):    
    hours, reminder = divmod(duration_seconds, 3600)
    minutes, seconds = divmod(reminder, 60)
    
    print('{} hours {} minutes {} seconds'.format(hours, minutes, seconds))


# format_duration(2)

def scramble(str1, str2):
    str3 = ''
    for l in str2:
        if l in str1 and str2.count(l) <= str1.count(l):
            str3 += l        
    print(str3)
    if str3 == str2:
        return True
    return False
# print(scramble('cedewaraaossoqqyt', 'codewars'))

def pig_it(sentence):
    sentence = sentence.split()
    sent = []
    for word in sentence:
        if word.isalpha() == True:
            w = word[1:]
            sent.append(w + word[0] +'ay')
        sent.append(word) 
    for w in sent:
        if w.isalpha() and w in sentence:
            sent.remove(w)  
    return ' '.join(sent)    

print(pig_it('Panem et circenses'))


#top_3 words. put the string in a set
#  and count the occurances of each word in a dictionary
#  return the list of dict keys with highest count
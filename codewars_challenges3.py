from urllib.parse import urlparse

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

def res

def format_duration(duration_seconds):    
    hours, reminder = divmod(duration_seconds, 3600)
    minutes, seconds = divmod(reminder, 60)
    
    print('{} hours {} minutes {} seconds'.format(hours, minutes, seconds))


format_duration(2)
    
from collections import Counter

def forcast():

    return ['snow','snow','snow','freezing rain','rain','fog','hail']

def lunch():
    return ['snow','snow','aaaa','bbbb']


breakfast_counter = Counter(forcast())
lunch_counter = Counter(lunch())
add_counter = breakfast_counter & lunch_counter
print(add_counter)



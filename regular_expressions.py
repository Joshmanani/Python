import re

patterns = ['term1', 'term2']
text = 'this is a string with only term1'

for pattern in patterns:
    print ("I'm searching for " + pattern)

    if re.search(pattern, text):
        print('we found your text in the sentence')
    else:
        print(' no match ')

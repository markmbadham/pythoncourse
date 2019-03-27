d = {}
for word in str.__doc__.split():
    word = word.strip(',.;:')
    #print word
    #print d
    if not word.isalpha(): continue
    if word in d: d[word] += 1
    else:  d[word] = 1
print 'word','count'
for key in d: print key, d[key]

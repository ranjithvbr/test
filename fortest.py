def count_dict(mystring):
    d = {}
# count occurances of character
    for w in mystring:
        d[w] = mystring.count(w)
# print the result
    for k in sorted(d):
        print (k + ': ' + str(d[k]))

mystring=raw_input('give the str: ')
count_dict(mystring)

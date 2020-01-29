def print_string(*words,sep=' ',end='\n'):
    strings=''
    for word in words:
        strings+=word+sep
    if end!='\n':
        print(strings[:-1]+end)
    else:
        print(strings[:-1])
print_string('This', 'is', 'a', 'test', ',', 'Yes', sep = '_', end = '.')
print_string('This', 'is', 'a', 'test')
print_string('This', 'is', 'a', 'test', sep = '-')
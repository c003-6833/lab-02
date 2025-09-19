with open('sample.txt', 'r') as f , open('copy.txt', 'w') as f2:
    for line in f :
        f2.write(line)


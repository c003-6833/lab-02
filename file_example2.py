with open('sample.txt', 'r') as f:
    number = 1
    for line in f:
        print(number , ":" , line.strip())
        number+=1
# Open 'sample.txt' for reading and 'copy.txt' for writing
with open('sample.txt', 'r') as source_file, open('copy.txt', 'w') as destination_file:
    for line in source_file:
        destination_file.write(line)

import string

with open('text.txt', 'w') as file:
    file.write('''-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer.
''')
punctuations = string.punctuation
punctuations_nums = 0
letters_nums = 0

with open('text.txt', 'r') as input_file, open('output.txt', 'a') as output_file :
    for index, line in enumerate(input_file):
        letters_nums = 0
        punctuations_nums = 0
        for s in line:

            if s.isalpha():
                letters_nums += 1
            elif s in punctuations:
                punctuations_nums += 1

        output_file.write(f'Line {index + 1}: {line.strip()} ({letters_nums})({punctuations_nums})\n')



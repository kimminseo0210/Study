import random

# create voca
vocab = {}

with open('C:\\Study\\Python\\CodeIt\\Voca\\vocabulary.txt','r') as f:
    for line in f:
        data = line.strip().split(": ")
        eng_word, kor_word = data[0], data[1]
        vocab[eng_word] = kor_word

# list of voca
keys = list(vocab.keys())

# Quiz voca
while True:
    # random list of voca
    index = random.randint(0, len(keys)-1)
    eng_word = keys[index]
    kor_word = vocab[eng_word]
    
    # user input
    answer = input(f'{eng_word}: ')
    
    # break Quiz
    if answer == 'q':
        break
    # check Quiz
    else:
        if answer == kor_word:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {kor_word}입니다")
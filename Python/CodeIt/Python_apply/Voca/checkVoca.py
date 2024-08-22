with open('C:\\Study\\Python\\CodeIt\\Voca\\vocabulary.txt','r') as f:
    for line in f:
        data = line.strip().split(": ")
        eng_word, kor_word = data[0], data[1]
        
        answer = input(f'{eng_word}: ')
        if answer == kor_word:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {kor_word}입니다")
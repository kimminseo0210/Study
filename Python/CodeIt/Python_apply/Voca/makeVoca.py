with open('C:\\Study\\Python\\CodeIt\\Voca\\vocabulary.txt','w') as f:
    
    while True:
        english = input("영어 단어를 입력하세요: ")
        if english == 'q':
            break
        
        korean = input("한국어 뜻을 입력하세요: ")
        
        f.write(f'{english}: {korean}\n')
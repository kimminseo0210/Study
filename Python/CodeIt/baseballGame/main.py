from random import randint
'''
def generate_numbers():
    numbers = []
    
    while len(numbers) < 3:
        rand_num = randint(0,9)
        if rand_num not in numbers:
            numbers.append(rand_num)
    
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers
'''
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    
    while len(new_guess) < 3:
        user_num = int(input(f"{len(new_guess)+1}번째 숫자를 입력하세요: "))
        
        if user_num > 9:
            print("범위 컷ㅋ")
        elif user_num in new_guess:
            print("중복임 ㅋ")
        else:
            new_guess.append(user_num)
    return new_guess


print(take_guess())
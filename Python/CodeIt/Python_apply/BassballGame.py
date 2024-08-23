from random import randint

def generate_numbers():
    numbers = []
    
    while len(numbers) < 3:
        rand_num = randint(0,9)
        if rand_num not in numbers:
            numbers.append(rand_num)
    
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

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

def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0
    
    for i in range(len(guesses)):
        if guesses[i] in solution:
            if guesses[i] == solution[i]:
                strike_count += 1
            else:
                ball_count += 1
    
    return strike_count, ball_count

ANSWER = generate_numbers()
tries = 0

while True:
    user_guess = take_guess()
    
    strike, ball = get_score(user_guess, ANSWER)
    
    print(f"{strike}S {ball}B")
    tries += 1
    
    if strike == 3:
        break

print(f"축하합니다. {tries}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.")
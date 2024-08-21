from random import randint

def generate_numbers(n):    # 로또 6자리 번호 생성
    numbers = []
    
    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    
    return numbers

def draw_winning_numbers(): # 추가 번호 1자리 생성
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

def count_matching_numbers(numbers, winning_numbers):   # 번호 매칭
    count = 0
    
    for num in numbers:
        if num in winning_numbers:
            count += 1
    
    return count

def check(numbers, winning_numbers):
    number_count = count_matching_numbers(numbers, winning_numbers[:6])
    bouns_count = count_matching_numbers(numbers, winning_numbers[6:])
    
    if number_count == 6:
        return 100000000
    elif number_count == 5 and bouns_count == 1:
        return 1000000
    elif number_count == 4:
        return 50000
    elif number_count == 3:
        return 5000
    else:
        return 0
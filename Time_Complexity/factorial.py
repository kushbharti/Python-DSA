def factorial(num):
    sum = 1
    for i in range(1,num+1):
        sum *= i 
    return sum

print(factorial(5))




def calc_factorial(num):
    answer = 1 
    while num > 1:
        answer *= num
        num -=1
    return answer

print(calc_factorial(5))
from math_module import my_div, my_sum, my_sub

print('Here are the results of your calculations:\n')

def main():
    div = my_div(6, 3)
    sum = my_sum(4, 2)
    sub = my_sub(60, 28)
    return print(f"The result of adding: {sum}, "
                 f"division: {div}, substraction: {sub}")

print("Give me two numbers in this format [a b], and I`ll do you math!")

def main():
    sum = my_sum(sum_a, sum_b)
    sub = my_sub(sub_a, sub_b)
    div = my_div(div_a, div_b)
    return print(f"Here are the result of adding: {sum}, "
                 f"substraction: {sub}, and division: {div}")


sum_a, sum_b = input('Two numbers to add up: ').split(' ')
sub_a, sub_b = input('Two numbers to substract: ').split(' ')
div_a, div_b = input('Two numbers to divide: ').split(' ')

# launching the programm.
if __name__ == '__main__':
    main()

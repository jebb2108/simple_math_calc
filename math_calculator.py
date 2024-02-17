from math_module import my_div, my_sum, my_sub

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

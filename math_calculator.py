from math_module import check_division, my_sum, my_sub

print('Here are the results of your calculations: ')

def main():
    division = check_division(6, 3)
    sum = my_sum(4, 2)
    sub = my_sub(60, 28)
    return print(sum, division, sub)


if __name__ == '__main__':
    main()

from math_module import my_div, my_sum, my_sub

print('Here are the results of your calculations: ')

def main():
    div = my_div(6, 3)
    sum = my_sum(4, 2)
    sub = my_sub(60, 28)
    return print(sum, div, sub)


if __name__ == '__main__':
    main()

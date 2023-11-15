
def reverse_list(my_list):

    if not my_list:
        return []
    if len(my_list) == 1:
        return [my_list[0]]
    else:
        return reverse_list(my_list[1:]) + [my_list[0]]


def main():
    print('Hello, world!')


if __name__ == '__main__':
    main()

data = [1,5,7]

print(reverse_list(data))
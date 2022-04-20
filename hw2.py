from random import choice


def get_random(input_list):
    if input_list:
        result = choice(input_list)
        return result


if __name__ == '__main__':
    print(get_random([1, 3, 5, 6, 6, 7]))
    print(get_random([]))

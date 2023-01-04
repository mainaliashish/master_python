# DRY principle

def say_hello(planet: str):
    '''
    info : Accepts planet name as string and returns a sentence
    @return : String
    '''
    return f"Hello world from {planet.title() if planet else 'Earth'}!"


def add_numbers(numbers: list):
    '''
    Info: This function accepts list of numbers and returns sum
    @return : sum
    '''
    sum = 0
    for number in numbers:
        sum += number
    return sum


def multiply_numbers(*args: int):
    '''
    info : This function accepts integers, multiply each numbers and returns the total
    @return : total
    '''
    return sum(args)
    total = 1
    for number in args:
        total *= number
    return total


# def sum(num_one, num_two):
#     '''
#     info : Accepts two numbers and return their sum
#     '''
#     def calculate_sum(n_one, n_two):
#         return n_one + n_two
#     return calculate_sum(num_one, num_two)


def check_even_or_odd(number):
    '''
    info : return whether number is odd or even
    '''
    if number % 2 == 0:
        return f"{number} is even number."
    return f"{number} is odd number."


def show_age(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} is {v} years old.")


def super_add(*args, **kwargs):
    total = 0
    for val in kwargs.values():
        total += val
    # print(F"kwargs : {total}")
    # print(sum(args) + total)
    return sum(args) + total


def highest_even(nums: list):
    # even_nums = [num for num in nums if num % 2 == 0]
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return max(even_nums)


if __name__ == '__main__':
    hello = say_hello('mars')
    print(hello)

    result = add_numbers(list(range(1, 6)))
    print(result)

    res = multiply_numbers(1, 2, 3, 4)
    print(res)

    # res = sum(10, 40)
    # print(res)

    # res = check_even_or_odd(4)
    # print(res)

    # for num in range(1, 40):
    #     print(check_even_or_odd(num))
    print("*" * 20)
    result = super_add(1, 2, 3, 4, 5, num_one=6, num_two=7)
    print(result)

    print(sum([1, 2, 3, 4, 5]))

    print(highest_even([1, 2, 3, 4, 5, 6, 7, 9, 20, 90]))

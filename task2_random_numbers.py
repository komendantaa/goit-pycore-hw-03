import random

# def validate_param(number: int, name: str):
#     if not isinstance(number, int):
#         raise TypeError(f"'{name}' should be an integer")
#     if number < 1 or number > 1000 :
#         raise ValueError(f"'{name}' should be more than 1 and less than 1000")


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if (min < 1) or (max > 1000) or (min >= max) or (max - min < quantity):
        return []

    result = []

    for _ in range(quantity):
        number = random.randint(min, max)
        while number in result:
            number = random.randint(min, max)
        result.append(number)

    result.sort()
    return result


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

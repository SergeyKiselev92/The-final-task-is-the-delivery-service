"""the_final_task_delivery_service."""


def number_of_platforms(data: list, expected_result: int) -> int:
    """Функция описывает основную логику кода.

    Задается счетчик, который будет считать сколько раз
    марсоход должен перевезти роботов.
    С помощью бесконечного цикла (условий заданных в нем)
    считается кол-во поездок марсохода,
    в зависимости от заданного лимита грузоподъемности
    платформы на одну поездку.
    """
    data = [int(item) for item in robots]
    sorted(data)
    count: int = 0
    left_pointer: int = 0
    right_pointer: int = len(data) - 1
    while left_pointer <= right_pointer:
        result: int = data[left_pointer] + data[right_pointer]
        if result == expected_result:
            right_pointer -= 1
            left_pointer += 1
        if result > expected_result:
            right_pointer -= 1
        else:
            if result < expected_result:
                left_pointer += 1
                right_pointer -= 1
        count += 1
    return count


if __name__ == "__main__":
    # Задается количество роботов
    robots = input().split()
    # Задается грузоподъемность платформы
    limit = int(input())
    print(number_of_platforms(robots, limit))

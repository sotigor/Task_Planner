from unittest import TestCase, main
from Functions import Funcs
from random import choice


class TempFuncs:

    @staticmethod
    def first_func():
        value = choice(list(range(9)))

        return value

    @staticmethod
    def second_func():
        return quit()

    @staticmethod
    def third_func():
        # value_id: int
        # format {value_id: [len(title) > 0, len(description) > 0, \
        # priority in range(1, 11), formatted(due_time) == DD.MM.YYYY]
        value_id = 24  # Some random value_id
        return {value_id: ["some_title", "some_description",
                           "6", "24.12.2024"]}

    @staticmethod
    def due_time_validation(due_time: str) -> bool:

        due_time_split = due_time.split('.')
        if len(due_time_split) == 3 \
                and sum(map(lambda data: len(data), due_time_split)) == 8:

            try:
                return 0 < int(due_time_split[0]) < 32 \
                       and 0 < int(due_time_split[1]) < 13 \
                       and 2022 <= int(due_time_split[2]) <= 2132
            except (ValueError, TypeError):
                return False

        return False


class TestFunctions(TestCase):

    def setUp(self):
        self.functions = Funcs()

    def test_first_func(self):
        value = self.functions.first_func()

        self.assertTrue(value in list(range(9)))

    def test_second_func(self):
        with self.assertRaises(SystemExit):
            self.functions.second_func()

    def test_third_function(self):
        result = self.functions.third_func()

        value_id, *_ = result
        title, description, priority, due_time = result[value_id]

        self.assertTrue(len(result) == 1)
        self.assertTrue(type(value_id) == int and value_id >= 0)
        self.assertTrue(type(title) == str and len(title) >= 3)
        self.assertTrue(type(title) == str and len(title) >= 5)
        self.assertTrue(type(priority) == str
                        and priority in list(map(str, (range(1, 11)))))
        self.assertTrue(self.functions.due_time_validation(due_time))


if __name__ == "__main__":
    main()

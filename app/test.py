"""
test class
"""


class TestCarsApi:
    def __init__(self, name):
        self.name = name

    def print_test(self):
        print(self.name)

    def print_blah(self, num: int):
        print("blah")
        print(self.print_test() * num)


if __name__ == "__main__":
    test_obj = TestCarsApi(name="Tesla")
    test_obj.print_blah(num=5)

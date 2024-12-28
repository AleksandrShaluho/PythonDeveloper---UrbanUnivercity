from random import choice

# class object as function
class MysticBall:
    def __init__(self, *strings):
        self.words = strings

    def __call__(self, *strings):
        return choice(self.words)

first_ball = MysticBall('Yes', 'No', 'Maybe')
print(first_ball())
print(first_ball())
print(first_ball())

# closure
def get_advanced_writer(file_name):
    def write_everything(*dataset):
        with open(file_name, 'w', encoding='utf-8') as file:
            for data in dataset:
                file.write(str(data) + '\n')

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# lambda function
first = 'Мама мыла раму'
second = 'Рамена мало было'
is_matching = lambda char1, char2: char1 == char2
print(list(map(is_matching, first, second)))

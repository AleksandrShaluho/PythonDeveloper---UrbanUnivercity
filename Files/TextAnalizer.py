from WordsFinder import *

finder1 = WordsFinder('test_file_1.txt')
print(finder1.get_all_words())
print(finder1.find('TEXT'))
print(finder1.count('teXT'))

finder2 = WordsFinder('Mother Goose - Monday’s Child.txt', 'Rudyard Kipling - If.txt',
                      'Walt Whitman - O Captain! My Captain!.txt')
print(finder2.get_all_words())
print(finder2.find('the'))
print(finder2.count('the'))

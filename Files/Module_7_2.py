def custom_write(filename, strings):
    file = open(filename,'a+',encoding='utf-8')
    strings_positions = dict()
    for string in strings:
        strings_positions[(strings.index(string)+1,file.tell())] = string
        file.write(string+'\n')
    file.close()
    return strings_positions

info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
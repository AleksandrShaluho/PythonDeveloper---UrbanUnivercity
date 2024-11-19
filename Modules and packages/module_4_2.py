def TestFunction():
    def InnerFunction():
        print('Я в области видимости функции TestFunction')

    InnerFunction()

TestFunction()

# InnerFunction()

def test_function():
    def inner_function():
        print(" в области видимости функции test_function")
    inner_function()

test_function()
inner_function()

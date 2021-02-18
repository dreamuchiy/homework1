def str_cmp(a, b):
    if type(a) != str or type(b) != str:
        return 0
    elif a == b:
        return 1
    elif len(a) > len(b):
        return 2
    elif b == 'learn':
        return 3
    # Вопрос с тотальностью мне по прежнему не очень ясен

print(str_cmp(42, "hello"))
print(str_cmp('', ''))
print(str_cmp("Lorem ipsum dolor sit amet", "learn"))
print(str_cmp("", "learn"))
print(str_cmp("", "python"))



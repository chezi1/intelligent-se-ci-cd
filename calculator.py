def divide_numbers(a, b):
    # 这是一个糟糕的除法实现，没有处理 b 为 0 的情况
    return a / b

def process_data(user_input):
    # 模拟一个处理数据的函数，使用了危险的 eval()
    result = eval(user_input)
    return result

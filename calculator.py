def divide_numbers(a, b):
    # 这是一个糟糕的除法实现，没有处理 b 为 0 的情况
    return a / b

def process_data(user_input):
    # 模拟一个处理数据的函数，使用了危险的 eval()
    result = eval(user_input)
    return result
    
def test_bug():
    # 故意放一个 eval 让大模型骂
    return eval("1+1")
def very_bad_function(user_input):
    # 这是一个极其危险的函数，绝对会被AI骂
    print("Running dangerous code...")
    return eval(user_input)

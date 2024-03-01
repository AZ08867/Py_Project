"""
match语句
接受一个表达式并把它的值与一个或多个 case 块给出的一系列模式进行比较。
类似 Rust 或 Haskell 中的模式匹配。
只有第一个匹配的模式会被执行，并且它还可以提取值的组成部分（序列的元素或对象的属性）赋给变量。
"""

# 最简单的形式是将一个主语值与一个或多个字面值进行比较，其中最后一个case _ 是作为通配符，必定会匹配成功


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403:
            return "Authentication required."
        case 404:
            return "Not found."
        case _:
            return "Something's wrong with the internet."


# print(http_error(401))

# 形如解包赋值的模式可被用于绑定变量,
# 第一个模式有两个字面值，与上述字面值模式类似
# 接下来的两个模式结合了一个字面值和一个变量，变量绑定了来自主语（point）的一个值。
# 第四个模式捕获了两个值，使其在概念上与解包赋值(x，y) = point 类似。

# point is an (x, y) tuple
# point = (3, 0)  # --> X = 3

# point = (0, 5)  # --> Y = 5

point = (3, 5)  # --> X = 3, Y = 5

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

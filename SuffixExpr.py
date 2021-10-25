from fractions import Fraction


class SuffixExpr:

    """
    中缀表达式转后缀
    """

    def __init__(self, expr):
        # 中缀表达式
        self.infix_expr = expr
        # 后缀表达式
        self.suffix_expr = self.toSuffix()
        # 表达式结果
        self.value = self.suffixExpr2Value()

    def calc(self, num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '×':
            return num1 * num2
        elif operator == '÷':
            if num2 == 0:
                return False
            return num1 / num2

    # 中缀表达式转换后缀表达式
    def toSuffix(self):
        # 后缀表达式
        suffix_list = []
        # 操作符列表
        operator_list = []
        # 操作符优先级
        operator_priority = {
            '+': 1,
            '-': 1,
            '×': 2,
            '÷': 2
        }
        if not self.infix_expr:
            return []
        infix_list = self.infix_expr.split(' ')
        for item in infix_list:
            if item in ['+', '-', '×', '÷']:
                while len(operator_list) >= 0:
                    if len(operator_list) == 0:
                        operator_list.append(item)
                        break
                    operator = operator_list.pop()
                    if operator == '(' or operator_priority[item] > operator_priority[operator]:
                        operator_list.append(operator)
                        operator_list.append(item)
                        break
                    else:
                        suffix_list.append(operator)
            elif item == '(':
                operator_list.append(item)
            elif item == ')':
                while len(operator_list) > 0:
                    operator = operator_list.pop()
                    if operator == '(':
                        break
                    else:
                        suffix_list.append(operator)
            else:
                suffix_list.append(item)

        while len(operator_list) > 0:
            suffix_list.append(operator_list.pop())

        self.suffix_expr = suffix_list
        return suffix_list

    def suffixExpr2Value(self):
        """
        表达式求值
        :return: result
        """
        value_list = []
        for item in self.suffix_expr:
            if item in ['+', '-', '×', '÷']:
                num2 = value_list.pop()
                num1 = value_list.pop()
                result = self.calc(num1, num2, item)
                if result == False or result < 0:
                    return False
                value_list.append(result)
            else:
                if item.find('/') > 0:
                    attach = 0
                    right = ''
                    if item.find("'") > 0:
                        parts = item.split("'")
                        attach = int(parts[0])
                        right = parts[1]
                    else:
                        right = item
                    parts = right.split('/')
                    result = Fraction(attach * int(parts[1]) + int(parts[0]), int(parts[1]))
                    value_list.append(result)
                else:
                    value_list.append(Fraction(int(item), 1))

        return value_list[0]
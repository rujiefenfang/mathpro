from BinTree import BinTree
from SuffixExpr import SuffixExpr
from fractions import Fraction
import random
import math
import os

class AutoGenerate:

    def __init__(self, operand_range, expr_sum):
        self.operator_sum = 3
        self.operator_range = operand_range
        self.expr_sum = expr_sum
        self.chance = random.randint(1, 10) / 100
        self.question_list = self.generateQuestion()
        self.normalizeExpr(self.question_list)

    def generateParentheses(self, expr, operand_num):
        """
        生成括号表达式
        :param
            exp: 表达式
            number_of_oprand: 运算符数目
        :return: 括号表达式
        """
        expr_list = []
        num = operand_num
        if expr:
            expr_len = len(expr)
            lposition = random.randint(0, int(num / 2))
            rposition = random.randint(lposition + 1, int(num / 2) + 1)
            idx = -1
            for i in range(expr_len):
                if expr[i] in ['+', '-', '×', '÷']:
                    expr_list.append(expr[i])
                else:
                    idx += 1
                    if idx == lposition:
                        expr_list.append('(')
                        expr_list.append(expr[i])
                    elif idx == rposition:
                        expr_list.append(expr[i])
                        expr_list.append(')')
                    else:
                        expr_list.append(expr[i])
        # 判断是否表达式左右都为括号，是则重新生成
        if expr_list[0] == '(' and expr_list[-1] == ')':
            expr_list = self.generateParentheses(expr, operand_num)
            return expr_list
        return expr_list

    def getOperandNum(self):
        """
        生成获取操作数，以及是否生成分数随机判断
        :return: ret :
        """
        operator_range = self.operator_range
        chance = self.chance
        chance *= 100
        chance = int(chance)
        flag = False
        ret = {}
        if self.getRandomNum(100) <= chance:
            operand_list = self.getRangeDec()
            ret['operand'] = operand_list[0] / operand_list[1]
            ret['operandString'] = self.Dec2String(operand_list)
            ret['operandList'] = [operand_list[0], operand_list[1]]
        else:
            operand = self.getRandomNum(operator_range)
            ret['operand'] = operand
            ret['operandString'] = str(operand)
            ret['operandList'] = [operand, 1]
        return ret

    def Dec2String(self, operand_list):
        oprand1 = operand_list[0]
        oprand2 = operand_list[1]
        if oprand2 == 1:
            return oprand1
        if oprand1 > oprand2:
            temp = int(oprand1 / oprand2)
            oprand1 -= (temp * oprand2)
            return str(temp) + "'" + str(oprand1) + "/" + str(oprand2)
        else:
            return str(oprand1) + "/" + str(oprand2)

    def getRangeDec(self):
        operator_range = self.operator_range
        while True:
            operand1 = self.getRandomNum(operator_range)
            operand2 = self.getRandomNum(operator_range)
            if(operand1 % operand2) == 0:
                continue
            else:
                break
        return self.simplifiedDec(operand1, operand2)

    def simplifiedDec(self, operand1, operand2):
        num = Fraction(operand1, operand2)
        num1 = int(num.numerator)
        num2 = int(num.denominator)
        return [num1, num2]

    def getFactorList(self, operator):
        list = []
        for i in range(2, operator + 1):
            if(operator % i) == 0:
                list.append(i)
        return list

    def getRandomNum(self, range):
        return random.randint(1, range)

    def getOperandSym(self, operand):
        operand_list = ['+', '-', '×', '÷']
        return operand_list[operand - 1]

    def normalizeExpr(self, expr_list):
        """
        规范化输出表达式
        :param exp_list: 表达式列表
        :return
        """
        if not expr_list:
            return
        if os.path.exists("question.txt"):
            with open("question.txt", "r+") as file:
                file.truncate(0)
        for i, expr in enumerate(expr_list):
            exp_string = "Question" + str(i+1) + ": " + expr + " =" + "\n"
            with open("question.txt", "a+", encoding = "utf-8") as file:
                file.write(exp_string)

    def isRepeat(self, expr_list, expr):
        """
        判断重复方法
        :param
            express_set: 表达式集合
            expression: 生成的表达式
        :return: True or False
        """
        suffixExpr = SuffixExpr(expr)
        generate_suffix_expr = suffixExpr.suffix_expr
        binTree = BinTree()
        generate_bin_tree = binTree.generate(generate_suffix_expr)
        for i in expr_list:
            suffixExpr2 = SuffixExpr(i)
            generate_suffix_expr2 = suffixExpr2.suffix_expr
            generate_bin_tree2 = binTree.generate(generate_suffix_expr2)
            if binTree.isEqual(generate_bin_tree) == binTree.isEqual(generate_bin_tree2):
                return True
        return False

    def generateOperation(self):
        operator_list = ['+', '-', '×', '÷']
        return operator_list[random.randint(0, len(operator_list) - 1)]

    def calc(self, expr):
        suffixExpr = SuffixExpr(expr)
        exprValue = str(suffixExpr.suffixExpr2Value())
        return exprValue

    def generateQuestion(self):
        expr_sum = self.expr_sum
        expr_list = []
        count = 0

        while count < expr_sum:
            random_operator_sum = random.randint(1, self.operator_sum)
            parenteses_flag = random.randint(0, 1)
            operator_sum = random_operator_sum + 1
            expr = []
            for i in range(random_operator_sum + operator_sum):
                if i % 2 == 0:
                    expr.append(self.getOperandNum()['operandString'])

                    if i > 1 and expr[i - 1] == '÷' and expr[i] == '0':
                        while True:
                            expr[i - 1] = self.generateOperation()
                            if expr[i - 1] == '÷':
                                continue
                            else:
                                break
                else:
                    expr.append(self.generateOperation())

                if i > 3:
                    if expr[i - 2] == '÷':
                        if expr[i - 1] > expr[i - 3]:
                            temp = expr[i - 1]
                            expr[i - 1] = expr[i - 3]
                            expr[i - 3] = temp
                    elif expr[i - 2] == '-':
                        if expr[i - 1] < expr[i - 3]:
                            temp = expr[i - 1]
                            expr[i - 1] = expr[i -3]
                            expr[i - 3] = temp

            if parenteses_flag and operator_sum != 2:
                expr = ' '.join(self.generateParentheses(expr, operator_sum))
            else:
                expr = ' '.join(expr)

            if self.expr_sum <= 500:
                if self.isRepeat(expr_list, expr):
                    continue
                else:
                    ret = self.calc(expr)
                    if ret == "False":
                        pass
                    else:
                        expr_list.append(expr)
                        count += 1
            else:
                ret = self.calc(expr)
                if ret == "False":
                    pass
                else:
                    expr_list.append(expr)
                    count += 1
        return expr_list



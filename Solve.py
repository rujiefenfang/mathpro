from SuffixExpr import SuffixExpr
import re
import os

class Solve:
    def __init__(self, question_file, solve_file):
        self.expr_list = []
        self.question_file = question_file
        self.solve_file = solve_file

    def getExprSolution(self, expr_list):
        self.expr_list = expr_list
        if os.path.exists('Answers.txt'):
            with open('Answers.txt', 'r+') as file:
                file.truncate(0)
        for i, expr in enumerate(self.expr_list):
            string = str(i + 1)
            suffixExpr = SuffixExpr(expr)
            expr_value = str(suffixExpr.suffixExpr2Value()) + '\n'
            ret = "Answers" + string + ': ' + expr_value
            with open('Answers.txt', 'a+', encoding = 'utf-8') as file:
                file.write(ret)
    def check_solve(self):
        wrongNum = 0
        rightNum = 0
        question_solution = []
        wrong_list = []
        right_list = []
        try:
            with open(self.question_file, 'r', encoding='utf-8') as file:
                for line in file:
                    expr_string = re.findall(r'Question\d+: (.*) =\n', line)
                    if expr_string:
                        expr = expr_string[0]
                    else:
                        continue
                    suffixExpr = SuffixExpr(expr)
                    expr_value = str(suffixExpr.suffixExpr2Value())
                    question_solution.append(expr_value)
        except IOError:
            print("请检查文件路径")

        try:
            with open(self.solve_file, 'r', encoding='utf-8') as file:
                for i, line in enumerate(file):
                    solve_string = re.findall(r'Answers\d+: (.*)\n', line)
                    if solve_string:
                        solve = solve_string[0]
                    else:
                        continue
                    if solve == question_solution[i]:
                        rightNum += 1
                        right_list.append(i + 1)
                    else:
                        wrongNum += 1
                        wrong_list.append(i + 1)
            with open('Grade.txt', 'w+', encoding='utf-8') as file:
                right_string = 'Right: ' + str(rightNum) + ' ' + str(right_list) + '\n'
                wrong_string = 'Wrong: ' + str(wrongNum) + ' ' + str(wrong_list) + '\n'
                file.write(right_string)
                file.write(wrong_string)
        except IOError:
            print("请检查文件路径")

if __name__ == '__main__':
    question_file = 'question.txt'
    solve_file = 'Answers.txt'
    solve = Solve(question_file, solve_file)
    solve.check_solve()

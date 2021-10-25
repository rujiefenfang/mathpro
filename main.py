from Solve import Solve
from AutoGenerate import AutoGenerate
from SuffixExpr import SuffixExpr
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="小学四则运算自动生成器")
    parser.add_argument('-n', '-na', type=str, help='控制生成题目的个数')
    parser.add_argument('-r', '-ra', type=str, help='题目中数值（自然数、真分数和真分数分母）的范围')
    parser.add_argument('-e', '-ea', type=str, default=" ", help='题目文件')
    parser.add_argument('-a', '-aa', type=str, default=" ", help='答案文件')
    args = parser.parse_args()

    if args.n is not None and args.r is not None:
        n = int(args.n)
        r = int(args.r)
        generate = AutoGenerate(r,n)
        print("题目已经生成，路径为question.txt")
        questions = generate.question_list
        questionPath = 'question.txt'
        AnswersPath = 'Answers.txt'
        if os.path.exists(questionPath) and os.path.exists(AnswersPath):
            solve = Solve(questionPath, AnswersPath)
            solve.getExprSolution(questions)
            print("答案已经生成，路径为Answers.txt")
    else:
        e = args.e
        e = e.strip()
        a = args.a
        a = a.strip()
        if os.path.exists(e) and os.path.exists(a):
            solve = Solve(e, a)
            print("核对答案")
            solve.check_solve()
            print("核对结果在Grade.txt")

if __name__ == '__main__':
    main()
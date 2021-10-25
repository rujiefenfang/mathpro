import os
import unittest
from unittest import TestCase
from AutoGenerate import AutoGenerate
from Solve import Solve
class temp():
    def test(solutionPath,questionPath,number,range):
        """
        :param solutionPath:
        :param questionPath:
        :param munber:
        :param range:
        """

        if number is not None and range is not None:
            n = int(number)
            r = int(range)
            generate = AutoGenerate(r, n)
            print("题目已经生成，路径为question.txt")
            questions = generate.question_list
            questionPath = 'question.txt'
            AnswersPath = 'Answers.txt'
            if os.path.exists(questionPath) and os.path.exists(AnswersPath):
                solve = Solve(questionPath, AnswersPath)
                solve.getExprSolution(questions)
                print("答案已经生成，路径为Answers.txt")
        else:
            if os.path.exists(questionPath) and os.path.exists(solutionPath):
                solve = Solve(questionPath, solutionPath)
                print("核对答案")
                solve.check_solve()
                print("核对结果在Grade.txt")



class Test(TestCase):

    def test1(self):
        #测试生成题目
        AnswersPath= 'Answers.txt'
        questionPath= 'question.txt'
        number= 100
        range= 100
        temp.test(AnswersPath,questionPath,number,range)
    def test2(self):
        #测试验证答案
        AnswersPath= 'Answers.txt'
        questionPath = 'question.txt'
        number = None
        range = None
        temp.test(AnswersPath, questionPath, number, range)

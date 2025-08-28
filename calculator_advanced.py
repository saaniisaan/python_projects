# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 13:49:57 2025

@author: saani
"""

class CalculatorError(Exception):
    pass

class Calculator:
    """ماشین حساب حرفه‌ای با پشتیبانی از عملیات اصلی"""
    
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise CalculatorError("تقسیم بر صفر امکان‌پذیر نیست")
        return a / b

    def run(self):
        print("ماشین حساب حرفه‌ای")
        while True:
            print("\nعملیات: +, -, *, / یا 'exit' برای خروج")
            op = input("عملیات را وارد کنید: ").strip()
            if op == "exit":
                print("خروج از برنامه...")
                break
            try:
                a = float(input("عدد اول: "))
                b = float(input("عدد دوم: "))
                if op == "+":
                    print("نتیجه:", self.add(a, b))
                elif op == "-":
                    print("نتیجه:", self.subtract(a, b))
                elif op == "*":
                    print("نتیجه:", self.multiply(a, b))
                elif op == "/":
                    print("نتیجه:", self.divide(a, b))
                else:
                    print("عملیات نامعتبر!")
            except ValueError:
                print("ورودی نامعتبر! لطفاً عدد وارد کنید.")
            except CalculatorError as e:
                print(e)


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
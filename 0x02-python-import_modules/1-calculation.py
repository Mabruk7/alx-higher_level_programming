#!/usr/bin/python3
a = 10
b = 5

from calculator_1.py import add, sub, mul, div

sum_result = add(a, b)
difference_result = sub(a, b)
product_result = mul(a, b)
division_result = div(a, b)

print(f"{a} + {b} = {sum_result}")
print(f"{a} - {b} = {difference_result}")
print(f"{a} * {b} = {product_result}")
print(f"{a} / {b} = {division_result}")
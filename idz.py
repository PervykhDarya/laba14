# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


def figure(type=0):
    def result(a, b):
        if type:
            return (a * b) / 2
        else:
            return a * b
    return result


if __name__ == "__main__":
    figure_type = int(input("0 - прямоугольник, 1 - треугольник: "))
    a, b = input("Введите два параметра фигуры: ").split()
    print(f"Площадь: {figure(figure_type)(int(a), int(b))}")

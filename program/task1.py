#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: подсчитайте количество гласных в строке, 
# введенной с клавиатуры с использованием множеств.


if __name__ == "__main__":
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    vowels_rus = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}

    string = input("Введите строку: ")

    count = 0

    for char in string.lower():
        if char in vowels or char in vowels_rus:
            count += 1

    print("Количество гласных в строке:", count)

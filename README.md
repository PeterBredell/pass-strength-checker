### Password Strength Checker

## Description
A Python tool to evaluate password strength based on length and complexity

## How to run and use
1. Clone the repo `git clone PeterBredell/pass-strength-checker'
2. Open command prompt in the directory of the pass.py file
3. Run: `python pass.py`
4. Enter your password that you want to test and recieve a strong alternative should your password be too weak.

## Why do strong passwords matter?
Passwords are our first line of defence and need to be strong enough for a threat actor to be inable to either guess or bruteforce your password.

This is why passwords need to consist of multiple special, lowercase, uppercase etc characters in order to make the lifes of threat actors as difficult as possible

38% of Americans report having at least one of their passwords cracked or guessed - This is a sign of a lack of knowledge on how to keep ourselves secure.

## What did I learn?

In this small project I learned:
Regular Expressions (re.search): Used regex to check for uppercase letters ([A-Z]), lowercase ([a-z]), digits (\d), and special characters, learning how to match patterns in strings efficiently.
String Module: Explored string.ascii_letters, string.digits, and string.punctuation to generate random, strong passwords with a diverse character set.
Join Method: Mastered ''.join() to combine random characters into a single password string, understanding separators and iterable handling.
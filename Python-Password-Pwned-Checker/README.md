# Python Pwned Password Checker

This quite cool Python program uses the 'Have I beeen pwned' database ([haveibeenpwned.com](haveibeenpwned.com) - thanks Troy Hunt!) to check if the input appears on a previous data leak.

Input a password. The program **hashes** it and sends the first 5 chars to the database, retreiving the matching leaked strings, following the **k-anonymity** technique.

It locally checks if there have been any leaks of that hashed password and returns either how many times that password was leaked or if it's not on the database.

Not: not being on the database does not necessarily mean that the password was not leaked NOR that the password is secure.


## How to use

On your CLI, run the program

`python3 password-checker.py password ...`


## Installation
This program uses inbuild libraries, so nothing extra is needed besides Python3


## Special note
I want to thank all those annonymous heroes that put code online, daily, as it was the internet who guided me to make this code and this short program a working one.
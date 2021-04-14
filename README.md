# Projekt polegający na stworzeniu własnego, prostego języka programowania.

Wymagania:
* Python 3
* llvm
* antlr:
```
$ pip install antlr4-python3-runtime
```

## Uruchomienie:

Przekompilowanie gramatyki:
```
$ antlr4 -Dlanguage=Python3 MyGrammar.g4
```
Uruchomienie kompilatora:
```
$ python main.py
```
Uruchomienie skompilowanego kodu:
```
$ lli-6.0 output.ll
```

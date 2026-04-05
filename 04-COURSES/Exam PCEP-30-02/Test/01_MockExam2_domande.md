# PCEP-30-02 — Section 1 Mock Exam #2
**Computer Programming and Python Fundamentals**
03/04/2026

---

**Q1.** Which of the following best describes a **semantic error** in a program?

A. The program contains a character sequence not recognized by the language  
B. The program violates the grammatical rules of the language  
C. The program runs without crashing but produces incorrect results  
D. The program attempts to execute an undefined keyword  

---

**Q2.** What is the output of the following code?

```python
print(9 % 4, 9 // 4)
```

A. `2 1`  
B. `1 2`  
C. `2 2`  
D. `1 1`  

---

**Q3.** Which of the following are **valid** Python identifiers? *(Select two)*

A. `2fast`  
B. `_speed`  
C. `class`  
D. `my_var_1`  
E. `my-var`  

---

**Q4.** What is the output of the following code?

```python
x = 4
y = 3
print(x ** y % 5)
```

A. `1`  
B. `64`  
C. `4`  
D. `19`  

---

**Q5.** Which of the following literals has type `float` in Python? *(Select two)*

A. `1e0`  
B. `1`  
C. `True`  
D. `1.0`  
E. `"1.0"`  

---

**Q6.** What is the output of the following code?

```python
x = 0o17
print(x)
```

A. `17`  
B. `15`  
C. `8`  
D. `23`  

---

**Q7.** What is the output of the following code?

```python
x = 5
x **= 2
x -= 1
print(x)
```

A. `26`  
B. `24`  
C. `9`  
D. `10`  

---

**Q8.** What is the output of the following code?

```python
print("Hello\nWorld")
```

A. `Hello\nWorld`  
B. `Hello World`  
C. `Hello` on one line, `World` on the next  
D. A `SyntaxError` is raised  

---

**Q9.** Which of the following expressions evaluates to `True`? *(Select two)*

A. `1 == True`  
B. `0 == True`  
C. `bool("") == False`  
D. `bool(0.0) == True`  
E. `False == 1`  

---

**Q10.** What is the output of the following code?

```python
print(2 + 3 == 5 and not False)
```

A. `False`  
B. `True`  
C. `1`  
D. A `TypeError` is raised  

---

**Q11.** What is the output of the following code?

```python
a = 0b1100
b = 0b1010
print(a ^ b)
```

A. `14`  
B. `6`  
C. `8`  
D. `12`  

---

**Q12.** Which of the following `print()` calls produces the output `1*2*3` ?

A. `print(1, 2, 3, sep="*")`  
B. `print(1, 2, 3, end="*")`  
C. `print(1*2*3)`  
D. `print("1", "2", "3", sep=",")`  

---

**Q13.** What is the output of the following code?

```python
x = 10
y = 3
print(x / y)
```

A. `3`  
B. `3.0`  
C. `3.3333333333333335`  
D. `3.33`  

---

**Q14.** Which of the following statements about Python **keywords** is correct?

A. Keywords can be used as variable names if assigned carefully  
B. Keywords are case-insensitive in Python 3  
C. Keywords are reserved words that cannot be used as identifiers  
D. New keywords can be defined using the `keyword` built-in function  

---

**Q15.** What is the output of the following code?

```python
x = ~5
print(x)
```

A. `5`  
B. `-5`  
C. `-6`  
D. `4`  

---

**Q16.** What is the output of the following code?

```python
x = "Python"
y = "3"
print(x + y * 2)
```

A. `Python33`  
B. `Python6`  
C. `PythonPython3`  
D. A `TypeError` is raised  

---

**Q17.** Which of the following correctly converts the string `"3.14"` to a float?

A. `float(int("3.14"))`  
B. `int("3.14")`  
C. `float("3.14")`  
D. `str(3.14)`  

---

**Q18.** What is the output of the following code?

```python
print(True + True + False)
```

A. `TrueTrueFalse`  
B. `2`  
C. `True`  
D. A `TypeError` is raised  

---

**Q19.** What is the output of the following code?

```python
x = 8
print(x >> 1)
```

A. `16`  
B. `4`  
C. `2`  
D. `1`  

---

**Q20.** Which of the following describes the difference between a **compiler** and an **interpreter**?

A. A compiler is faster at runtime because it translates on the fly; an interpreter pre-translates the whole program  
B. A compiler translates the entire source into machine code before execution; an interpreter translates and executes line by line  
C. Both produce identical executable files; the difference is only in the language used  
D. A compiler can only process Python; an interpreter handles all languages  

---

**Q21.** What is the output of the following code?

```python
x = 7
y = 2
print(x & y, x | y, x ^ y)
```

A. `2 7 5`  
B. `0 7 7`  
C. `3 6 5`  
D. `2 6 4`  

---

**Q22.** Which of the following variable names violates PEP-8 naming conventions for a constant? *(Select two)*

A. `MAX_SPEED`  
B. `maxSpeed`  
C. `max_speed`  
D. `MAXSPEED`  
E. `Max_Speed`  

---

**Q23.** What is the output of the following code?

```python
x = 0
print(bool(x), bool(x + 1), bool(""))
```

A. `False True False`  
B. `False True True`  
C. `True True False`  
D. `False False False`  

---

**Q24.** What is the output of the following code?

```python
name = input("Enter name: ")
print("Hello", name, sep=", ", end=".\n")
```

Assume the user types `Alice`.

A. `Hello Alice.`  
B. `Hello, Alice.`  
C. `Hello Alice`  
D. `Hello,Alice.`  

---

**Q25.** What is the output of the following code?

```python
print(1 < 2 < 3)
```

A. `False`  
B. A `SyntaxError` is raised  
C. `True`  
D. `1`  

---

Take your time. When ready, submit your answers in the format `Q1: B, Q2: A, ...` and we will review together.
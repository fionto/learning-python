# PCEP-30-02 — Section 1 Mock Exam #2
**Computer Programming and Python Fundamentals**
03/04/2026

---

**Q1.** Which of the following best describes a **semantic error** in a program?

C. The program runs without crashing but produces incorrect results  

---

**Q2.** What is the output of the following code?

```python
print(9 % 4, 9 // 4)
```

B. `1 2`  

---

**Q3.** Which of the following are **valid** Python identifiers? *(Select two)*

B. `_speed`  
D. `my_var_1`  

---

**Q4.** What is the output of the following code?

```python
x = 4
y = 3
print(x ** y % 5)
```

C. `4`  

---

**Q5.** Which of the following literals has type `float` in Python? *(Select two)*

A. `1e0`  
D. `1.0`  

---

**Q6.** What is the output of the following code?

```python
x = 0o17
print(x)
```

B. `15`  

---

**Q7.** What is the output of the following code?

```python
x = 5
x **= 2
x -= 1
print(x)
```

B. `24`  

---

**Q8.** What is the output of the following code?

```python
print("Hello\nWorld")
```

C. `Hello` on one line, `World` on the next  

---

**Q9.** Which of the following expressions evaluates to `True`? *(Select two)*

A. `1 == True`  
C. `bool("") == False`  

---

**Q10.** What is the output of the following code?

```python
print(2 + 3 == 5 and not False)
```

B. `True`  

---

**Q11.** What is the output of the following code?

```python
a = 0b1100
b = 0b1010
print(a ^ b)
```

A. `14`  

---

**Q12.** Which of the following `print()` calls produces the output `1*2*3` ?

A. `print(1, 2, 3, sep="*")`  

---

**Q13.** What is the output of the following code?

```python
x = 10
y = 3
print(x / y)
```

C. `3.3333333333333335`  

---

**Q14.** Which of the following statements about Python **keywords** is correct?

C. Keywords are reserved words that cannot be used as identifiers  

---

**Q15.** What is the output of the following code?

```python
x = ~5
print(x)
```

C. `-6`  

---

**Q16.** What is the output of the following code?

```python
x = "Python"
y = "3"
print(x + y * 2)
```

A. `Python33`  

---

**Q17.** Which of the following correctly converts the string `"3.14"` to a float?

C. `float("3.14")`  

---

**Q18.** What is the output of the following code?

```python
print(True + True + False)
```

C. `True`  

---

**Q19.** What is the output of the following code?

```python
x = 8
print(x >> 1)
```

B. `4`  

---

**Q20.** Which of the following describes the difference between a **compiler** and an **interpreter**?

B. A compiler translates the entire source into machine code before execution; an interpreter translates and executes line by line  

---

**Q21.** What is the output of the following code?

```python
x = 7
y = 2
print(x & y, x | y, x ^ y)
```

A. `2 7 5`  

---

**Q22.** Which of the following variable names violates PEP-8 naming conventions for a constant? *(Select two)*

B. `maxSpeed`  
C. `max_speed`  
E. `Max_Speed`  

---

**Q23.** What is the output of the following code?

```python
x = 0
print(bool(x), bool(x + 1), bool(""))
```

A. `False True False`  

---

**Q24.** What is the output of the following code?

```python
name = input("Enter name: ")
print("Hello", name, sep=", ", end=".\n")
```

Assume the user types `Alice`.

B. `Hello, Alice.`  

---

**Q25.** What is the output of the following code?

```python
print(1 < 2 < 3)
```

C. `True`  
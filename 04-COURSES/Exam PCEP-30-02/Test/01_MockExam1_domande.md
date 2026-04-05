# PCEP-30-02 — Section 1 Mock Exam
**Computer Programming and Python Fundamentals**
25 questions · Time suggested: 35 minutes

---

**Q1.** Which of the following best describes the role of a Python **interpreter**?

A. It translates the entire source file into machine code before execution begins  
B. It translates and executes the source code line by line at runtime  
C. It checks only the syntax of the code without running it  
D. It compiles the code into bytecode and stores it as a binary executable  

---

**Q2.** What is the output of the following code?

```python
print(2 ** 3 ** 2)
```

A. 512  
B. 64  
C. 6  
D. 729  

---

**Q3.** Which of the following are **valid Python keywords**? *(Select two)*

A. `True`  
B. `none`  
C. `elif`  
D. `switch`  
E. `until`  

---

**Q4.** What is the output of the following code?

```python
print(7 // 2, 7 % 2)
```

A. `3.5 1`  
B. `3 1`  
C. `4 1`  
D. `3 0`  

---

**Q5.** Which of the following variable names is **not** compliant with PEP-8 conventions for a simple local variable?

A. `total_sum`  
B. `TotalSum`  
C. `totalsum`  
D. `total_sum_2`  

---

**Q6.** What is the output of the following code?

```python
x = 10
x //= 3
print(x)
```

A. `3.33`  
B. `3`  
C. `4`  
D. `1`  

---

**Q7.** Which of the following literals represents the integer value **255** expressed in hexadecimal notation?

A. `0o255`  
B. `0b11111111`  
C. `0xFF`  
D. `255h`  

---

**Q8.** What is the output of the following code?

```python
print("ab" * 3 + "c")
```

A. `ababababc`  
B. `ababc`  
C. `ab3c`  
D. `abbbc`  

---

**Q9.** Which of the following statements about **indentation** in Python is true?

A. Indentation is optional and is used only for readability  
B. Python requires consistent indentation to define code blocks  
C. A block must be indented with exactly 4 spaces; tabs are not allowed  
D. Indentation applies only inside function definitions  

---

**Q10.** What is the output of the following code?

```python
print(0.1 + 0.2 == 0.3)
```

A. `True`  
B. `False`  
C. `None`  
D. A `TypeError` is raised  

---

**Q11.** What is the output of the following code?

```python
x = 5
y = 2
print(x & y)
```

A. `7`  
B. `0`  
C. `3`  
D. `1`  

---

**Q12.** Which of the following correctly reads a value from the user and stores it as an integer?

A. `x = input(int("Enter a number: "))`  
B. `x = int(input("Enter a number: "))`  
C. `x = integer(input("Enter a number: "))`  
D. `x = input("Enter a number: ", int)`  

---

**Q13.** What is the output of the following code?

```python
print(not True or False and True)
```

A. `True`  
B. `False`  
C. `None`  
D. A `SyntaxError` is raised  

---

**Q14.** Which of the following are **correct** ways to write a multi-line comment or note in Python? *(Select two)*

A. Using `//` at the start of each line  
B. Using `#` at the start of each line  
C. Enclosing the text in triple double-quotes `"""..."""` as an unassigned string literal  
D. Using `/* ... */` around the block  
E. Using `--` at the start of each line  

---

**Q15.** What is the output of the following code?

```python
print(type(3.0))
```

A. `<class 'int'>`  
B. `<class 'float'>`  
C. `<class 'double'>`  
D. `<class 'number'>`  

---

**Q16.** What is the output of the following code?

```python
x = 15
y = 4
print(x / y)
```

A. `3`  
B. `3.0`  
C. `3.75`  
D. `4.0`  

---

**Q17.** Which of the following values are of type **bool** in Python? *(Select two)*

A. `1`  
B. `True`  
C. `"True"`  
D. `False`  
E. `0.0`  

---

**Q18.** What is the output of the following code?

```python
print(2 + 3 * 4 - 1)
```

A. `19`  
B. `13`  
C. `24`  
D. `21`  

---

**Q19.** What is the output of the following code?

```python
x = "Hello"
print(x, "World", sep="-", end="!\n")
```

A. `Hello World!`  
B. `Hello-World!`  
C. `Hello-World`  
D. `Hello World`  

---

**Q20.** Which of the following correctly describes **lexical** errors in a programming language?

A. Errors arising from the wrong use of language constructs (e.g. dividing by zero)  
B. Errors caused by using character sequences that are not part of the language alphabet  
C. Errors due to logically incorrect algorithms  
D. Errors caused by incorrect indentation  

---

**Q21.** What is the output of the following code?

```python
print(int(3.9))
```

A. `4`  
B. `3`  
C. `3.9`  
D. A `ValueError` is raised  

---

**Q22.** What is the output of the following code?

```python
x = 0b1010
y = 0b0110
print(x | y)
```

A. `0`  
B. `14`  
C. `2`  
D. `16`  

---

**Q23.** Which of the following is a correct **scientific notation** literal in Python representing the value 0.0015?

A. `1.5E3`  
B. `1.5e-3`  
C. `15e-4`  — wait, this equals 0.0015 too  
D. Both B and C are correct  

---

**Q24.** What is the output of the following code?

```python
a = "3"
b = 2
print(a * b)
```

A. `6`  
B. `32`  
C. `33`  
D. `"3" * 2`  

---

**Q25.** Which of the following expressions evaluates to `True`? *(Select two)*

A. `5 != 5`  
B. `3 >= 3`  
C. `not False`  
D. `0 == False`  
E. `"" == False`  

---
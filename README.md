# SQL Parser using PLY (Python Lex-Yacc)

## Overview

This project implements a lightweight SQL-like query parser using **PLY (Python Lex-Yacc)**. It supports basic SQL operations such as:

* DELETE with WHERE conditions
* SELECT with GROUP BY
* JOIN operations

The parser performs:

* Lexical analysis (tokenization)
* Syntax parsing
* Error detection for invalid queries

---

## Features

* Case-insensitive SQL keyword recognition
* Custom grammar rules for SQL subsets
* Lexing and parsing error handling
* Structured output (AST-like tuples)

---

## Supported Queries

### DELETE

```
DELETE FROM employees WHERE id = 101
```

### SELECT with GROUP BY

```
SELECT dept FROM employees GROUP BY dept
```

### JOIN

```
table1 JOIN table2 ON id = dept_id
```

---

## Project Structure

```
sql-parser-ply/
│
├── main.py              # Runs sample queries
├── lexer_parser.py     # Lexer + Parser logic
├── requirements.txt
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Running the Project

```bash
python main.py
```

---

## Example Output

```
Query: DELETE FROM employees WHERE id = 101
Parsed: ('DELETE', 'employees', ('id', '=', 101))
```

---

## Concepts Used

* Compiler Design
* Lexical Analysis
* Parsing (Context-Free Grammars)
* Abstract Syntax Representation

---

## Future Improvements

* Support for INSERT and UPDATE
* Nested queries
* Full SQL grammar support

---

## Author:
Jaanhavi Ashwin Kher

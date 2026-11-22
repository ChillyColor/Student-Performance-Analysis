# Student Performance Analysis

A Python command-line project that analyzes student marks using NumPy. The program loads student records from a CSV file and reports class statistics, topper details, subject performance, pass/fail counts, and grade distribution.

## Features

- Load student IDs, names, and marks from a CSV dataset
- Calculate class and subject averages
- Find the highest and lowest student totals
- Identify the class topper
- Compare individual totals with the class average
- Identify the most difficult and easiest subjects
- Find students who fail in at least one subject or pass all subjects
- Calculate subject pass percentages
- Calculate grade percentages for the complete class

## Sample Dataset

The project includes 15 students and 5 subjects in `data/student_marks.csv`:

| Column | Description |
|---|---|
| `StudentID` | Unique student ID |
| `Name` | Student name |
| `Maths` | Mathematics marks |
| `Physics` | Physics marks |
| `Chemistry` | Chemistry marks |
| `ComputerScience` | Computer Science marks |
| `English` | English marks |

The pass mark used by the performance and subject-analysis functions is 35.

## Project Structure

```text
Student-Performance-Analysis/
├── data/
│   └── student_marks.csv
├── src/
│   ├── __init__.py
│   ├── analysis.py
│   └── data_loder.py
├── tests/
│   └── test_analysis.py
├── main.py
└── README.md
```

## Requirements

- Python 3.10 or later
- NumPy
- pytest

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ChillyColor/Student-Performance-Analysis.git
   cd Student-Performance-Analysis
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows:

   ```bash
   .venv\Scripts\activate
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install numpy pytest
   ```

## Run the Analysis

Run the program from the project root:

```bash
python main.py
```

The program prints the student count, subject count, class statistics, topper information, subject averages, pass/fail statistics, and grade distribution.

## Run Tests

Run the pytest suite from the project root:

```bash
python -m pytest -v
```

## NumPy Concepts Used

- Two-dimensional arrays
- Column stacking
- Array indexing and slicing
- Sum, mean, minimum, and maximum operations
- Axis-based calculations
- Boolean indexing
- `argmin`, `argmax`, `where`, `any`, and `all`
- Grade selection and percentage calculation

## Grading System

Grades are assigned according to each student's average mark:

| Average Marks | Grade |
|---:|:---:|
| 90 or above | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| 35–49 | E |
| Below 35 | F |

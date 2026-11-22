# Student Performance Analytics

A Python project built using **NumPy** to analyse student academic performance. It processes student marks across multiple subjects and generates useful statistics, performance insights, and grade distributions.

## Features

### 1. Data Loading
- Load student records from a CSV file.
- Separate student IDs, student names, subject names, and marks into NumPy arrays.
- Store marks in a 2D NumPy array for efficient numerical operations.

### 2. Basic Statistics
- Calculate total marks obtained by each student.
- Calculate average marks for each student.
- Calculate subject-wise average marks.
- Find the overall class average.
- Identify the highest and lowest total marks.

### 3. Student Performance Analysis
- Identify the class topper.
- Find students performing above the class average.
- Identify students scoring below a specified target.
- Find students who failed in at least one subject.
- Identify students who passed all subjects.
- Find students who failed in multiple subjects.

### 4. Subject Analysis
- Calculate average marks for each subject.
- Find the highest and lowest marks in each subject.
- Identify the easiest and most difficult subjects.
- Calculate subject-wise pass percentages.
- Identify the topper in each subject.

### 5. Grading System
- Assign grades based on students' average marks.
- Calculate the number of students in each grade.
- Calculate grade-wise percentages.

## Technologies Used

- **Python** – Programming language
- **NumPy** – Numerical computations and array operations
- **CSV** – Student dataset storage
- **Pytest** – Unit testing

## Project Structure

```text
Student_Performance_Analytics/
│
├── data/
│   └── student_marks.csv
│
├── src/
│   ├── __init__.py
│   ├── analysis.py
│   └── data_loder.py
│
├── tests/
│   └── test_analysis.py
│
├── main.py
├── README.md
└── requirements.txt
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd Student_Performance_Analytics
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Alternatively, install the dependencies individually:

```bash
pip install numpy pytest
```

## Running the Project

Run the main application from the project root directory:

```bash
python main.py
```

The application loads the student dataset, performs the analysis, and displays the results in the terminal.

## Running Unit Tests

The project uses Pytest to validate the analysis functions.

Run all tests from the project root directory:

```bash
python -m pytest -v
```

## Dataset

The project uses a CSV file named `student_marks.csv`.

The dataset contains the following columns:

| Column | Description |
|---|---|
| StudentID | Unique student identifier |
| Name | Student name |
| Maths | Mathematics marks |
| Physics | Physics marks |
| Chemistry | Chemistry marks |
| ComputerScience | Computer Science marks |
| English | English marks |

Each student is evaluated across five subjects.

## Concepts Practised

This project demonstrates practical usage of NumPy concepts, including:

- Array creation and data types
- Array indexing and slicing
- Array dimensions and shapes
- Aggregation functions (`sum`, `mean`, `min`, `max`)
- Axis-based operations
- Boolean indexing
- Conditional
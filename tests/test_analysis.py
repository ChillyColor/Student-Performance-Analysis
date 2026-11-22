import numpy as np
import pytest
from src.analysis import *


# Sample dataset: 5 students, 3 subjects

@pytest.fixture
def student_marks():
    return np.array([
        [90, 80, 70],
        [30, 20, 50],
        [35, 35, 35],
        [100, 100, 100],
        [60, 70, 80]
    ])


# ---------------- MODULE 2: BASIC STATISTICS ----------------

def test_calculateTotalMarks(student_marks):
    expected = np.array([240, 100, 105, 300, 210])
    result = calculateTotalMarks(student_marks)

    assert np.array_equal(result, expected)


def test_calculateAverageMarks(student_marks):
    expected = np.array([80, 100/3, 35, 100, 70])
    result = calcualteAverageMarks(student_marks)

    assert np.allclose(result, expected)


def test_calculateSubjectAverage(student_marks):
    expected = np.array([63, 61, 67])
    result = calculateSubjectAverage(student_marks)

    assert np.allclose(result, expected)


def test_calculateMaxMinMarksInEachSub(student_marks):
    expected_max = np.array([100, 100, 100])
    expected_min = np.array([30, 20, 35])

    result_max, result_min = calculateMaxMinMarksInEachSub(student_marks)

    assert np.array_equal(result_max, expected_max)
    assert np.array_equal(result_min, expected_min)


def test_calculateOverallAverage(student_marks):
    expected = 955 / 15
    result = calculateOverallAverage(student_marks)

    assert np.isclose(result, expected)


def test_calculateHighestTotalMarks(student_marks):
    assert calculateHighestTotalMarks(student_marks) == 300


def test_calculateLowestTotalMarks(student_marks):
    assert calculateLowestTotalMarks(student_marks) == 100


# ---------------- MODULE 3: STUDENT PERFORMANCE ----------------

def test_findTopper(student_marks):
    assert findTopper(student_marks) == 3


def test_calculateTopperMarks(student_marks):
    marks, average = calculateTopperMarks(student_marks, 3)

    assert marks == 300
    assert average == 100


def test_findFailure(student_marks):
    assert findFailure(student_marks) == 1


def test_findAboveAverage(student_marks):
    expected = np.array([0, 3, 4])
    result = findAboveAverage(student_marks)

    assert np.array_equal(result, expected)


def test_findbelowTarget(student_marks):
    expected = np.array([1, 2])
    result = findbelowTarget(student_marks, 200)

    assert np.array_equal(result, expected)


def test_topperInEachSubject(student_marks):
    expected = np.array([3, 3, 3])
    result = topperInEachSubject(student_marks)

    assert np.array_equal(result, expected)


def test_findFailedInAtleastOneSubject(student_marks):
    expected = np.array([1])
    result = findFailedInAtleastOneSubject(student_marks, 35)

    assert np.array_equal(result, expected)


def test_findStudentPassedAllSubjects(student_marks):
    expected = np.array([0, 2, 3, 4])
    result = findStudentPassedAllSubjects(student_marks)

    assert np.array_equal(result, expected)


# ---------------- MODULE 4: SUBJECT ANALYSIS ----------------

def test_findMostDifficultSubject(student_marks):
    assert findMostDifficultSubject(student_marks) == 1


def test_findEasiestSubject(student_marks):
    assert findEasiestSubject(student_marks) == 2


def test_findStudentsPassedAllSubjects(student_marks):
    expected = np.array([0, 2, 3, 4])
    result = findStudentsPassedAllSubjects(student_marks)

    assert np.array_equal(result, expected)


def test_findStudentsFailedMultipleSubjects(student_marks):
    expected = np.array([1])
    result = findStudentsFailedMultipleSubjects(student_marks)

    assert np.array_equal(result, expected)


def test_calculateSubjectPassPercentage(student_marks):
    expected = np.array([80, 80, 100])
    result = calculateSubjectPassPercentage(student_marks)

    assert np.allclose(result, expected)


# ---------------- MODULE 5: GRADING SYSTEM ----------------

def test_findGrade(student_marks):
    expected = np.array(["A", "F", "E", "A+", "B"])
    result = findGrade(student_marks)

    assert np.array_equal(result, expected)


def test_calculateStudentsInGrade(student_marks):
    expected_grades = np.array(["A", "A+", "B", "E", "F"])
    expected_counts = np.array([1, 1, 1, 1, 1])

    grades, counts = calculateStudentsInGrade(student_marks)

    assert np.array_equal(grades, expected_grades)
    assert np.array_equal(counts, expected_counts)


def test_calculateGradePercentage(student_marks):
    expected_grades = np.array(["A", "A+", "B", "E", "F"])
    expected_percentage = np.array([20, 20, 20, 20, 20])

    grades, percentage = calculateGradePercentage(student_marks)

    assert np.array_equal(grades, expected_grades)
    assert np.allclose(percentage, expected_percentage)
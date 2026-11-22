import numpy as np

def calculateTotalMarks(student_marks):
    totalMarks=np.sum(student_marks,axis=1)
    return totalMarks

def calcualteAverageMarks(student_marks):
    avgMarks=np.mean(student_marks,axis=1)
    return avgMarks

def calculateSubjectAverage(student_marks):
    avgSubject=np.mean(student_marks,axis=0)
    return avgSubject

def calculateMaxMinMarksInEachSub(student_marks):
    highestmarks=np.max(student_marks,axis=0)
    lowestmarks=np.min(student_marks,axis=0)
    return highestmarks,lowestmarks

def calculateOverallAverage(student_marks):
    classAverage=np.mean(student_marks)
    return classAverage

def calculateHighestTotalMarks(student_marks):
       subjectWiseTotalMarks=calculateTotalMarks(student_marks)
       return np.max(subjectWiseTotalMarks)
   
def calculateLowestTotalMarks(student_marks):
       subjectWiseTotalMarks=calculateTotalMarks(student_marks)
       return np.min(subjectWiseTotalMarks)

def findTopper(student_marks):
    totalMarks=calculateTotalMarks(student_marks)
    topperIdx=np.argmax(totalMarks)
    return topperIdx

def calculateTopperMarks(student_marks,idx):
    avgmarks=np.mean(student_marks[idx])
    marks=np.sum(student_marks[idx])
    return marks,avgmarks


def findFailure(student_marks,):
    totalMarks=calculateTotalMarks(student_marks)
    failureIdx=np.argmin(totalMarks)
    return failureIdx

def findAboveAverage(student_marks):
    totalMarks = calculateTotalMarks(student_marks)
    classAvg = np.mean(totalMarks)
    aboveAverage = np.where(totalMarks > classAvg)[0]
    return aboveAverage

def findbelowTarget(student_marks,target_marks):
    totalMarks = calculateTotalMarks(student_marks)
    belowTarget=np.where(totalMarks<target_marks)[0]
    return belowTarget

def topperInEachSubject(student_marks):
    topperIdx=np.argmax(student_marks,axis=0)
    return topperIdx

def findFailedInAtleastOneSubject(student_marks,target):
    failureIdx=np.where(np.any(student_marks<target,axis=1))[0]
    return failureIdx

def findStudentPassedAllSubjects(student_marks,target=35):
    passIdx=np.where(np.all(student_marks >=target,axis=1))[0]
    return passIdx

def findMostDifficultSubject(student_marks):
    avgMarksEach=np.mean(student_marks,axis=0)
    difficultSubject=np.argmin(avgMarksEach)
    return difficultSubject

def findEasiestSubject(student_marks):
    avgMarksEach=np.mean(student_marks,axis=0)
    easiestSubject=np.argmax(avgMarksEach)
    return easiestSubject

def findStudentsPassedAllSubjects(student_marks):
    passedAll=np.where(np.all(student_marks>=35,axis=1))[0]
    return passedAll

def findStudentsFailedMultipleSubjects(student_marks):
    booleanTable=student_marks<35
    simplifiedBooleanTable=np.sum(booleanTable,axis=1)
    failedMultiple=np.where(simplifiedBooleanTable > 1)[0]
    return failedMultiple

def calculateSubjectPassPercentage(student_marks,passingMarks=35):
    passedStudents=np.sum(student_marks>=passingMarks,axis=0)
    totalStudents=student_marks.shape[0]
    passPercentage=(passedStudents/totalStudents)*100
    return passPercentage
    
def findGrade(student_marks):
    meanMarks=np.mean(student_marks,axis=1)
    conditions = [
    meanMarks >= 90,
    meanMarks >= 80,
    meanMarks >= 70,
    meanMarks >= 60,
    meanMarks >= 50,
    meanMarks >= 35
    ]
    choices = ["A+", "A", "B", "C", "D", "E"]
    grades=np.select(conditions,choices,default="F")
    return grades

def calculateStudentsInGrade(student_marks):
    studentGrades=findGrade(student_marks)
    uniqueGrades,count=np.unique(studentGrades,return_counts=True)
    return uniqueGrades,count

def calculateGradePercentage(student_marks):
    grades,count=calculateStudentsInGrade(student_marks)
    totalStudents=student_marks.shape[0]
    percentageGrade=(count/totalStudents)*100
    return grades,percentageGrade
    
    

    
    


    
    
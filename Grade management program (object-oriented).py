##########
# 프로그램명: 성적관리 프로그램 (객체지향 버전)
# 작성자: 소프트웨어학부/윤영찬
# 작성일: 4/10
# 프로그램 설명: 학번, 이름, 영어, C언어, 파이썬 점수를 받아 총점, 평균, 학점, 등수를 계산하는 프로그램
##########

#학생 정보 객체
class Student:
    def __init__(self, student_id, name, english, c_language, python):
        self.student_id = student_id
        self.name = name
        self.english = english
        self.c_language = c_language
        self.python = python
        self.total = self.english + self.c_language + self.python
        self.average = self.total // 3
        self.grade = self.calculate_grade()
        self.rank = 0

#학점 계산기
    def calculate_grade(self):
        avg = self.average
        if avg > 90:
            return 'A+'
        elif avg == 90:
            return 'A'
        elif avg > 85:
            return 'A-'
        elif avg > 80:
            return 'B+'
        elif avg == 80:
            return 'B'
        elif avg >= 75:
            return 'B-'
        elif avg > 70:
            return 'C+'
        elif avg == 70:
            return 'C'
        elif avg >= 65:
            return 'C-'
        elif avg > 60:
            return 'D+'
        elif avg == 60:
            return 'D'
        elif avg > 55:
            return 'D-'
        else:
            return 'F'

#화면 출력
    def display(self):
        print(f"{self.student_id:<10} {self.name:<10} {self.english:>4} {self.c_language:>9} {self.python:>8} {self.total:>9} {self.average:>9} {self.grade:^14} {self.rank:>0}")

#정보 처리
class GradeManager:
    def __init__(self):
        self.students = []

    #학생 정보 입력
    def input_student(self):
        student_id = input("학번: ")
        name = input("이름: ")
        english = int(input("영어: "))
        c_language = int(input("C-언어: "))
        python = int(input("파이썬: "))
        student = Student(student_id, name, english, c_language, python)
        self.students.append(student)

    #등수 계산기
    def calculate_ranks(self):
        totals = [s.total for s in self.students]
        sorted_totals = sorted(set(totals), reverse=True)
        rank_dict = {score: rank + 1 for rank, score in enumerate(sorted_totals)}
        for s in self.students:
            s.rank = rank_dict[s.total]

    #출력 화면
    def display_all(self):
        print("                                    성적관리 프로그램                                   ")
        print("=======================================================================================")
        print("학번        이름          영어     C-언어   파이썬     총점      평균      학점    등수")
        print("=======================================================================================")
        for student in self.students:
            student.display()

# 메인 함수
def main():
    manager = GradeManager()
    for _ in range(5):
        manager.input_student()
    manager.calculate_ranks()
    manager.display_all()

main()

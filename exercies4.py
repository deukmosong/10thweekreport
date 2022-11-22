class Student:
    def __init__(self,name,studentid):
        self.__name=name
        self.__student_id=studentid
        self.__korean_quiz=0
        self.__math_quiz=0
        self.__science_quiz=0
        self.__total_score=0
    def __str__(self):
        return '이름 :'+self.__name+'학번 :'+self.__student_id+'\n국어성적:'+str(self.__korean_quiz)+'수학성적:'+str(self.__math_quiz)+'과학성적:'+str(self.__science_quiz)+'\n합계:'+str(self.__total_score)+'평균='+str(self.__total_score/3)

    def get_name(self):
        return self.__name
    def get_student_id(self):
        return self.__student_id
    def korean_quiz(self):
        return self.__korean_quiz
    def manth_quiz(self):
        return self.__math_quiz
    def science_quiz(self):
        return self.__science_quiz
    def set_korean_quiz(self,score):
        self.__total_score+=score
        self.__korean_quiz=score
    def set_maht_quiz(self,score):
        self.__total_score+=score
        self.__math_quiz=score
    def set_science_quiz(self,score):
        self.__total_score+=score
        self.__science_quiz=score
    def get_total_score(self):
        return self.__totla_score
    def get_ave_score(self):
        return self.__total_score/3

name=input('학생의 이름을 입력하세요:')
studentid=input('학생의 학번을 입력하세요:')
student=Student(name,studentid)
korean_quiz=int(input('학생의 국어 성적을 입력하세요:'))
math_quiz=int(input('학생의 수학 성적을 입력하세요:'))
science_quiz=int(input('학생의 과학 성적을 입력하세요:'))
student.set_korean_quiz(korean_quiz)
student.set_maht_quiz(math_quiz)
student.set_science_quiz(science_quiz)
print(student)




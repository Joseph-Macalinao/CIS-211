from typing import List, Set, Dict, Optional


class Student:
    def __init__(self, name: str, interests: List[str]):
        self.name = name
        self.interests = interests
        self.freetimes = set([8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.meetings: List[int] = []

    def schedule_meeting(self, time: int):
        if time in self.freetimes:
            self.meetings.append(time)
            self.freetimes.remove(time)

    def get_freetimes(self):
        return self.freetimes


class Club:
    def __init__(self, name: str):
        self.name = name
        self.members: List[Student] = []
        self.meeting_time: Optional[int] = None

    def join(self, student: Student):
        self.members.append(student)

    def find_common_time(self) -> int:
        index = 0
        #student_0 = self.members[0].freetimes
        free = []
        for student_free_check in self.members:
            free.append(student_free_check.freetimes)
        for i in free:
            for e in i:
                for j in free:
                    if e not in j:
                        pass
                return e

        return 0

    def schedule(self, time: int):
        self.meeting_time = time



class ASUO:
    def __init__(self):
        self.students: List[Student] = []
        self.clubs: List[Club] = []

    def enroll(self, student: Student):
        self.students.append(student)


s1 = Student("joe",[])
s2 = Student("joe",[])
s3 = Student("joe",[])
s4 = Student('joe',[])

c1 = Club('joe club')
c2 = Club('moe club')
c1.join(s1)
c1.join(s2)
c1.join(s3)
c2.join(s2)
c2.join(s4)
print(c2.find_common_time())

# for i in self.members:
#     free = i.get_freetimes()
#     for e in free:
#         if e in student_0:
#             return e

# if set.isdisjoint(student_0, free):
#     return 0
# else:
#     while True
# for e in self.members:
#     if any(item in free for item in e.freetimes):
#         return item
# check = any(item in i.freetimes for item in i.freetimes)
# return check
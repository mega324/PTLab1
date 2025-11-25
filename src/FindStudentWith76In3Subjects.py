# -*- coding: utf-8 -*-
from Types import DataType


class FindStudentWith76In3Subjects:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def find(self) -> str:
        for student, subjects in self.data.items():
            count_76_plus = 0
            for subject, score in subjects:
                if score >= 76:
                    count_76_plus += 1
            if count_76_plus >= 3:
                return student
        return "Студентов с 76+ баллами по 3+ предметам не найдено"

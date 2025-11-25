# -*- coding: utf-8 -*-
from src.Types import DataType
from src.FindStudentWith76In3Subjects import FindStudentWith76In3Subjects
import pytest


class TestFindStudentWith76In3Subjects:

    @pytest.fixture()
    def input_data(self) -> DataType:
        data: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 80),
                ("программирование", 90),
                ("литература", 76)
            ],
            "Петров Петр Петрович": [
                ("математика", 100),
                ("социология", 90),
                ("химия", 61)
            ],
            "Сидоров Алексей Николаевич": [
                ("математика", 76),
                ("физика", 76),
                ("химия", 76),
                ("биология", 80)
            ],
            "Кузнецова Мария Сергеевна": [
                ("математика", 75),
                ("физика", 77),
                ("химия", 79)
            ]
        }
        return data

    def test_find_student_exists(self, input_data: DataType) -> None:
        finder = FindStudentWith76In3Subjects(input_data)
        result = finder.find()
        # Может найти любого студента с 3+ предметами 76+
        # Проверяем, что результат не сообщение об отсутствии
        assert result != "Студентов с 76+ баллами по 3+ предметам не найдено"
        assert result in ["Иванов Иван Иванович", "Сидоров Алексей Николаевич"]

    def test_find_student_not_exists(self) -> None:
        data: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 75),
                ("программирование", 75),
                ("литература", 75)
            ]
        }
        finder = FindStudentWith76In3Subjects(data)
        result = finder.find()
        assert result == "Студентов с 76+ баллами по 3+ предметам не найдено"

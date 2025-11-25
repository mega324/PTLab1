# -*- coding: utf-8 -*-
import argparse
import sys
import os

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from YamlDataReader import YamlDataReader
from FindStudentWith76In3Subjects import FindStudentWith76In3Subjects


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    # Выбор в зависимости от расширения файла
    _, file_extension = os.path.splitext(path)
    if file_extension.lower() in ['.yaml', '.yml']:
        reader = YamlDataReader()
    else:
        reader = TextDataReader()

    students = reader.read(path)
    print("Students: ", students)

    # Расчет рейтинга
    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    # Поиск студента с 76+ баллами по 3+ предметам
    finder = FindStudentWith76In3Subjects(students)
    result = finder.find()
    print("Student with 76+ in 3+ subjects:", result)


if __name__ == "__main__":
    main()
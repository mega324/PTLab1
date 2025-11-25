# -*- coding: utf-8 -*-
import yaml
from Types import DataType
from DataReader import DataReader


class YamlDataReader(DataReader):

    def read(self, path: str) -> DataType:
        with open(path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        
        if data is None:
            return {}
            
        students: DataType = {}
        for student_name, subjects in data.items():
            students[student_name] = []
            for subject, score in subjects.items():
                students[student_name].append((subject, score))
        
        return students
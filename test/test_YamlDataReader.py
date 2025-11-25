# -*- coding: utf-8 -*-
import pytest
import os
from src.Types import DataType
from src.YamlDataReader import YamlDataReader


class TestYamlDataReader:

    def test_read_from_file(self, tmpdir) -> None:
        # Создаем временный YAML файл
        yaml_content = """Иванов Иван Иванович:
  математика: 91
  химия: 100
Петров Петр Семенович:
  русский язык: 87
  литература: 78
"""
        p = tmpdir.mkdir("datadir").join("test_data.yaml")
        with open(str(p), 'w', encoding='utf-8') as f:
            f.write(yaml_content)

        expected_data = {
            "Иванов Иван Иванович": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87), ("литература", 78)
            ]
        }

        # Тестируем чтение
        reader = YamlDataReader()
        result = reader.read(str(p))
        assert result == expected_data

    def test_read_empty_file(self, tmpdir) -> None:
        p = tmpdir.mkdir("datadir").join("empty.yaml")
        with open(str(p), 'w', encoding='utf-8') as f:
            f.write("")

        reader = YamlDataReader()
        result = reader.read(str(p))
        assert result == {}

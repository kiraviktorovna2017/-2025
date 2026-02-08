# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from datetime import datetime
from typing import Optional

class Table:
    """
        Класс, описывающий стол.

        :param material: Материал стола (например, 'дерево', 'металл')
        :param length: Длина стола в метрах
        :param width: Ширина стола в метрах

        :raises TypeError: Если material не строка, length/width не числа
        :raises ValueError: Если length или width отрицательны

        Примеры:
        >>> table = Table('дерево', 1.5, 0.8)
        >>> table.calculate_area()
        1.2
        >>> table.is_large_table(1.0)
        True
        """
    def _init_(self, material: str, length: float, width: float):
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError("Длина и ширина должны быть числами")
        if length < 0 or width < 0:
            raise ValueError("Длина и ширина не могут быть отрицательными")

        self.material = material
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        """
        Вычисляет площадь стола.
        :return: Площадь стола в квадратных метрах
        Примеры:
        >>> table = Table('дерево', 2.0, 1.0)
        >>> table.calculate_area()
        2.0
        """
        return self.length * self.width

    def is_large_table(self, threshold: float) -> bool:
        """
        Проверяет, является ли стол большим (площадь > threshold).
        :param threshold: Пороговая площадь
        :return: True, если площадь больше threshold
        """
        return self.calculate_area() > threshold
class SocialMediaProfile:
    """
        Класс, описывающий профиль в социальной сети.

        :param username: Имя пользователя
        :param followers: Количество подписчиков
        :param is_verified: Флаг верификации

        :raises TypeError: Если username не строка, followers не целое, is_verified не булево
        :raises ValueError: Если followers отрицательный

        Примеры:
        >>> profile = SocialMediaProfile('john_doe', 1000, False)
        >>> profile.add_follower()
        >>> profile.followers
        1001
        >>> profile.verify_profile()
        >>> profile.is_verified
        True
        """

    def _init_(self, username: str, followers: int, is_verified: bool):
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть строкой")
        if not isinstance(followers, int):
            raise TypeError("Количество подписчиков должно быть целым числом")
        if not isinstance(is_verified, bool):
            raise TypeError("Флаг верификации должен быть булевым значением")
        if followers < 0:
            raise ValueError("Количество подписчиков не может быть отрицательным")

        self.username = username
        self.followers = followers
        self.is_verified = is_verified

    def add_follower(self) -> None:
        """
        Добавляет одного подписчика.

        Примеры:
        >>> profile = SocialMediaProfile('jane_doe', 500, False)
        >>> profile.add_follower()
        >>> profile.followers
        501
        """
        self.followers += 1

    def verify_profile(self) -> None:
        """
        Верифицирует профиль.

        Примеры:
        >>> profile = SocialMediaProfile('admin', 10000, False)
        >>> profile.verify_profile()
        >>> profile.is_verified
        True
        """
        self.is_verified = True
class Student:
    """
    Класс, описывающий студента учебного заведения.

    :param name: Имя студента
    :param group_number: Номер учебной группы
    :param graduation_year: Год окончания обучения

    :raises TypeError: Если name не строка, group_number не строка/число, graduation_year не целое число
    :raises ValueError: Если имя пустое, номер группы пустой или год окончания меньше текущего года

    Примеры:
    >>> student = Student('Анна Каренина', 'ИТ-202', 2027)
    >>> student.years_remaining()
    1
    >>> student.get_info()
    'Студент: Анна Каренина, группа: ИТ-202, окончание: 2027 г.'
    """
    def _init_(self, name: str, group_number: str, int, graduation_year: int):
        if not isinstance(name, str) or not name.strip():
            raise TypeError("Имя должно быть непустой строкой")
        if not isinstance(group_number, (str, int)):
            raise TypeError("Номер группы должен быть строкой или числом")
        if not isinstance(graduation_year, int):
            raise TypeError("Год окончания должен быть целым числом")

        group_str = str(group_number).strip()
        if not group_str:
            raise ValueError("Номер группы не может быть пустым")
        if graduation_year < datetime.now().year:
            raise ValueError(f"Год окончания не может быть меньше текущего года ({datetime.now().year})")

        self.name = name.strip()
        self.group_number = group_str
        self.graduation_year = graduation_year
    def years_remaining(self) -> int:
        """
        Рассчитывает, сколько лет осталось учиться студенту.

        :return: Количество полных лет до окончания обучения (0 или больше)

        Примеры:
        >>> student = Student('Иван Иванов', 'ФМ-101', 2028)
        >>> student.years_remaining()  # при текущем годе 2026
        2
        >>> graduate = Student('Мария Сидорова', 'ВКГ-55', 2026)
        >>> graduate.years_remaining()
        0
        """
        current_year = datetime.now().year
        remaining = self.graduation_year - current_year
        return max(0, remaining)
    def change_group(self, new_group: str, int) -> None:
        """
        Изменяет номер учебной группы студента.

        :param new_group: Новый номер группы (строка или число)

        :raises TypeError: Если новый номер группы имеет неверный тип
        :raises ValueError: Если новый номер группы пустой

        Примеры:
        >>> student = Student('Петр Смирнов', 'БИ-303', 2027)
        >>> student.change_group('БИ-304')
        >>> student.group_number
        'БИ-304'
        >>> student.change_group('')
        Traceback (most recent call last):
        ...
        ValueError: Новый номер группы не может быть пустым
        """
        if not isinstance(new_group, (str, int)):
            raise TypeError("Новый номер группы должен быть строкой или числом")
        
        new_group_str = str(new_group).strip()
        if not new_group_str:
            raise ValueError("Новый номер группы не может быть пустым")
        
        self.group_number = new_group_str

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest


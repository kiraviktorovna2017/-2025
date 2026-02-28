class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
            return self._name

    @property
    def author(self):
            return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages
    @property
    def pages(self):
        return self._pages
    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value < 0:
            raise ValueError("Количество страниц не может быть отрицательным")
        self._pages = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Страниц: {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration
    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность не может быть нулевой или отрицательной")
        self._duration = float(value)

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность: {self._duration} часов"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"
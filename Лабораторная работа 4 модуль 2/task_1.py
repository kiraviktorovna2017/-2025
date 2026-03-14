class Cosmetics:
    def __init__(self, brand, product_name, volume, expiration_date):
        self.brand = brand
        self.product_name = product_name
        self.volume = volume
        self.expiration_date = expiration_date
        self.is_active = True  # если True — средство можно использовать

    def check_expiration(self, current_date):
        from datetime import datetime
        exp_date = datetime.strptime(self.expiration_date, "%m.%Y")
        curr_date = datetime.strptime(current_date, "%m.%Y")
        if curr_date > exp_date:
            self.is_active = False
            return True
        return False

    def use_product(self, amount):
        if self.is_active and amount <= self.volume:
            self.volume -= amount
            print(f"Использовано {amount} мл {self.product_name}. Осталось: {self.volume} мл.")
        elif not self.is_active:
            print(f"{self.product_name} просрочено! Использовать нельзя.")
        else:
            print(f"В {self.product_name} меньше {amount} мл — нельзя использовать столько.")


class SkincareCosmetics(Cosmetics):  # уходовая косметика
    def __init__(self, brand, product_name, volume, expiration_date, skin_type, active_ingredient):
        super().__init__(brand, product_name, volume, expiration_date)
        self.skin_type = skin_type
        self.active_ingredient = active_ingredient
        self.__ph_level = 5.5  # уровень pH (скрытый параметр)

    def adjust_ph(self, new_ph):
        if 4.0 <= new_ph <= 7.0:
            self.__ph_level = new_ph
            print(f"pH {self.product_name} изменён на {self.__ph_level}.")
        else:
            print("Ошибка! pH должен быть от 4.0 до 7.0.")

    def get_ph_level(self):
        return self.__ph_level


class DecorativeCosmetics(Cosmetics):  # декоративная косметика
    def __init__(self, brand, product_name, volume, expiration_date, product_type, shade):
        super().__init__(brand, product_name, volume, expiration_date)
        self.product_type = product_type
        self.shade = shade
        self._waterproof = False  # водостойкость (защищённый параметр)

    def set_waterproof(self, is_waterproof):
        self._waterproof = is_waterproof
        status = "водостойкий" if self._waterproof else "не водостойкий"
        print(f"{self.product_name} теперь {status}.")

    def apply_product(self):
        if self.is_active:
            print(f"Нанесли {self.product_name} ({self.shade})!")
        else:
            print(f"{self.product_name} просрочен — нельзя нанести.")


if __name__ == "__main__":
    # Создаём косметику
    serum = SkincareCosmetics("La Roche-Posay", "Hydraphase Intense", 30.0, "12.2025", "сухая", "гиалуроновая кислота")
    hand_cream = SkincareCosmetics("Nivea", "Крем для рук", 75.0, "09.2024", "нормальная", "пантенол")
    mascara = DecorativeCosmetics("Maybelline", "The Falsies", 10.0, "05.2024", "тушь для ресниц", "чёрный")
    lipstick = DecorativeCosmetics("Chanel", "Rouge Coco", 4.0, "11.2025", "помада", "розовый")

    # Проверяем сроки годности (текущая дата — 03.2024)
    current_date = "03.2024"
    print(f"Проверка сроков на {current_date}:")
    print(f"Сыворотка просрочена? {serum.check_expiration(current_date)}")
    print(f"Крем для рук просрочен? {hand_cream.check_expiration(current_date)}")
    print(f"Тушь просрочена? {mascara.check_expiration(current_date)}")
    print(f"Помада просрочена? {lipstick.check_expiration(current_date)}")

    # Используем уходовую косметику
    print("\nИспользуем косметику:")
    serum.use_product(2.0)
    hand_cream.use_product(5.0)

    # Корректируем pH сыворотки
    print(f"\nКорректируем pH сыворотки:")
    serum.adjust_ph(5.2)
    print(f"Новый pH: {serum.get_ph_level()}")

    # Наносим декоративную косметику
    print("\nНаносим декоративную косметику:")
    mascara.apply_product()
    lipstick.apply_product()

    # Делаем тушь водостойкой
    print("\nДелаем тушь водостойкой:")
    mascara.set_waterproof(True)
    print(mascara)





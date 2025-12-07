salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
sum_spend=0
for i in range(months):
    sum_spend=sum_spend+spend*(1+increase)**i
    i+=1
sum_salary=salary*months
money_capital=int(round(sum_spend-sum_salary, 0))
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)


from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, value


"""
Створити задачу, змінні з кордонами (>=0) та додати цільову функцію
"""
model = LpProblem("Drinks Production Optimization", LpMaximize)
lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
juice = LpVariable("Fruit Juice", lowBound=0, cat="Integer")
model += lemonade + juice, "Maximize production"


"""
Додати обмеження:
Вода 2L+1J <= 100
Цукор 1L <= 50
Лимонний сік 1L ≤ 30
Фруктове пюре: 2J ≤ 40
"""
model += 2 * lemonade + 1 * juice <= 100, "Water constraint"
model += 1 * lemonade <= 50, "Sugar constraint"
model += 1 * lemonade <= 30, "Lemon juice constraint"
model += 2 * juice <= 40, "Fruit puree constraint"


if __name__ == "__main__":
    """
    Розв'язати задачу та вивести результати
    """
    model.solve()
    print("Status:", LpStatus[model.status])

    for variable in model.variables():
        print(f"{variable.name} produced: {variable.varValue}")
    print(f"Total produced: {value(model.objective)} products")

    """
    Другий варіант виводу:
    print("Fruit Juice produced:", value(juice) або juice.varValue)
    print("Lemonade produced:", value(lemonade) або lemonade.varValue) 
    """

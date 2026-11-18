import random

n = int(input("Введите размер матрицы n: "))

# заполняем матрицу случайными числами от -5 до 10
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(-5, 10))
    matrix.append(row)

print("\nНаша матрица:")
for row in matrix:
    print(row)

# --- ПУНКТ 1: сумма в столбцах без отрицательных ---
print("\n--- Пункт 1 ---")
total_sum = 0

for j in range(n):  # перебираем столбцы
    has_negative = False
    for i in range(n):
        if matrix[i][j] < 0:
            has_negative = True
            break

    if not has_negative:
        col_sum = 0
        for i in range(n):
            col_sum += matrix[i][j]
        total_sum += col_sum
        print(f"Столбец {j} подходит, его сумма = {col_sum}")

print(f"Общая сумма: {total_sum}")

# --- ПУНКТ 2: минимум среди диагоналей, ПАРАЛЛЕЛЬНЫХ ПОБОЧНОЙ ---
print("\n--- Пункт 2 (диагонали, параллельные ПОБОЧНОЙ) ---")

# ВАЖНО: у побочной диагонали сумма индексов i + j = n - 1.
# У диагоналей, параллельных ей, сумма индексов i + j = k (постоянна на всей диагонали).
# k меняется от 0 (верхний правый угол) до 2n-2 (нижний левый угол).

min_sum = None

for k in range(2 * n - 1):
    diag_sum = 0
    # проходим по строкам
    for i in range(n):
        j = k - i  # так как i + j = k
        if 0 <= j < n:  # проверяем, что не вылезли за границы
            diag_sum += abs(matrix[i][j])

    print(f"Диагональ k={k}, сумма модулей = {diag_sum}")

    if min_sum is None or diag_sum < min_sum:
        min_sum = diag_sum

print(f"\nМинимум среди сумм: {min_sum}")
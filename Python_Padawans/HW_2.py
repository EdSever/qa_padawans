# 1. Создать переменную item_1 типа integer.
print("1. Создать переменную item_1 типа integer.")
item_1 = 10
print("Переменная item_1 типа integer =", item_1)
print()

# 2. Создать переменную item_2 типа integer.
print("2. Создать переменную item_2 типа integer.")
item_2 = 20
print("Переменная item_2 типа integer =", item_2)
print()

# 3. Создать переменную result_sum в которой вы суммируете item_1 и item_2.
print("3. Создать переменную result_sum в которой вы суммируете item_1 и item_2.")
result_sum = item_1 + item_2
print("result_sum = item_1 + item_2")
print()

# 4. Вывести result_sum в консоль.
print("4. Вывести result_sum в консоль.")
print("result_sum =", result_sum)
print()

# 5. Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.
print("5. Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.")
result_subtr_max = max(item_1, item_2)
result_subtr_min = min(item_1, item_2)
result_subtr = result_subtr_min - result_subtr_max
print("result_subtr_max = max(item_1, item_2) ")
print("result_subtr_min = min(item_1, item_2) ")
print("result_subtr = result_subtr_min - result_subtr_max")
print()

#  6. Вывести result_subtr в консоль.
print(" 6. Вывести result_subtr в консоль.")
print("result_subtr =", result_subtr)

# 7. Создать переменную result_multi в которой вы умножаете item_1 на item_2.
print("7. Создать переменную result_multi в которой вы умножаете item_1 на item_2.")
print("result_multi = item_1 * item_2")
print()

# 8. Вывести result_multi в консоль.
print("8. Вывести result_multi в консоль.")
result_multi = item_1 * item_2
print("result_multi =", result_multi)

# 9. Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
print("9. Создать переменную result_exp в которой вы item_1 возводите в степень item_2.")
print("result_exp =  item_1 ** item_2")
print()

# 10. Вывести result_exp в консоль.
print("10. Вывести result_exp в консоль.")
result_exp = item_1 ** item_2
print("result_exp =", result_exp)
print()

# 11. Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
print("11. Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.")
import math
print("pow(item_1, item_2)")
print()

# 12. Вывести result_m_exp в консоль.
print("12. Вывести result_m_exp в консоль.")
result_m_exp = pow(item_1, item_2)
print("result_m_exp =", result_m_exp)
print()

# 13. Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item
print("13. Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item")
print("result_s_root = item_1 ** 0.5")
print()

# 14. Вывести result_s_root в консоль.
print("14. Вывести result_s_root в консоль.")
result_s_root = item_1 ** 0.5
print("result_s_root =", result_s_root)
print()

# 15. Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item
#     используя библиотеку math.
print("15. Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item "
      "используя библиотеку math.")
print("math.sqrt(item_1)")
print()

# 16. Вывести result_m_s_root в консоль.
print(" 16. Вывести result_m_s_root в консоль.")
result_m_s_root = math.sqrt(item_1)
print("result_m_s_root =", result_m_s_root)
print()

# 17. Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item
#     используя библиотеку math используя метод pow.
print("17. Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item "
      "используя библиотеку math используя метод pow.")
result_mp_s_root = math.pow(item_1, 0.5)
print("math.pow(item_1, 0.5)")
print()

# 18. Вывести result_mp_s_root в консоль.
print("18. Вывести result_mp_s_root в консоль.")
print("result_mp_s_root =", result_mp_s_root)
print()

# 19. Присвоить переменной item_1 odd значение
print("19. Присвоить переменной item_1 odd значение")
item_1 = 9
print("item_1 =", item_1)
print()

# 20. Присвоить переменной item_2 even значение
print("20. Присвоить переменной item_2 even значение")
item_2 = 4
print("item_2 =", item_2)
print()

# 21. Создать переменную result_division в которой вы разделите item_1 на item_2.
print("21. Создать переменную result_division в которой вы разделите item_1 на item_2.")
result_division = item_1 / item_2
print("result_division = item_1 / item_2")
print()

# 22. Вывести result_division в консоль.
print("22. Вывести result_division в консоль.")
print("result_division =", result_division)
print()

# 23. Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
print("23. Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.")
result_m_floor = math.floor(result_division)
print("result_m_floor = math.floor(result_division)")
print()

# 24. Вывести result_m_floor в консоль.
print("24. Вывести result_m_floor в консоль.")
print("result_m_floor =", result_m_floor)
print()

# 25. Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
print("25. Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.")
result_m_ceil = math.ceil(result_division)
print("result_m_ceil = math.ceil(result_division)")
print()

# 26. Вывести result_m_ceil в консоль.
print("26. Вывести result_m_ceil в консоль.")
print("result_m_ceil =", result_m_ceil)
print()

# 27. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
print("27. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.")
print("result_int = int(result_division)")
result_int = int(result_division)
print()

#  28. Вывести result_int в консоль.
print(" 28. Вывести result_int в консоль.")
print("result_int =", result_int)
print()

# 29. Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
print("29. Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.")
result_no_division_loss = item_1 // item_2
print("result_no_division_loss = item_1 // item_2")
print()

# 30. Вывести result_no_division_loss в консоль.
print("30. Вывести result_no_division_loss в консоль.")
print("result_no_division_loss =", result_no_division_loss)
print()

# 31. Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
print("31. Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.")
result_division_loss = item_1 % item_2
print("result_division_loss = item_1 % item_2")
print()

# 32. Вывести result_division_loss в консоль.
print("32. Вывести result_division_loss в консоль.")
print("result_division_loss =", result_division_loss)
print()

# 33. Создать переменную item_3 и присвоить ей целое число
print("33. Создать переменную item_3 и присвоить ей целое число")
item_3 = 15
print("item_3 =", item_3)
print()

# 34. Прибавить 10 к item_3 с присвоением.
print("34. Прибавить 10 к item_3 с присвоением.")
item_3 += 10
print("item_3 += 10")
print()

# 35. Вывести item_3 в консоль.
print("35. Вывести item_3 в консоль.")
print("item_3 =", item_3)
print()

# 36. Отнять 5 от item_3 с присвоением.
print("36. Отнять 5 от item_3 с присвоением.")
item_3 -= 5
print("item_3 -= 5")
print()

# 37. Вывести item_3 в консоль.
print("37. Вывести item_3 в консоль.")
print("item_3 =", item_3)
print()

# 38. Умножить item_3 на 3 с присвоением.
print("38. Умножить item_3 на 3 с присвоением.")
item_3 *= 3
print("item_3 *= 3")
print()

# 39. Вывести item_3 в консоль.
print("39. Вывести item_3 в консоль.")
print("item_3 =", item_3)
print()

# 40. Разделить item_3 на 2 с присвоением.
print("40. Разделить item_3 на 2 с присвоением.")
item_3 /= 2
print("item_3 /= 2")
print()

# 41. Вывести item_3 в консоль.
print("41. Вывести item_3 в консоль.")
# item_3 = int(item_3)
print("item_3 =", item_3)
print()

# 42. Возвести в степень 2 item_3 с присвоением.
print("42. Возвести в степень 2 item_3 с присвоением.")
item_3 **= 2
print("item_3 **= 2")
print()

# 43. Вывести item_3 в консоль.
print("43. Вывести item_3 в консоль.")
print("item_3 =", item_3)
print()

# 44. Найти квадратный корень item_3 с присвоением.
print("44. Найти квадратный корень item_3 с присвоением.")
item_3 **= 0.5
print("item_3 **= 0.5")
print()

# 45. Вывести item_3 в консоль.
print("45. Вывести item_3 в консоль.")
print("item_3 =", item_3)
print()

# 46. Присвоить остаток от деления item_3
print("46. Присвоить остаток от деления item_3")
print()

# 47. Вывести item_3 в консоль.
print("47. Вывести item_3 в консоль.")
print()

# 48. Создать переменную b_item_t и присвоить True
print("48. Создать переменную b_item_t и присвоить True")
b_item_t = True
print("b_item_t = True")
print()

# 49. Создать переменную b_item_f и присвоить False
print("49. Создать переменную b_item_f и присвоить False")
b_item_f = False
print("b_item_f = False")
print()

# 50. Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f
print("50. Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f")
b_item_relult_sum = b_item_t + b_item_f
print("b_item_relult_sum = b_item_t + b_item_f")
print()

# 51. Вывести b_item_relult_sum в консоль.
print("51. Вывести b_item_relult_sum в консоль.")
print("b_item_relult_sum =", b_item_relult_sum)
print()

# 52. Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f
print("52. Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f")
b_item_relult_subtr = b_item_t - b_item_f
print("b_item_relult_subtr = b_item_t - b_item_f")
print()

# 53. Вывести b_item_relult_subtr в консоль.
print("53. Вывести b_item_relult_subtr в консоль.")
print("b_item_relult_subtr =", b_item_relult_subtr)
print()

# 54. Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f
print("54. Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f")
b_item_relult_multi = b_item_t * b_item_f
print("b_item_relult_multi = b_item_t * b_item_f")
print()

# 55. Вывести b_item_relult_multi в консоль.
print("55. Вывести b_item_relult_multi в консоль.")
print("b_item_relult_multi =", b_item_relult_multi)
print()

# 56. Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f
print("56. Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f")
# b_item_relult_division = b_item_t / b_item_f
print("b_item_relult_division = b_item_t / b_item_f")
print()

# 57. Вывести b_item_relult_division в консоль. (Получить ошибку)
print("57. Вывести b_item_relult_division в консоль. (Получить ошибку)")
# print("b_item_relult_division =", b_item_relult_division)
print()

# 58. Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int
print("58. Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int ")
b_item_1_int = int(b_item_t)
print("b_item_1_int = int(b_item_t)")
print()

# 59. Вывести b_item_1_int в консоль.
print("59. Вывести b_item_t_int в консоль.")
print("b_item_1_int =", b_item_1_int)
print()

# 60. Создать переменную b_item_2_int и присвоить явное приведение b_item_f к int
print("60. Создать переменную b_item_2_int и присвоить явное приведение b_item_f к int ")
b_item_2_int = int(b_item_f)
print("b_item_2_int = int(b_item_f)")
print()

# 61. Вывести b_item_2_int в консоль.
print("61. Вывести b_item_2_int в консоль.")
print("b_item_2_int =", b_item_2_int)
print()

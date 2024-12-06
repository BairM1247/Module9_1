def apply_all_func(int_list, *functions):

    results = {}
    for func in functions:
        try:
            result = func(int_list)
            results[func.__name__] = result
        except Exception as e:
            results[func.__name__] = f"Ошибка: {e}"
    return results

result1 = apply_all_func([6, 20, 15, 9], max, min)
print(result1)


result2 = apply_all_func([6, 20, 15, 9], len, sum, sorted)
print(result2)


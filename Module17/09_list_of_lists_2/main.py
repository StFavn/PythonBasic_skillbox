nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
print('Ответ:', [nice_list[i // 9][i // 3 % 3][i % 3] for i in range(18)])  # Это медленее, но понятнее ведь
print('Ответ:', [num for sec_dimension in nice_list for fst_dimension in sec_dimension for num in fst_dimension])

import os

path = os.path.abspath(os.path.join('..', '..', 'Module14'))
# path = input('')

num_files, num_dirs, dir_weight = 0, 0, 0
for address, dirs, files in os.walk(path):
    num_dirs += len(dirs)
    num_files += len(files)
    for a_file in files:
        dir_weight += os.path.getsize(os.path.join(address, a_file))

print(path)
print('Размер каталога (в Кб):', dir_weight / 1024)
print('Количество подкаталогов:', num_dirs)
print('Количество файлов:', num_files)

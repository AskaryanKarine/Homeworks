### Список функций:
```
get_update_list
Функция для создания списка библиотек, которые необходимо обновить.
    Функция возвращает строку, содержащую список обновленных функций 
    в формате old_lib_name==new_version
    Строка записывается в файл reqs.txt    
```
```
updating    
Функция для установки обновлений библиотеки.
    Функция устанавливает библиотеки из файла reqs.txt и удаляет этот файл.
```
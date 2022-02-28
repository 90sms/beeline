Нужно дополнительно установить фреймворк Flask

На вход приходит файл содержит 100000 строк, 6 столбцов данных в виде текста и целых чисел. В некоторых записях могут содержаться ошибки по ожидаемому типу данных.

Столбец 1 – IP-адрес в формате: 0.0.0.0.
Столбец 2 – маска подсети в формате: 0.0.0.0.
Столбец 3 – подсеть в формате: 0.0.0.0.
Столбец 4 – номер компьютера в виде целого неотрицательного числа.
Столбец 5 – Ф.И.О. пользователя.
Столбец 6 – ошибка.
 
Клиентское приложение имеет графический / web интерфейс. Единственный объект интерфейса – кнопка «Начать».
 

При нажатии кнопки «Начать» сервер применяет к тестовому файлу следующие операции:
1.           Если IP-адрес имеет формат, отличный от стандартного, в столбец ошибки вносится отметка «IP err».
2.           Если маска подсети имеет формат, отличный от стандартного, в столбец ошибки вносится отметка «Mask err».
3.           Если адрес подсети имеет формат, отличный от стандартного, в столбец ошибки вносится отметка «Subnet err».
4.           Если подсеть указана неверно, в столбец ошибки вносится отметка «Subnet incorrect».
5.           Если подсеть не указана, то она вычисляется и вносится в соответствующий столбец.
6.           Если номер компьютера имеет формат, отличный от стандартного, в столбец ошибки вносится отметка «Num err».
7.           Если номер компьютера отсутствует, то он должен быть присвоен в порядке возрастания.
8.           Если номер компьютера повторяется, то он должен быть заменён на очередной в порядке возрастания.


Данный скрипт обрабатывает логи типа access.log. Результат выполнение записывается в базу данных postgres.
Содержимое базы данных при каждом запуске скрипта переписывается. 

# Зависимости 

```
pandas==1.1.3
tqdm==4.51.0
```

# Запуск

```
chmod +x script.py
./script.py -i/--inpath [Путь к файлу] -H/--host [ip  (default='127.0.0.1')] -p/--port [port (default=5432)] -d/--dbname [dbname default='logs] -u/--username [username default='postgres] -P/--password [password]
```
или:

```
python script.py -i/--inpath [Путь к файлу] -H/--host [ip  (default='127.0.0.1')] -p/--port [port (default=5432)] -d/--dbname [dbname default='logs] -u/--username [username default='postgres] -P/--password [password]
```


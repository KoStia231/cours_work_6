# Сервис Email рассылки 

### Для настроек проекта нужно использовать переменные окружения

###### пример файла .env

```
.env.example
```

### Установить все зависимости

```python
pip install - r requirements.txt
```

### Применить все миграции

```python
python3 manage.py migrate 
```

### Создать админа

```python
python3 manage.py admin_reg
```

###### Файл для создания админа находится по пути

###### users/management/commands/admin_reg.py


### Запуск сервера

```python
python3 manage.py runserver 
```

## Пользователи в базе

> username-> ***admin@example.com***
>
>password-> ***admin***

> username-> ***kosta123139@gmail.com***
>
>password-> ***Hh14767Hh***

> username-> ***kos@gmail.com***
>
>password-> ***Hh14767HH***
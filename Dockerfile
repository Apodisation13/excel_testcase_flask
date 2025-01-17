# Использовать официальный образ родительского образа / слепка.
FROM python:3.9

# Установка рабочей директории, откуда выполняются команды внутриконтейнера.
WORKDIR /excel_testcase_flask

# Скопировать все файлы с локальной машины внутрь файловой системывиртуального образа.
COPY . .

# Запустить команду внутри образа, установка зависимостей.
RUN pip install --upgrade pip && pip install -r requirements.txt
#RUN chmod +x entrypoint.sh
RUN chmod +x /excel_testcase_flask/entrypoint.sh

# Добавить мета-информацию к образу для открытия порта к прослушиванию.
EXPOSE 5000

# Выполнить команду внутри контейнера
#CMD ["python", "./manage.py",  "runserver", "0.0.0.0:8000"]

ENTRYPOINT ["/excel_testcase_flask/entrypoint.sh"]

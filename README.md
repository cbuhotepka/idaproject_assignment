# Pictures exchange application
test assignment

## Описание

Веб-приложение для загрузки изображений, позволяющее загружать файлы с компьютера или по ссылке. Возможно создавать, удалять изображения.
Изменение размера изображения с сохранением пропорций возможно по одному из предоставленных измерений. Если предоставлены 2 с несоответствующими пропорциями берётся большее.

## Разворачивание

Только локально.

    python -m venv venv
    
    .\venv\Scripts\activate.ps1
    
    cd .\idaproject_assignment
    
    pip install -r requirements.txt
    
    python manage.py runserver
    
    start http://127.0.0.1:8000/

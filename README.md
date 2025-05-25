# ai_resume_builder

![Интерфейс генератора резюме](screenshot.png.png)

Веб-приложение для генерации резюме на FastAPI с минималистичным интерфейсом в стиле iOS.

## Назначение

Демонстрация fullstack-навыков: FastAPI, Jinja2, Tailwind CSS, Docker. Пользователь заполняет форму, а приложение красиво отображает готовое резюме.

## Стек
- Python
- FastAPI
- Jinja2
- Tailwind CSS (CDN)
- Docker

## Как запустить

### Через Docker
```bash
git clone https://github.com/DjoLenMark/ai_resume_builder.git
cd ai_resume_builder
docker build -t ai_resume_builder .
docker run -p 8000:8000 ai_resume_builder
```

### Обычный способ
```bash
git clone https://github.com/DjoLenMark/ai_resume_builder.git
cd ai_resume_builder
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate для Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Пример заполнения формы
- Имя: Иван Иванов
- Профессия: Python-разработчик
- Образование: МГУ, Прикладная математика
- Опыт работы: 2 года в Яндекс, 1 год в стартапе
- Навыки: FastAPI, Docker, SQL, Git
- Контакты: ivan@example.com, Telegram: @ivan

## Структура
```
ai_resume_builder/
├── app/
│   ├── main.py
│   ├── templates/
│   │   ├── index.html
│   │   └── resume.html
│   └── static/
│       └── style.css (если нужно)
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

## Особенности
- Нет авторизации, баз данных, внешних API
- Только FastAPI, шаблоны и UI
- Минимализм, мягкие тени, шрифт San Francisco 
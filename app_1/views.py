# from django.shortcuts import render
import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)     

def index(request):
    maingpage = """
        <header>
            <a href="">Главная страница</a>
            <a href="">Обо мне</a>
        </header>
        <div>
            <h1>Главная страница</h1>
            <h2>Это главная страница</h2>
        </div>
        <footer>
            <div>
                <p> Контакты: <a href="email@mail.ru">email@mail.ru</a> Тестовая ссылка</p>
            </div>
        </footer>
        """
    logger.info(f'Страница "Главная" успешно открыта')
    return HttpResponse(maingpage)


def about(request):
    about_page="""
        <header>
            <a href="">Главная страница</a>
            <a href="">Обо мне</a>
        </header>
        <div>
        <h1>Добро пожаловать на страницу с информацией обо мне</h1>
        <p>Меня зовут Виктория</p>
        <p>Я учусть в GB</p>
        </div>
        """
    logger.info(f'Страница "Обо мне" успешно открыта')
    return HttpResponse(about_page)


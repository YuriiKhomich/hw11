# presenter.py
"""
Вариант с простым фабричным методом:
+ позволяет добавлять новые типы статей без изменения
существующего кода в presenter.py. Если в будущем появятся новые типы статей,
достаточно будет добавить новую реализацию в ArticleFactory.
Это обеспечивает лучшую гибкость и расширяемость кода
+ зависит только от абстрактного класса Article и фабрики ArticleFactory,
что позволяет изолировать презентер от конкретных реализаций статей
-  если приложение достаточно простое, то использование
фабричного метода может быть излишним, и более прямолинейный подход может
быть предпочтительным, как напрмер, в нашем случае, или согласно ТЗ и требований заказчика.
- IMHO Прямолинейный подход все таки легче для прочтения и понимания в маленьких проектах.
"""
from model import PapperArticle, SiteArticle, BlogArticle, NewsArticle
from view import get_user_choice, display_message

class ArticleFactory:
    @staticmethod
    def create_article(choice):
        if choice == "1":
            return PapperArticle()
        elif choice == "2":
            return SiteArticle()
        elif choice == "3":
            return BlogArticle()
        elif choice == "4":
            return NewsArticle()
        else:
            return None

def add_article(articles, article):
    if article:
        articles.append(article)
        display_message("Статья успешно добавлена!")
    else:
        display_message("Некорректный выбор. Статья не добавлена.")

def run():
    articles = []
    choice = get_user_choice()
    article = ArticleFactory.create_article(choice)
    add_article(articles, article)

if __name__ == "__main__":
    run()


"""
Вариант прямолинейный

from model import PapperArticle, SiteArticle, BlogArticle, NewsArticle
from view import get_user_choice, display_message

def create_article():
    choice = get_user_choice()

    if choice == "1":
        article = PapperArticle()
    elif choice == "2":
        article = SiteArticle()
    elif choice == "3":
        article = BlogArticle()
    elif choice == "4":
        article = NewsArticle()
    else:
        article = None

    return article

def add_article(articles, article):
    if article:
        articles.append(article)
        display_message("Статья успешно добавлена!")
    else:
        display_message("Некорректный выбор. Статья не добавлена.")

def run():
    articles = []
    article = create_article()
    add_article(articles, article)

if __name__ == "__main__":
    run()


"""
# model.py

class Article:
    def __init__(self):
        self.title = ""
        self.description = ""
        self.text = ""

class PapperArticle(Article):
    def __init__(self):
        super().__init__()
        self.papper = ""

class SiteArticle(Article):
    def __init__(self):
        super().__init__()
        self.site = ""

class BlogArticle(Article):
    def __init__(self):
        super().__init__()
        self.blog = ""

class NewsArticle(Article):
    def __init__(self):
        super().__init__()
        self.news = ""

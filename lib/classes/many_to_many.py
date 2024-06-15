class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
            self._articles = []
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return self._articles
    
    def magazines(self):
        return list(set(article.magazine for article in self._articles))
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
            self._articles = []
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string")
    
    def articles(self):
        return self._articles
    
    def contributors(self):
        return list(set(article.author for article in self._articles))
    
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
    
    def contributing_authors(self):
        author_count = {}
        for article in self._articles:
            if article.author in author_count:
                author_count[article.author] += 1
            else:
                author_count[article.author] = 1
        
        contributing_authors = [author for author, count in author_count.items() if count > 2]
        return contributing_authors if contributing_authors else None


class Article:
    def __init__(self, author, magazine, title):
        if isinstance(author, Author):
            self._author = author
            author._articles.append(self)
        else:
            raise ValueError("Author must be an instance of Author class")
        
        if isinstance(magazine, Magazine):
            self._magazine = magazine
            magazine._articles.append(self)
        else:
            raise ValueError("Magazine must be an instance of Magazine class")

        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters")
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def magazine(self):
        return self._magazine

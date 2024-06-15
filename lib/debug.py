#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if _name_ == '_main_':
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    magazine1 = Magazine("Tech Monthly", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")
    article1 = author1.add_article(magazine1, "Tech Trends 2024")
    article2 = author1.add_article(magazine2, "Healthy Living Tips")
    article3 = author2.add_article(magazine1, "AI in 2024")
    article4 = author1.add_article(magazine1, "The Future of AI")

    print(author1.articles())
    print(author1.magazines())
    print(author1.topic_areas())

    print(magazine1.articles())
    print(magazine1.contributors())
    print(magazine1.article_titles())
    print(magazine1.contributing_authors())

    print(article1.author.name)
    print(article1.magazine.name)

     # Don't remove this line, it's for debugging!
    ipdb.set_trace()
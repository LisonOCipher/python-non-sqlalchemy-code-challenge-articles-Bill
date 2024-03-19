from author import Author
from magazine import Magazine

# author creation
author1 = Author("John Doe")
author2 = Author("Jane Smith")

# magazine creation
magazine1 = Magazine("Tech Weekly", "Technology")
magazine2 = Magazine("Fashion Monthly", "Fashion")

# articles
article1 = author1.add_article(magazine1, "Python Programming Tips")
article2 = author1.add_article(magazine2, "Summer Fashion Trends")
article3 = author2.add_article(magazine1, "Machine Learning Applications")

# test 
print("Author:", author1.name)
print("Articles by Author:", [article.title for article in author1.articles()])
print("Magazines contributed to:", [mag.name for mag in author1.magazines()])
print("Topic areas:", author1.topic_areas())

print("Magazine:", magazine1.name)
print("Articles in Magazine:", [article.title for article in magazine1.articles()])
print("Contributors to Magazine:", [author.name for author in magazine1.contributors()])
print("Top Publisher:", Magazine.top_publisher().name)

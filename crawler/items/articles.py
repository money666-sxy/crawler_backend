from crawler.items.notebooks import Notebook
from crawler.items.authors import Author

class Article(object):
    def __init__(self, article_id=None, title=None, content=None, public_comments_count=None, slug=None, likes_count=None,
                 views_count=None, total_rewards_count=None, first_shared_at=None, like_rate=None):

        self.article_id = article_id
        self.title = title
        self.content = content
        self.public_comments_count = public_comments_count
        self.likes_count = likes_count
        self.slug = slug
        self.views_count = views_count
        self.total_rewards_count = total_rewards_count
        self.first_shared_at = first_shared_at
        self.like_rate = 0
        self.author = Author()
        self.notebook = Notebook()
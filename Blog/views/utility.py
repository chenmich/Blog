from ..models.views.blog_view import BlogView

def get_post_views():
    titles = ['混凝土中的气泡与引所剂之我见'
                ,'减水剂在混凝土中的作用'
                ,'搅拌站管理的要点'
                ,'混凝土配合比设计浅见']
    views = []
    for n in range(0, 4):
        view = BlogView(titles[n])
        views.append(view)
    return views
from .models import Post
from django.conf import settings

class Visited(object):

    def __init__(self,request):
        self.session=request.session
        visited=self.session.get(settings.SESSION_ID)
        if not visited:
            visited = self.session[settings.SESSION_ID] = {'slugs': []}
        self.visited=visited

    def add(self,post):
        post_title=str(post.title)
        if post_title not in self.visited['slugs']:
            post.visitors_counter += 1
            post.save()
            self.visited['slugs'].append(str(post_title))
            self.session[settings.SESSION_ID]=self.visited

    




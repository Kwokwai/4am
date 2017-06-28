from haystack.views import SearchView
from forum.models import Topic


class MySeachView(SearchView):
    template_name = "index.html"
    context_object_name = "topic_list"

    def extra_context(self):
        context = super(MySeachView, self).extra_context()
        context['topic_list'] = Topic.objects.all()
        return context
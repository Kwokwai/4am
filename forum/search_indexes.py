from haystack import indexes
from forum.models import Topic


class TopicIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Topic

    def index_queryset(self, using=None):
        return self.get_model().objects.all()



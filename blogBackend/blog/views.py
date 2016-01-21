""" Used this tutorial:
http://www.django-rest-framework.org/tutorial/quickstart/#views"""


from .models import Entry
from rest_framework import viewsets
from .serializers import BlogSerializer


class EntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Entry.objects.all().order_by('datePub')
    serializer_class = BlogSerializer

from time import time

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils.text import slugify


def get_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)

        return render(request, self.template,
                      context={self.model.__name__.lower(): obj,
                               'admin_object': obj,
                               'detail': True})

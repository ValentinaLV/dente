from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import View

from .models import News, Comment
from .utils import ObjectDetailMixin
from .forms import NewsCommentForm


def news_pagination(request):
    posts = News.objects.all()
    paginator = Paginator(posts, settings.POSTS_PER_PAGE)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    return {
        'page_obj': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }


def news_list(request):
    return render(request, 'news.html',
                  context=news_pagination(request))


@login_required()
def like_news(request, slug):
    post = News.objects.get(slug=slug)
    post.like_voters.add(request.user)
    post.unlike_voters.remove(request.user)
    post.save()
    return redirect('news:news-details', slug=slug)


@login_required()
def unlike_news(request, slug):
    post = News.objects.get(slug=slug)
    post.unlike_voters.add(request.user)
    post.like_voters.remove(request.user)
    post.save()
    return redirect('news:news-details', slug=slug)


@login_required()
def leave_comment(request, slug):
    post = News.objects.get(slug=slug)
    comments = Comment.objects.filter(news=post)

    if request.method == 'POST':
        comment_form = NewsCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.news = post
            new_comment.save()
            return redirect('news:leave-comment-news', slug=slug)
    else:
        comment_form = NewsCommentForm()

    return render(request, 'news_comments.html', {
        'news': post,
        'comments': comments,
        'form': comment_form
    })


class NewsDetail(ObjectDetailMixin, View):
    model = News
    template = 'news_details.html'

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from dente.settings import COMMENTS_PER_PAGE
from .models import PatientFeedback
from .forms import PatientFeedbackForm


def pagination_feedback(request):
    feedbacks = PatientFeedback.objects.all()
    feedback_form = PatientFeedbackForm()

    paginator = Paginator(feedbacks, COMMENTS_PER_PAGE)

    page_num = request.GET.get('page', 1)
    page = paginator.get_page(page_num)

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
        'prev_url': prev_url,
        'form': feedback_form
    }


@login_required()
def patient_feedback(request):
    if request.method == 'POST':
        feedback_form = PatientFeedbackForm(request.POST)
        if feedback_form.is_valid():
            new_feedback = feedback_form.save(commit=False)
            new_feedback.user = request.user
            new_feedback.save()
            return redirect('feedback:patient_feedback_url')

    return render(request, 'patient_feedback.html',
                  context=pagination_feedback(request))

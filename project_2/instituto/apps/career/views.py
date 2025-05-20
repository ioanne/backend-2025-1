from django.shortcuts import render

from apps.career.models import Career


def career_list(request):
    """
    View to list all careers.
    """
    careers = Career.objects.all()

    return render(request, 'career_list.html', {'careers': careers})
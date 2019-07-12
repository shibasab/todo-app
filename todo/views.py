from django.shortcuts import render

def post_list(request):
    return render(request, 'todo/post_list.html', {})
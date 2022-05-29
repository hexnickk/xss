from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        search = request.GET.get('search', None)
        return render(request, 'reflected0/index.html', {'search': search})

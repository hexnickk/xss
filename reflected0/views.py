from django.shortcuts import render
from django.views import View
from json import dumps


class ReflectedHTMLView(View):
    def get(self, request):
        search = request.GET.get('search', None)
        return render(request, 'reflected0/simple.html', {'search': search})


class ReflectedJSONView(View):
    def get(self, request):
        search = request.GET.get('search', None)
        json = dumps({
            'query': {
                **request.GET
            }
        })
        return render(request, 'reflected0/json.html', {'search': search, 'json': json})


class ReflectedURLView(View):
    def get(self, request):
        profile = request.GET.get('profile', '')
        return render(request, 'reflected0/url.html', {'profile': profile})


class ReflectedURLSchemeView(View):
    def get(self, request):
        return render(request, 'reflected0/url-scheme.html')

    def post(self, request):
        profile = request.POST.get('profile', '')
        return render(request, 'reflected0/url-scheme.html', {'profile': profile})

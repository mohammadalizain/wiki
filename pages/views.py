from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def function_name(request):
    return HttpResponse("<h1> Hello</h1>")

 def details_view(request)
 	context = {
        "object": {
            "key1":"value1",
            "key2":"value2",
            "key3":"value3",
            
        },
    }
    return render(request, 'list.html', context)


    def list_view(request):
    context = {
        "article": {
            "title":"Do or do not",
            "content":"There is no try.",
            "last_updated_on":"2018-7-31",
        },
    }
    return render(request, 'list.html', context)
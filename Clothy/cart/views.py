from django.shortcuts import render

# Create your views here.

def cart_summary(request):
    context = {'hello':'bla bla',
                'bla':'hell world'}
    return render(request, 'cart_summary.html', context)


def cart_add(request):
    pass


def cart_delete(request):
    pass


def cart_update(request):
    pass
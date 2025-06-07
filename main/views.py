from django.shortcuts import render,redirect
from .models import Article,Review
from .forms import CustomerRegistrationForm,ArticleForm,ReviewForm
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView


# Create your views here.
def main(request):
    articles=Article.objects.all()
    top_article=Article.objects.order_by('?').first() 
    return render(request,'main/main.html',{'articles':articles,'top_article':top_article})

def about(request):
    return render(request,'main/about.html')

def register(request):
    form = CustomerRegistrationForm()
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('main')
        else:
            messages.error(request, 'Please correct the errors below.')

    return render(request, 'main/register.html', {
        'form': form,
        'now': datetime.now()
    })


def login(request):
    return render(request,'main/login.html')

@login_required(login_url='login')
def dashboard(request):
    form=ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Article added successfully!')
            return redirect('dashboard')

    return render(request, 'main/dashboard.html', {
        'form': form,
        'now': datetime.now()
    })

@login_required(login_url='login')
def review(request):
    all_reviews=Review.objects.all()
    form=ReviewForm()
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, "Thanks for your feedback!")
            return redirect('reviews')
    else:
        messages.error(request, "You must be logged in to leave a review.")
    return render(request,'main/review.html',{'form': form,'all_reviews':all_reviews})

class ArticleDetailView(DetailView):
    model=Article
    template_name='main/article_detail.html'
    context_object_name='article'

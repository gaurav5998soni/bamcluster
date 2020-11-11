from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Article, ContactUs, OurTeam
from .forms import ArticleForm, ProductForm, ContactUsForm, OurTeamForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.

def home(request):
	mydict = {
		"Articles": Article.objects.all().order_by('-created')[:3],
		"Products": Product.objects.all()[:4]
	}
	return render(request, 'cluster/index.html',mydict)



class Products(ListView):
	template_name = 'cluster/products.html'
	model = Product
	context_object_name = 'products'
	paginate_by = 12


def product_detail(request, pk):
	context = {}
	context["product"] = Product.objects.get(id=pk)
	return render(request, 'cluster/product.html', context)

class ProductUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
	model = Product
	fields = ['product_title','product_description', 'product_img']
	#
	# def form_valid(self, form):
	# 	form.instance.author = self.request.user
	# 	return super().form_valid(form)
	#
	def test_func(self):
		post = self.get_object()
		# if self.request.user == post.author:
		if self.request.user.is_authenticated:
			return True
		return False


def delete_product(request):
	product_id = request.GET.get('product_id')
	product = get_object_or_404(Product, id=product_id)
	
	product.delete()
	return JsonResponse('deleted', safe=False)


def delete_article(request):
	article_id = request.GET.get('article_id')
	article = get_object_or_404(Article, id=article_id)
	
	article.delete()
	return JsonResponse('deleted', safe=False)


# class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
# 	model = Product
# 	success_url = '/'

# 	def test_func(self):
# 		post = self.get_object()
# 		if self.request.user.is_authenticated:
# 			return True
# 		return False


class article(ListView):
	template_name = 'cluster/articles.html'
	model = Article
	context_object_name = 'articles'
	ordering = ['-created']
	paginate_by = 5



def article_detail(request, pk):
	context = {}
	context["article"] = get_object_or_404(Article, id=pk)
	return render(request, 'cluster/article.html', context)

class ArticleUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
	model = Article
	fields = ['title','description']

	def test_func(self):
		post = self.get_object()
		# if self.request.user == post.author:
		if self.request.user.is_authenticated:
			return True
		return False




class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Article
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user.is_authenticated:
			return True
		return False


def login_view(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request,
							username=username,
							password=password)
		if user is not None:
			
			login(request,user)
			messages.success(request, 'Login successfully!')

			return redirect('updates')
		else:
			messages.error(request, 'Username/Password is not valid!')

	return render(request, 'cluster/admin/login.html')


def updates(request):
	
	article_form = ArticleForm()
	product_form = ProductForm()
	if request.method == "POST":
		
		article_form = ArticleForm(request.POST)
		product_form = ProductForm(request.POST, request.FILES)
		if article_form.is_valid():
			title = article_form.cleaned_data.get('a_title')
			messages.success(request, 'Article {title} is created successfully!')
			article_form.save()
			
		if product_form.is_valid():

			product_form.save()
			print('hello')
			title = article_form.cleaned_data.get('title')
			messages.success(request, 'Article {title} is created successfully!')
			
		else:
			messages.error(request, 'Username/Password is not valid!')


	return render(request, 'cluster/admin/updates.html')


def add_member(request):
	if request.method == "POST":
		form = OurTeamForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			messages.success(request, 'Hey {name}, is created successfully!')
			form.save()
			return redirect('our_team')
		else:
			messages.error(request, 'Fill all fields accurately!')

	return render(request, 'cluster/admin/add_member.html')


def our_team(request):
	form = OurTeamForm()
	members = OurTeam.objects.all().order_by('-date')
	page    = request.GET.get('page', 1)
	paginator= Paginator(members, 10)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)
	
	query = request.GET.get('search')
	
	if query:
		members = OurTeam.objects.filter(Q(name__icontains=query)|
			Q(designation__icontains=query))
		
	context = {
		#'members': members,
		'page_obj': members,
	}
	
	return render(request, 'cluster/admin/our_team.html', context)


class OurTeamUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
	model = OurTeam
	fields = '__all__'

	def test_func(self):
		post = self.get_object()
		# if self.request.user == post.author:
		if self.request.user.is_authenticated:
			return True
		return False


class OurTeamDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = OurTeam
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user.is_authenticated:
			return True
		return False


def contact_us(request):
	form = ContactUsForm()
	if request.method == "POST":
		form = ContactUsForm(request.POST)
		print(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			messages.success(request, '{name}, is created!')
			form.save()
			return redirect('home')
		else:
			messages.error(request, 'Fill all fields accurately!')
	return render(request, 'cluster/contact_us.html', )


def contact_us_responses(request):
	responses = ContactUs.objects.all()
	return render(request, 'cluster/admin/contact_us_responses.html',{'responses':responses})


def support_us(request):
	return render(request, 'cluster/help_us.html')


def logout_view(request):
	logout(request)
	return redirect('/cluster/')
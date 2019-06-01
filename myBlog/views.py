from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import commentForm

# Create your views here.
def homepage(request):

	#return HttpResponse("<h1>Hello World</h1>")
	posts = Post.objects.all()
	header = "welcome"

	return render(request,'index.html', {'titles':posts, 'header':header}) 
	

def singlepost(request, post_id):

	post = Post.objects.get(id=post_id)
	form = commentForm()
	comments = post.comments.all()

	if request.method == 'POST':
		form = commentForm(request.POST)

		if form.is_valid:
			comment = form.save(commit=False)
			comment.post = post
			comment.author = request.user
			comment.save()

	return render(request, 'singlepost.html', {'post':post, 'comments=':comments, 'form':form})


	
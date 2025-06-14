from django.shortcuts import render,redirect
from .models import Post

# Create your views here.
# def index_inner(request):
#     return render(request, 'crud/index_inner.html')

# def index_outer(request):
#     return render(request, 'index_outer.html')

def show(request):
    posts = Post.objects.all()
    # for post in posts:
    #     print(post)
    # # print(posts)

    context = {
        'posts':posts
    }
    return render(request, 'crud/show.html', context)

def insert(request):
    if request.method == 'POST':
        post_image_ = request.FILES['post_image']
        title_ = request.POST['title']
        content_ = request.POST['content']

        # QuerySet
        add_post = Post.objects.create(
            image=post_image_,
            title = title_,
            content = content_
        )
        add_post.save()
        return redirect('show')
    return render(request, 'crud/insert.html')

def update_post(request, post_id):
    update_post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        if request.FILES:
            update_post.image = request.FILES['post_image']

        update_post.title = request.POST['title']
        update_post.content = request.POST['content']
        update_post.save()
        return redirect('show')
        
    context = {
        'post': update_post
    }
    return render(request, 'crud/update.html', context)

def delete_post(request, post_id):
    delete_post = Post.objects.get(id=post_id)
    delete_post.delete()
    return redirect('show')

"""
https://witzcode.pythonanywhere.com/technology/2/15/?wz_tech=C%20programming&wz_category=variable

http - request, response
ssl -

witzcode.pythonanywhere.com IP:PORT

/technology/2/15/ - endpoint

?
wz_tech=C%20programming
&
wz_category=variable
&
page=2
&
limit=5
"""
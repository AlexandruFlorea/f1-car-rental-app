from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.shortcuts import get_object_or_404, render
from blogs.models import Post, Comment
from blogs.forms import PostForm, CommentForm


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'blogs/post_list.html'


class PostDetails(DetailView):
    model = Post
    template_name = 'blogs/post_detail.html'


class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'blogs/post_create_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', ]
    template_name = 'blogs/post_update.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blogs/post_confirm_delete.html'
    success_url = reverse_lazy('blogs:all')  # We have to use reverse_lazy() instead of reverse(), as the urls are not loaded when the file is imported.


def post_detail(request, slug):
    template_name = 'blogs/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create object but don't save it to the db yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
         comment_form = CommentForm()

    return render(request, template_name, {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    })

from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import *
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.db.models import Q
from hitcount.views import HitCountDetailView

# Create your views here.

def LikeView(request, pk):
    post = get_object_or_404(Anon, id=request.POST.get('post_id'))
    post.likes.add(request.user)

    return HttpResponseRedirect(reverse('anons_detail', args=[str(pk)]))

class AnonsListView(ListView):
    model = Anon
    template_name = 'anons/anons_list.html'

class AnonsDetailView(HitCountDetailView):
    model = Anon
    template_name = 'anons/anons_detail.html'
    count_hit = True

    def showvideo(request):

        lastvideo = Anon.objects.last()

        videofile = lastvideo.videofile
        
        context = {
            'videofile': videofile,
        }
        
        return render(request, 'anons/anons_detail.html', context)

    def post(self, request, *args, **kwargs):
        new_comment = BlogComment(content = request.POST.get('content'), 
            author = self.request.user, blogpost_connected = self.get_object()
        )
        new_comment.save()
        
        return self.get(self, request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(AnonsDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Anon, id=self.kwargs['pk'])
        total_likes = stuff.likes.count()
        context['total_likes'] = total_likes
        
        data = super().get_context_data(**kwargs)

        comments_connected = BlogComment.objects.filter(
            blogpost_connected = self.get_object()).order_by('-date_posted')
        
        data['comments'] = comments_connected
        
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance = self.request.user)
        
        context.update(data)
        return context
    
class AnonsCreateView(CreateView):
    model = Anon
    template_name = 'anons/anons_create.html'

    fields = ('name', 'body', 'image', 'video', 'telegram', 'instagram', 'youtube')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    
    def test_func(self):
        return self.request.user.is_superuser

class AnonsUpdateView(UpdateView):
    model = Anon
    template_name = 'anons/anons_update.html'

    fields = ('name', 'body', 'image', 'video', 'telegram', 'instagram', 'youtube')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    
    def test_func(self):
        return self.request.user.is_superuser

class AnonsDeleteView(DeleteView):
    model = Anon
    template_name = 'anons/anons_delete.html'
    success_url = reverse_lazy('anons_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
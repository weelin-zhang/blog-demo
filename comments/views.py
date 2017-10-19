from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from django.http import HttpResponse
from .models import Comment
from .form import CommentForm
from django.views.generic import View
from blog.models import Post
import markdown


# Create your views here.


class PostCommentView(View):
    def post(self, request, post_pk):
        post = get_object_or_404(Post, pk=post_pk)
        comment_form = CommentForm(request.POST)
        # 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
        if comment_form.is_valid():
            # 在 处理 post 请求时候， 通过 comment_form = ArticleForm(request.POST)来获取一个填有用户数据的form
            # 在调用了 is_valid 方法以后 就可以通过 comment_form.cleaned_data ，返回一个 装有数据的字典
            d_d = comment_form.cleaned_data
            print(d_d)
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            comment = comment_form.save(commit=False)

            # 讲评论和文章关联起来
            comment.post = post
            # 最终将评论数据保存进数据库，调用模型实例的 save 方法
            comment.save()

            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            return redirect(reverse('blog:detail', kwargs={'pk': post_pk}))

            return redirect(post)  # 同上前提在Post的models中给Post类定义get_absolute_url方法
        else:
            d_d = comment_form.cleaned_data
            print(d_d)
            # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
            # 因此我们传了三个模板变量给 detail.html，
            # 一个是文章（Post），一个是评论列表，一个是表单 form
            # 注意这里我们用到了 post.comment_set.all() 方法，
            # 这个用法有点类似于 Post.objects.all()
            # 其作用是获取这篇 post 下的的全部评论，
            # 因为 Post 和 Comment 是 ForeignKey 关联的，
            # 因此使用 post.comment_set.all() 反向查询全部评论。
            comment_list = post.comment_set.all()
            post.body = markdown.markdown(post.body,
                                          extensions=[
                                              'markdown.extensions.extra',
                                              'markdown.extensions.codehilite',
                                              'markdown.extensions.toc',
                                          ])

            context = {'post': post,
                       'form': comment_form,
                       'comment_list': comment_list
                       }
            return render(request, 'detail.html', {'context': context})

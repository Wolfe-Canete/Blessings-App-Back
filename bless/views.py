from django.shortcuts import render
from rest_framework import generics
from .models import Blessing, Comment
from .serializers import BlessSerializer
from .serializers import CommentSerializer


class BlessingList(generics.ListCreateAPIView):
    queryset = Blessing.objects.all()
    serializer_class = BlessSerializer

class BlessingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blessing.objects.all()    
    serializer_class = BlessSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# functions for CRUD Later on

    #     def blessing_create(request):
#     if request.method !='POST':
#         form = BlessingForm()
#     else:
#         form = BlessingForm(request.POST)
#         if form.is_valid():
#             blessing = form.save()
#             return redirect('blessing_detail', pk=blessing.pk)
#     return render(
#         request,
#         'blessing/blessing_form.html',
#         {'form': form}
#     )

# def blessing_edit(request, pk):
#     bless_edit = Blessing.objects.get(pk=pk)
#     if request.method != "POST":
#         form = PostForm(instance=bless_edit)
#     else:
#         form = BlessingForm(request.POST, instance=bless_edit)
#         if form.is_valid():
#             bless_edit = form.save()
#             return redirect(
#                 'blessing_detail',
#                 pk=bless_edit.pk
#             )
#     return render(
#         request,
#         'blessing/blessing_form.html',
#         {'form', form}
#     )

# def blessing_delete(request, pk):
#     Blessing.objects.get(id=pk).delete()
#     return redirect('blessing_list')

# def comment_create(request):
#     if request.method !='POST':
#         form = CommentForm()
#     else:
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save()
#             return redirect('comment_detail', pk=comment.pk)
#     return render(
#         request,
#         'blessing/comment_form.html',
#         {'form': form}
#     )

# def comment_edit(request, pk):
#     comment = Comment.objects.get(pk=pk)
#     if request.method != "POST":
#         form = PostForm(instance=comment)
#     else:
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             comment = form.save()
#             return redirect(
#                 'comment_detail',
#                 pk=comment.pk
#             )
#     return render(
#         request,
#         'blessing/comment_form.html',
#         {'form', form}
#     )

# def comment_delete(request, pk):
#     Comment.objects.get(id=pk).delete()
#     return redirect('comment_list')
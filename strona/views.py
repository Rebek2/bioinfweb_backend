from django.shortcuts import render
from .serializer import *
from rest_framework import viewsets
from .DAL import Database
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes


def home(request):
    print('czesc')
    a = Database()
    print(a.retrieve_post_by_id(2))
    return render(request, 'Home.html')


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class MultimediaViewSet(viewsets.ModelViewSet):
    queryset = Multimedia.objects.all()
    serializer_class = MultimediaSerializer


class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer


@api_view(['GET'])
def CommentsOfPost(request,id):
    comments = Comment.objects.all().filter(post_id = id)
    serializer = CommentSerializer(comments,many=True)
    return Response(serializer.data)


@api_view(['POST'])
@parser_classes([JSONParser])
def UpdatePost(request, id):
    #print(id)
    #print(request.data)
    #print(request.data["author"], request.data["title"], request.data["content"])
    a = Database()
    return Response(a.modify_post_by_id(id, request.data["title"], request.data["content"], request.data["author"]))

@api_view(['POST'])
@parser_classes([JSONParser])
def AddPost(request):
    a = Database()
    a.modify_post_by_id(id, request.data[1])
    print(request.data)
    print(request.data["author"])
    return Response("",404)


@api_view(["GET"])
def PhotosOfPost(request,post_id):
    photos = Multimedia.objects.all().filter(post_id=post_id)

    serializer = MultimediaSerializer(photos,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def PhotosOfMember(request,id):
    photos = Multimedia.objects.all().filter(members_id = id)
    serializer = MultimediaSerializer(photos, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@parser_classes([JSONParser])
def PublishPost(request, id):
    a = Database()
    return Response(a.pulish_post(id, bool(request.data["choice"])))


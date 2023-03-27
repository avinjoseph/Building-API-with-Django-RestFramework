from django.shortcuts import render
from django.http import Http404, JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Advocate, Company
from .serializer import AdvocateSerializer,CompanySerializer
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates','advocates/:username']
    return Response(data)

@api_view(['GET','POST'])
def advocate_list(request):
    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query = ''

        advocates = Advocate.objects.filter(Q(name__icontains = query) | Q(bio__icontains = query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        query = request.POST.get('query')

        advocates = Advocate.objects.create(name = request.data['name'], bio = request.data['bio'])
        serializer = AdvocateSerializer(advocates, many=False)
        return Response(serializer.data)


class AdvocateDetails(APIView):

    def get_object(self, username):
        try:
            return Advocate.objects.get(name=username)
        except Advocate.DoesNotExist:
            raise JsonResponse('User not found')
        

    def get(self,request,username):
        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def put(self,request,username):
        advocate = self.get_object(username)
        advocate.name = request.data['name']
        advocate.bio = request.data['bio']
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
    
    def delete(self,request,username):
        advocate = self.get_object(username)
        advocate.delete()
        return Response('User was deleted')




# @api_view(['GET','DELETE','PUT'])
# def advocate_detail(request,username):
#     advocate = Advocate.objects.get(name=username)

#     if request.method == 'GET':
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         advocate.name = request.data['name']
#         advocate.bio = request.data['bio']
#         advocate.save()
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)
    
#     if request.method == 'DELETE':
#         advocate.delete()
#         return Response('User was deleted')



## Company endpoints

@api_view(['GET'])
def company_details(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies,many=True)
    return Response(serializer.data)


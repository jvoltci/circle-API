from django.shortcuts import render
from django.utils.functional import empty
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from circleApp.models import Products, Category, SubCategory
from circleApp.serializers import ProductSerializer, CategorySerializer, SubCategorySerializer


@csrf_exempt
def productApi(request, id=0):
    if request.method == 'GET':
        return JsonResponse("Invalid API", safe=False)

    elif request.method == 'POST':
        productData = JSONParser().parse(request)
        exists = Products.objects.filter(subCategory_id=productData['subCategory'], ProductName=productData['ProductName']).exists()
        if not exists:
            productSerializer = ProductSerializer(data=productData)
            if productSerializer.is_valid():
                productSerializer.save()
                return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    # elif request.method == "DELETE":
    #     product = Products.objects.get(ProductId=id)
    #     product.delete()
    #     return JsonResponse('Deleted Successfully!!', safe=False)

@csrf_exempt
def categoryApi(request, id=''):
    if request.method == 'GET':
        if id == '':
            categories = Category.objects.all()
            categorySerializer = CategorySerializer(categories, many=True)
            return JsonResponse(categorySerializer.data, safe=False)
        else:
            subCategories = SubCategory.objects.filter(category_id=id)
            subCategorySerializer = SubCategorySerializer(subCategories, many=True)
            return JsonResponse(subCategorySerializer.data, safe=False)

@csrf_exempt
def productCategoryApi(request, id=''):
    if request.method == 'GET':
        if id == '':
            return JsonResponse("Invalid API", safe=False)
        else:
            subCategoriesIds = SubCategory.objects.filter(category_id=id).values('id')
            Ids = []
            for item in subCategoriesIds:
                Ids.append(item['id'])

            products = Products.objects.filter(subCategory_id__in=Ids)
            productSerializer = ProductSerializer(products, many=True)
            return JsonResponse(productSerializer.data, safe=False)

@csrf_exempt
def productSubCategoryApi(request, id=''):
    if request.method == 'GET':
        if id == '':
            return JsonResponse("Invalid API", safe=False)
        else:
            products = Products.objects.filter(subCategory_id=id)
            productSerializer = ProductSerializer(products, many=True)
            return JsonResponse(productSerializer.data, safe=False)

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response

from myapp.models import Product
from myproject.settings import DEFAULT_FROM_EMAIL
from .serializers import ProductSerializer, MailSerializer

#For the class based view we would use APIview
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.core.mail import send_mail


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def products(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"details": "product added successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductView(APIView):
    PermissionClasses = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, pk):
        product = get_object_or_404(product, id=pk)
        
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def patch(self, request, pk):
        product = get_object_or_404(product, id=pk)
        
        serializer = ProductSerializer(product, data=request.data, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
            return Response({"detail": "product updated"})
    def put(self, request, pk):
        product = get_object_or_404(product, id=pk)
        serializer = ProductSerializer(product, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"detail": "product updated"})
        
    def delete(self, request, pk):
        product = get_object_or_404(product, id=pk)
        product.delete()
        return Response({"details": "Product deleted successfully"})


@api_view(["POST"])
def send_user_email(request):
    serializer = MailSerializer(data=request.data)
    if serializer.is_valid(raise_exception = True):
        subject = serializer.validated_data.get("subject") #type: ignore
        body = serializer.validated_data.get("body") #type: ignore
        receiver = serializer.validated_data.get("receiver") #type: ignore
        # Send email logic here
        
        send_mail(
            subject = str(subject),
            message = str(body),
            from_email = f"Reasonable Solutions <<{DEFAULT_FROM_EMAIL}>>",
            recipient_list = [str(receiver)]
        )
        
        
        return Response({"details": "Email sent successfully"})

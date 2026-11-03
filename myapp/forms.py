from django.forms import ModelForm
from myapp.models import Product
# from myapp.models import Student




class ProductForm(ModelForm):
    class Meta:
        model = Product
        # fields = "__all__"
        exclude= ["uploaded_by"]
        
# class StudentForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = "__all__"        
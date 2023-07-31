from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django import forms
from geopy.geocoders import Nominatim
 
def get_address(place):
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(place)
    return getLoc.address
class GeoForm(forms.Form):
    place=forms.CharField()
class GeoView(View):
    def get(self,request,*args,**kwargs):
        form=GeoForm()
        return render(request,"geo.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=GeoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            place=form.cleaned_data.get("place")
            address=get_address(place)
            print(address)
        return render(request,"geo.html",{"form":form,"result":address})

class OperationForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class RegistrationForm(forms.Form):
    firstname=forms.CharField()
    lastname=forms.CharField()
    email=forms.EmailField()
    username=forms.CharField()
    password=forms.CharField()
class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print("form is invalid")
        return render(request,"registration.html")
class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    

class AdditionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"addition.html")
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1+n2
        print(res)
        return render(request,"addition.html",{"result":res})
    
    
class SubtractionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"subtraction.html")
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1-n2
        print(res)
        return render(request,"subtraction.html",{"result":res})
    
class MultiplicationView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"multi.html")
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1*n2
        print(res)
        return render(request,"multi.html",{"result":res})
    
class DivisionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"divi.html")  
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1/n2
        print(res)
        return render(request,"divi.html",{"result":res})
class FactorialView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"fact.html")
    def post(self,request,*args,**kwargs):
        n=int(request.POST.get("num"))
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        
    
        return render(request,"fact.html",{"result":fact})
class PrimeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"prime.html")
    def post(self,request,*args,**kwargs):
        n=int(request.POST.get("num"))
        for i in range(2,n):
            if n%i==0:
                result="false"
                print(result)
                break
        else:
            result=True
            print(result)
        return render(request,"prime.html",{"res":result})

class PalindromeView(View):
    def get(self,request,*args,**kwargs):
         return render(request,"palidrome.html")
    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")
        if n==n[: : -1]:
            result="True"
            print(result)
        else:
            result="False"
            print(result)
        return render(request,"palidrome.html",{"res":result})
    
class ArmstrongView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"armstrong.html")
    def post(self,request,*args,**kwargs):
        n=int(request.POST.get("num"))
        
        order = len(str(n))
        sum = 0

        temp = n
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if n == sum:
            result="True"
            print(result)
        else:
            result="False"
            print(result)
        return render(request,"armstrong.html",{"res":result})
class LimitView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"limit.html")
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        even=[]
        for i in range(n1,n2):
            if i%2==0:
                even.append(i)
        return render(request,"limit.html",{"res":even})
class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"home.html")
class HealthView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"health.html")
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        s=request.POST.get("sex")
        bmi=n1/n2
        round(bmi,2)
        context={"gender":"","risk":"","shape":"","bmi":bmi}
        if s=="female":
            if bmi<=0.80:
                context["gender"]="female"
                context["risk"]="low"
                context["shape"]="pear"
            elif bmi<=0.85 and bmi>=0.81:
                context["gender"]="female"
                context["risk"]="moderate"
                context["shape"]="avocado"
            elif bmi>=0.85:
                context["gender"]="female"
                context["risk"]="high"
                context["shape"]="apple"
        elif s=="male":
            if bmi<=0.95:
                context["gender"]="male"
                context["risk"]="low"
                context["shape"]="pear"
            elif bmi<=1.0 and bmi>=0.96:
                 context["gender"]="male"
                 context["risk"]="moderate"
                 context["shape"]="avocado"
            elif bmi>1.0:
                context["gender"]="male"
                context["risk"]="high"
                context["shape"]="apple"
        return render(request,"health.html",context)
    
class TemparatureView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"temp.html")
    def post(self,request,*args,**kwargs):
        n=int(request.POST.get("value"))
        result=(n * 9/5) + 32
        return render(request,"temp.html",{"res":result})
class ExponentView(View):
    def get(self,request,*args,**kwargs):
        form=OperationForm()
        return render(request,"exponent.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=OperationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1**n2
            return render(request,"exponent.html",{"result":result})


        

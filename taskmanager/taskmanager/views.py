from django.shortcuts import render

def about(request):
	return render(request,'about.html')
def home(request):
	return render(request,'home.html')
def hoba(request):
	user_text=request.GET['usertext']
	r_text=user_text[::-1]
	return render(request,'hoba.html',{'usertext':user_text})


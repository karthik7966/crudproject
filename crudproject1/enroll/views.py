from django.shortcuts import render,redirect, HttpResponseRedirect
from .forms import StudentRegistration
from .models import user

#This Function Will Add new Item and Show All Items

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST,request.FILES)
        if fm.is_valid():
        #  nm = fm.cleaned_data['name']
        #  em = fm.cleaned_data['email']
        #  pw = fm.cleaned_data['password']
        
        #  reg = user(name=nm,email=em,password=pw)
         fm.save()
         fm = StudentRegistration()
         return redirect('addandshow')
    else:
        fm = StudentRegistration()
        stud = user.objects.all()
        return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud})


#This Function will Update/edit
def update_data(request,pk):
    # fm = StudentRegistration()
    # if request.method == 'POST':
    #     pi = user.objects.get(id=pk)
    #     fm = StudentRegistration(request.POST,instance=fm)
    #     if fm.is_valid():
    #         fm.save()
    # else:
    #     pi = user.objects.get(id=pk)
    #     fm = StudentRegistration(instance = pi)
    # return render (request, 'enroll/updatestudent.html', {'form':fm})

    stu=user.objects.get(id=pk)
    fm=StudentRegistration(instance=stu)
    if request.method=='POST':
        fm=StudentRegistration(request.POST,request.FILES,instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('addandshow')
    context={
        "fm":fm
    }
    return render(request,'enroll/updatestudent.html',context)


#This Function Will Delete 
def delete_data(request,pk):
    pi = user.objects.get(id = pk)
    if request.method == 'POST':
        pi = user.objects.get(id = pk)
        pi.delete()
        # return HttpResponseRedirect('/')
        return redirect('addandshow')


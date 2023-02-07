
from django.http import HttpResponse  
from collections import Counter
from django.shortcuts import render, redirect
import os
from django.contrib import messages
import pandas as pd
from .models import UserForm #forms.py
from django.core.files.storage import FileSystemStorage
from .forms import UserForm 

# Create your views here.
def index(request):

    global income,expense,month
    
    if request.method == 'POST':  
        user_info = UserForm(request.POST, request.FILES)  
        uploaded_file = request.FILES['file']
        income = "Income"
        expense = "Expenses"
        month = "Month"

        if user_info.is_valid(): 
            savefile = FileSystemStorage()

            name = savefile.save(uploaded_file.name, uploaded_file) 
           
            d = os.getcwd() # how we get the current dorectory
            file_directory = d+'/media/'+name #saving the file in the media directory
            readfile(file_directory)


            return redirect("displayData") 
        
           
    else:  
        user_info = UserForm()  
        return render(request,"index.html",{'form':user_info})    
       

    
            
def readfile(user_file):
    
    global rows,columns,data,excel_file

    excel_file = pd.read_excel(user_file)
    
    data = pd.DataFrame(data=excel_file, index=None)
    
    # rows = len(data.axes[0])
    # columns = len(data.axes[1])


def displayData(request):

    # userInfo  = UserForm.objects.all()
    # labels=[]
    
    # queryset = UserForm.objects.all()
    
    # for row in queryset:
    #        labels.append(" ".join(row))
     
   
    # return render(request,"displayData.html",{
    #     "labes":labels
    # })    
    

    monthly_income= [] 
    expenses=[]
    months=[]
    for x in data[income]:
         monthly_income.append(x)
    
    for x in data[expense]:
        expenses.append(x)

    for x in data[month]:
        months.append(x)

    # my_dashboard = dict(Counter( monthly_income)) #{'A121': 282, 'A122': 232, 'A124': 154, 'A123': 332}



    # keys = monthly_income # {'A121', 'A122', 'A124', 'A123'}
    # values = expenses
    # value2 =months

    # listkeys = []
    # listvalues = []

    # for x in keys:
    #     listkeys.append(x)

    # for y in values:
    #     listvalues.append(y)

    # print(listkeys)
    # print(listvalues)

    context = {
        'monthly_income': monthly_income ,
        'expenses': expenses,
        'months' :months,}
    
    return render(request, 'displayData.html', context)

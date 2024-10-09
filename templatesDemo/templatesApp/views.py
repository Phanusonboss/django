from django.shortcuts import render


def renderTemplate(request):
    myDict={"name":"Thamonwan"}
    return render(request, 'templatesApp/firstTemplate.html',context=myDict)


def renderEmployee(request):
    myDict={"id":334,"name":"Thamonwan","salary":10000}
    return render(request, 'templatesApp/employeeTemplate.html',context=myDict)

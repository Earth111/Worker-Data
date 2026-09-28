from django.shortcuts import render , redirect
from django.http import HttpResponse
from myApp.models import Person
from django.contrib import messages

# Create your views here.
def index(request):
    all_person = Person.objects.order_by("id")
    return render(request, "index.html", {"all": all_person})

def about(request):
    return render(request, "about.html")

def form(request) :
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        used_ids = set(Person.objects.values_list("id", flat=True))
        new_id = 1
        while new_id in used_ids:
            new_id += 1

        person = Person.objects.create(
            id=new_id,
            name=name,
            age=age
        )
        person.save()
        messages.success(request, "บันทึกข้อมูลสำเร็จ")
        return redirect("/")
    else :
        return render(request, "form.html")
    
def edit(request, person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]  
        person.save()
        messages.success(request, "แก้ไขข้อมูลสำเร็จ")
        return redirect("/")
    else : 
        person = Person.objects.get(id=person_id)
        return render(request, "edit.html", {"person": person})
    
def delete(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request, "ลบข้อมูลสำเร็จ")
    return redirect("/")
from django.shortcuts import render, redirect
from crud.forms import ProfessorForm, AlunoForm
from crud.models import Professor, Aluno


# Create your views here.
def home(request):
    data = {}
    search_prof = request.GET.get('search_prof')
    search_aluno = request.GET.get('search_aluno')
    if search_prof:
        data['pf'] = Professor.objects.filter(nome__icontains=search_prof)
    else:
        data['pf'] = Professor.objects.all()

    if search_aluno:
        data['al'] = Aluno.objects.filter(nome__icontains=search_aluno)
    else:
        data['al'] = Aluno.objects.all()
    return render(request, 'index.html', data)

def form_prof(request):
    data = {}
    data['form_prof'] = ProfessorForm()
    return render(request, 'form_prof.html', data)

def form_aluno(request):
    data = {}
    data['form_aluno'] = AlunoForm()
    return render(request, 'form_aluno.html', data)

def create(request):
    form_a = AlunoForm(request.POST or None)
    form_p = ProfessorForm(request.POST or None)
    if form_a.is_valid():
        form_a.save()
        return redirect('home')
    if form_p.is_valid():
        form_p.save()
        return redirect('home')

def view_aluno(request, pk):
    data = {}
    data['al'] = Aluno.objects.get(pk=pk)
    return render(request,'view_aluno.html', data)

def view_prof(request, pk):
    data = {}
    data['pf'] = Professor.objects.get(pk=pk)
    return render(request,'view_prof.html', data)

def edit_prof(request, pk):
    data = {}
    data['pf'] = Professor.objects.get(pk=pk)
    data['form_prof'] = ProfessorForm(instance=data['pf'])
    return render(request,'form_prof.html',data)

def edit_aluno(request, pk):
    data = {}
    data['al'] = Aluno.objects.get(pk=pk)
    data['form_aluno'] = AlunoForm(instance=data['al'])
    return render(request, 'form_aluno.html', data)

def update_aluno(request, pk):
    data = {}
    data['al'] = Aluno.objects.get(pk=pk)
    form = AlunoForm(request.POST or None, instance=data['al'])
    if form.is_valid():
        form.save()
        return redirect('home')

def update_prof(request, pk):
    data = {}
    data['pf'] = Professor.objects.get(pk=pk)
    form = ProfessorForm(request.POST or None, instance=data['pf'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete_aluno(request,pk):
    al = Aluno.objects.get(pk=pk)
    al.delete()
    return redirect('home')

def delete_prof(request, pk):
    pf = Professor.objects.get(pk=pk)
    pf.delete()
    return redirect('home')
from django.forms import ModelForm
from crud.models import Professor, Aluno

# Create the form class.
class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'disciplina', 'registro']

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'turma', 'serie', 'cgm']
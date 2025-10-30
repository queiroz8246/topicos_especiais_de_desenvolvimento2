class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
    def __str__(self):
        return f"Titulo: {self.titulo}, Descricao: {self.descricao}"

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        for tarefa in self.tarefas:
            return f"Titulo: {tarefa.titulo}, Descricao: {tarefa.descricao}"

gerenciar = GerenciadorTarefas()

while True:

    titulo = input("Digite o titulo: ")
    if titulo.lower() == "sair":
        break
    descricao = input("digite a descrição: ")
    tarefa = Tarefa(titulo, descricao)

    gerenciar.adicionar_tarefa(tarefa)
    print(gerenciar.listar_tarefas())


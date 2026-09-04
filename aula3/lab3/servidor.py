import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://broker:5556")
tarefas = []

while True:
    texto = ""
    message = socket.recv().decode()
    partes = message.split(" ", 1)
    comando = partes[0]

    if comando == "sair":
        socket.send_string("Até!")
        break

    elif comando == "adicionar":
        tarefa = partes[1]
        tarefas.append(tarefa)
        texto += "Tarefa criada!\n"

    elif comando == "remover":
        tarefa = partes[1]
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            texto += "Tarefa removida!\n"
        else:
            texto += "Tarefa não encontrada.\n"

    elif comando == "lista":
        for i, tarefa in enumerate(tarefas, start=1):
            texto += f"{i}. {tarefa}\n"

    else:
        texto += "Comando desconhecido.\n"

    socket.send_string(texto)
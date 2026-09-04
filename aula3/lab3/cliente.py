import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://broker:5555")

while True:
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Nome da tarefa: ")
        socket.send_string(f"adicionar {tarefa}")
    elif opcao == "2":
        tarefa = input("Nome da tarefa a remover: ")
        socket.send_string(f"remover {tarefa}")
    elif opcao == "3":
        socket.send_string("lista")
    elif opcao == "4":
        socket.send_string("sair")
        print(socket.recv_string())
        break
    else:
        continue

    resposta = socket.recv_string()
    print(resposta)
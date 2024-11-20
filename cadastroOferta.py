def chatbot():
    print("Bem-vindo ao CaféBot! Vamos começar com seu cadastro.")
    
    # Cadastro do usuário
    nome = input("Por favor, digite seu nome: ")
    while not nome.strip():
        print("O nome não pode estar vazio.")
        nome = input("Por favor, digite seu nome: ")

    email = input("Por favor, digite seu e-mail: ")
    while "@" not in email or "." not in email:
        print("E-mail inválido. Tente novamente.")
        email = input("Por favor, digite seu e-mail: ")

    idade = input("Por favor, digite sua idade: ")
    while not idade.isdigit() or int(idade) <= 0:
        print("Idade inválida. Digite um número maior que 0.")
        idade = input("Por favor, digite sua idade: ")
    
    print(f"\nObrigado, {nome}! Cadastro realizado com sucesso.")
    
    # Oferta de cafés
    print("\nTemos dois tipos de café disponíveis:")
    print("1. Bag Cítrico")
    print("2. Bag Suave")
    
    escolha = input("Qual você gostaria de experimentar? (Digite 1 ou 2): ")
    while escolha not in ["1", "2"]:
        print("Escolha inválida. Por favor, digite 1 para Bag Cítrico ou 2 para Bag Suave.")
        escolha = input("Qual você gostaria de experimentar? (Digite 1 ou 2): ")
    
    if escolha == "1":
        print("\nVocê escolheu o Bag Cítrico! Uma excelente escolha para quem gosta de sabores vibrantes.")
    elif escolha == "2":
        print("\nVocê escolheu o Bag Suave! Perfeito para um momento de relaxamento.")
    
    print("\nObrigado por usar o CaféBot! Aproveite seu café!")

# Executar o chatbot
if __name__ == "__main__":
    chatbot()

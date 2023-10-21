import os
import sys

def clear():
    os.system("clear")

e = 1

nome = str(input("Digite seu nome: "))

clear()

print(f"Olá {nome}! Seja bem-vindo(a) ao sistema de instruções da SALESFORCE.")
print("")

while (e != 2):
    print("Escolha uma das opções para seguir: ")
    print("1 - Informações sobre nossos produtos")
    print("2 - Entre em contato conosco")
    print("3 - Visite nossas redes sociais")
    print("4 - Participar do programa de fidelidade")
    print("")

    op = int(input("Digite a opção desejada: "))

    match op:
        case 1:
            clear()
            print(f"Boa escolha {nome}! Sobre qual produto você deseja obter informações?")
            print("")
            print("1 - Vendas")
            print("2 - Atendimento ao Cliente")
            print("3 - Marketing")
            print("4 - Commerce")
            print("5 - Data Cloud")
            print("6 - Voltar para o início")
            print("")

            produto = int(input("Digite a opção desejada: "))

            match produto:
                case 1:
                    clear()
                    print(f"O serviço de vendas da Salesforce é uma poderosa plataforma de automação de vendas e gerenciamento de relacionamento com o cliente (CRM) projetada para ajudar as empresas a otimizar seus processos de vendas. Ele oferece uma variedade de recursos essenciais:")
                    print("")
                    print("Gerenciamento de Leads e Oportunidades: Permite rastrear e gerenciar leads, oportunidades de vendas e clientes em potencial, fornecendo uma visão clara do funil de vendas.")
                    print("")
                    print("Automação de Vendas: Ajuda as equipes de vendas a automatizar tarefas repetitivas, como o acompanhamento de contatos, envio de e-mails e agendamento de reuniões, economizando tempo e aumentando a produtividade.")
                    print("")
                    print("Análise e Relatórios: Oferece ferramentas de análise avançadas que permitem às empresas avaliar o desempenho de vendas, identificar tendências e tomar decisões baseadas em dados.")
                    print("")


                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 2:
                    clear()
                    print(f"O serviço de atendimento ao cliente da Salesforce é uma plataforma de gerenciamento de relacionamento com o cliente (CRM) que se concentra em fornecer experiências excepcionais aos clientes. Com recursos avançados, permite que empresas ofereçam suporte eficiente e personalizado:")
                    print("")
                    print("")
                    print("Centralização de Dados do Cliente: Reúne informações de clientes em um único local, capacitando as equipes de atendimento a acessar informações cruciais rapidamente.")
                    print("")
                    print("Automação de Suporte: Automatiza tarefas de suporte, como triagem de solicitações, roteamento de casos e respostas automatizadas, para atender às necessidades dos clientes de forma mais eficaz.")
                    print("")
                    print("Gestão de Casos: Facilita o acompanhamento e resolução de casos de suporte, melhorando a eficiência e a transparência do processo.")
                    print("")
                    print("Integração com Canais de Comunicação: Oferece suporte a diversos canais de comunicação, como chat ao vivo, e-mail e redes sociais, para proporcionar atendimento multicanal.")
                    print("")
                    print("")
                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 3:
                    clear()
                    print(f"O serviço de marketing da Salesforce é uma plataforma líder em automação de marketing e gerenciamento de relacionamento com o cliente (CRM) que capacita empresas a criar campanhas de marketing altamente eficazes:")
                    print("")
                    print("")
                    print("Automação de Marketing: Permite a automação de tarefas de marketing, como o envio de e-mails, segmentação de público e acompanhamento de leads, economizando tempo e recursos.")
                    print("")
                    print("Personalização Avançada: Oferece a capacidade de personalizar campanhas de marketing com base no comportamento e preferências dos clientes, proporcionando experiências mais relevantes.")
                    print("")
                    print("Gestão de Campanhas Multicanais: Facilita a criação e gerenciamento de campanhas em vários canais, incluindo e-mail, mídias sociais, anúncios online e muito mais.")
                    print("")
                    print("Análises de Marketing: Fornece análises e relatórios detalhados para avaliar o desempenho de campanhas, identificar tendências e otimizar estratégias.")
                    print("")
                    print("Integração com Vendas e Atendimento: Permite a sincronização perfeita com as equipes de vendas e atendimento ao cliente, garantindo a consistência nas interações com os clientes.")
                    print("")
                    print("")

                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 4:
                    clear()
                    print(f"O serviço de e-commerce da Salesforce é uma plataforma completa que possibilita a criação e gestão de lojas online altamente eficazes e personalizadas:")
                    print("")
                    print("")
                    print("Construção de Lojas Virtuais: Permite que empresas desenvolvam lojas online atraentes e totalmente funcionais para vender produtos ou serviços.")
                    print("")
                    print("Personalização e Experiência do Cliente: Oferece recursos de personalização avançada para criar experiências de compra únicas, adaptadas às preferências dos clientes.")
                    print("")
                    print("Gestão de Pedidos e Inventário: Facilita o gerenciamento de pedidos, estoque e logística, garantindo uma operação eficiente.")
                    print("")
                    print("Integração de Pagamentos e Marketing: Integra-se com sistemas de pagamento, automação de marketing e análise de dados para impulsionar as vendas e aumentar a eficácia das campanhas.")
                    print("")
                    print("Segurança e Escalabilidade: Oferece segurança robusta e escalabilidade para acomodar o crescimento do e-commerce e proteger os dados dos clientes.")
                    print("")
                    print("")

                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 5:
                    clear()
                    print(f"O serviço de Data Cloud da Salesforce é uma solução inovadora que permite às empresas acessar e aproveitar uma vasta gama de dados e informações valiosas. Essa plataforma oferece:")
                    print("")
                    print("")
                    print("Acesso a Dados Externos: Facilita o acesso a dados externos, como informações demográficas, empresariais e de consumidores, enriquecendo as estratégias de marketing e vendas.")
                    print("")
                    print("Conexão com Terceiros: Integra-se com provedores de dados externos, permitindo a obtenção de dados de fontes confiáveis.")
                    print("")
                    print("Enriquecimento de Dados: Enriquece os registros de clientes com informações adicionais, proporcionando uma visão mais completa do público-alvo.")
                    print("")
                    print("Segmentação Avançada: Possibilita a segmentação precisa de público e campanhas com base em dados enriquecidos.")
                    print("")
                    print("Tomada de Decisão Informada: Capacita as empresas a tomar decisões mais informadas e estratégicas, melhorando o desempenho e a eficácia em todas as áreas de negócio.")
                    print("")
                    print("")

                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 6:
                    clear()

        case 2:
            clear()
            print(f"Ok {nome}. Por qual canal deseja entrar em contato?")
            print("")
            print("")
            print("1 - Telefone")
            print("2 - Whatsapp")
            print("3 - E-mail")
            print("4 - Instagram")
            print("")
            print("")

            canal = int(input("Digite a opção desejada: "))

            match canal:
                case 1:
                    clear()
                    print("Para entrar em contato conosco via telefone, basta ligar no número abaixo para ser atendido por um dos nossos funcionários:")
                    print("")
                    print("0800-1234-4321")
                    print("")
                    print("")
                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 2:
                    clear()
                    print("Para entrar em contato conosco via Whatsapp, basta salvar o número abaixo e enviar uma mensagem com seu nome e sua dúvida:")
                    print("")
                    print("11 91234-4321")
                    print("")
                    print("")
                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 3:
                    print("Para entrar em contato conosco via E-mail, basta enviar sua mensagem com seu nome e sua dúvida no endereço abaixo:")
                    print("")
                    print("salesforce@atendimento.com")
                    print("")
                    print("")
                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()



            clear()
            print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
            print("")
            print("1 - Voltar ao menu inicial")
            print("2 - Encerrar o programa.")
            print("")

            i = int(input("Digite a opção desejada: "))

            if (i == 1):
                clear()
            if (i == 2):
                clear()
                sys.exit()
        case 3:
            clear()
            print(f"Boa escolha {nome}! Segue abaixo nossas redes sociais:")
            print("Intagram: @salesforcebrasil")
            print("LinkedIn: SalesforceBrasil")
            print("")

            input("Pressione ENTER para continuar...")

            clear()
            print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
            print("")
            print("1 - Voltar ao menu inicial")
            print("2 - Encerrar o programa.")
            print("")

            i = int(input("Digite a opção desejada: "))

            if (i == 1):
                clear()
            if (i == 2):
                clear()
                sys.exit()
        case 4:
            clear()
            print(f"Que bom que deseja participar do nosso programa de fidelidade {nome}! Mas antes vamos saber um pouco melhor sobre o programa...")
            print("")
            print("O programa de fidelidade da Salesforce, denominado \"Salesforce Loyalty Plus\",")
            print("oferece aos clientes uma experiência excepcional e recompensadora. Com base na premiada")
            print("plataforma Salesforce, ele permite que as empresas personalizem ofertas, melhorem o")
            print("atendimento ao cliente e incentivem a fidelização. Os participantes ganham pontos por")
            print("engajamento e compras, que podem ser resgatados por descontos, serviços premium e acesso a")
            print("recursos exclusivos. O \"Salesforce Loyalty Plus\" impulsiona a satisfação do cliente e o")
            print("crescimento dos negócios, estabelecendo uma conexão duradoura entre empresas e clientes.")
            print("Uma maneira eficaz de recompensar e manter a lealdade em um mundo digital.")
            print("")

            input("Pressione ENTER para continuar...")

            clear()
            print(f"Obrigado pelo acesso {nome}! Você deseja voltar ao menu inicial ou finalizar o programa?")
            print("")
            print("1 - Voltar ao menu inicial")
            print("2 - Encerrar o programa.")
            print("")

            i = int(input("Digite a opção desejada: "))

            if (i == 1):
                clear()
            if (i == 2):
                clear()
                sys.exit()

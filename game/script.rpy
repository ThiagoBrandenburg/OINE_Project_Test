define s = Character('Sylvie', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")
define ct = Character('Catarina', color="#34eb3a")
define eu = Character('Eu',color="#000000")
define hl = Character('Helena',color="#008cff")

#Define Images

#personagens
image catarina happy ideia:
    "catarina happy ideia.png"
    zoom 0.3

image catarina angery:
    "catarina serious standing.png"
    zoom 0.3    

image catarina felicidade:
    "catarina happy explaining.png"
    zoom 0.3  

image bg entrada:
    "bg entrada.png"
    zoom 2.6

#Backgrounds
image p2d:
    "labP2D.png"
image bg andar1:
    "bg andar1.jpg"
    zoom 0.5

image bg terreo:
    "bg terreo.JPG"
    zoom 0.59
image biblioteca:
    "biblioteca.jpg"
    zoom 2.2

image restaurante:
    "bg_ru.jpeg"
    zoom 0.7

image placaF:
    "placaF.png"


#define flags -> se 0 então nn visitou ainda, se 1 já visitou, pra dar a primeira explicação
default terreo = 0
default primeiro_andar = 0
default segundo_andar = 0
default funcao = 0
default p2d = 0
default colmeia = 0
default secretaria = 0
default sala_prof = 0
default auditorio = 0
default biblioteca = 0
default ru = 0




label start:

    scene bg entrada

    eu "Nossa, é o meu primeiro dia na Udesc, estou ansioso!"

    eu "Estou curioso para conhecer cada canto dessa Universidade"

    eu "Mas..."

    eu "Por onde eu começo?"

    show catarina happy ideia at right

    ct "Olá, Meu nome é Catarina, você é calouro?"

    eu "Sim, sou calouro"

    ct "Ah! Então você é calouro, eu posso mostrar as partes interssantes do campus para você!"

    eu "Puxa você pode mesmo? Muito Obrigado"

    ct "Sem problemas, primeiro deixe eu te mostrar onde é o nosso bloco da Computação"
   

    #ct "Saia daqui imediatamente se quer manter sua sanidade!"
    # ct "Olá, Meu nome é Catarina, você é calouro?"

    # eu "S-sim?!"

    # ""

    # ct "Não, vc não é, volte imediatamente"

menu d_guarita:
    "O que farei?"
    
    "Seguir Catarina":
        scene placaF
        "Depois de uma árdua jornada subindo o morro do cct, você chegou ao bloco F"
    
        eu "Nossa, como é difícil chegar aqui"

        show catarina angery at right

        ct "Pois é, nosso campus ainda tem problemas de acessibilidade, mas tenho certeza que algo está será feito a respeito"

        show catarina felicidade at right

        ct "Mas vamos falar de coisas felizes! Há tantos laboratórios para conhecer, e lugares a visitar! Tenho certeza que todos estarão de braços abertos para nos receber!"

        jump terreo


        


# label fugir:
#     "Você decidiu que era uma boa ideia voltar e não entrar na Udesc"

#     "Good Ending"

#     return  

# label ficar:
#     "Você ficou, big mistake"
#     return


label terreo:
    scene bg terreo
    show catarina happy ideia at right
    ct "Este é o Térreo do Bloco L"
    if terreo == 0:
        show catarina happy ideia
        
        ct "No terreo, além das salas de aula e do ambiente de estudo, temos a maioria dos laboratórios de pesquisa e extensão"

        eu "Que tipo de laboratórios há aqui?"

        ct "Existem laboratório de Imagem, de software livre, de lógica... Nossa, existem tantos que não consigo lembrar agora!, vamos ter que explorar um por um"

        eu "Como eu faço para me juntar a um laboratório?"

        ct "Os laboratórios abrem processos seletivos periodicamente, mas é interessante buscar serviços voluntários"

        ct "Falar com os professores responsáveis de cada laboratório também é uma boa ideia"

        ct "Você ainda pode achar várias informações nas redes sociais"

        eu "Vou começar a seguir vários laboratórios!"
        
        eu "Quero visitar um!"
        $ terreo = 1
    menu:
        "Para onde devo ir?"

        "teste":
            $ terreo = 0
            jump terreo

        "Laboratório Função":
            jump function
        
        "Laboratório Colmeia":
            jump colmeia

        "Laboratório P2D":
            jump labp2d

        "Primeiro Andar":
            jump andar1
        
        "biblioteca":
            jump biblioteca
            
        
        "RU":
            jump ru
    

label andar1:
    scene bg andar1
    "Este é o primeiro andar"
    if primeiro_andar == 0:
        show catarina happy ideia
        ct "primeira vez no primeiro ein fml parabéns woop"
        $ primeiro_andar = 1
    menu:
        "Para onde devo ir?"

        "Secretaría":
            jump secretaria

        "Salas dos professores":
            jump sala_prof

        "Segundo Andar":
            jump andar2
    
        "Terreo":
            jump terreo

        


label andar2:
    "Este é o Segundo Andar"
    if segundo_andar == 0:
        show catarina happy ideia
        ct "primeira vez no segundo ein fml parabéns woop"
        $ segundo_andar = 1
    menu:
        "Para onde devo ir?"

        "Auditório":
            jump auditorio
        
        "Primeiro Andar":
            jump andar1
        



#salas no terreo
label labp2d:
    scene p2d
    show catarina felicidade at left
    
    ct "Esse é o LabP2D, eu conheço uma pessoa que trabalha aqui que pode apresentar apresentar esse lugar."
    show catarina happy ideia
    hl "Hmpf, você por acaso está DISTRIBUINDO as responsabilidades de apresentar os laboratórios, Catarina?"

    ct "Ah, aqui está ela, essa é a Helena! Ela é bolsista de um dos professores do laboratório" 
    
    ct "Então, Helena, pode nos explicar o que se faz aqui?"

    hl "Hmmmmmmm"

    hl "Ok, aceitarei essa requisição." 
    
    hl "O LabP2D é um laboratório de processamento paralelo e distribuído" 
    
    hl "A principal atividade do laboratório é o gerenciamento de nuvens. Na Nuvem Computacional privada do laboratório, estão hospedados diversos projetos da Universidade"

    "Helena aponta para os computadores no fundo da sala"

    hl "Aqueles são os servidores, esses servidores são computadores poderosos que são utilizados por alguns projetos da universidade"
    jump terreo

label function:
    "função"
    jump terreo

label colmeia:
    "colmeia"
    jump terreo


#salas no primeiro
label secretaria:
    "secretaria"
    jump andar1

label sala_prof:
    "sala prof"
    jump andar1

#salas no terceiro
label auditorio:
    "auditório"
    jump andar2

#biblioteca e RU
label biblioteca:
    "Biblioteca"
    scene biblioteca
    ct"owowowow"
    menu:
        "Para onde devo ir?"
        "restaurante":
            jump ru
        "terreo":
            jump terreo

label ru:
    "ru"
    scene restaurante
    ct"wowowowowowowo"
    menu:
        "Para onde devo ir?"
        "bibilioteca":
            jump biblioteca
        "terreo":
            jump terreo

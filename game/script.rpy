define s = Character('Sylvie', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")
define ct = Character('Catarina', color="#34eb3a")
define eu = Character('Eu',color="#ffffff")

#Define Images

image bg entrada:
    "bg entrada.png"
    zoom 2.6

image catarina happy ideia:
    "catarina happy ideia.png"
    zoom 0.3
#Backgrounds
image bg andar1:
    "bg andar1.jpg"
    zoom 0.5

image bg terreo:
    "bg terreo.JPG"
    zoom 0.59



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

    "Estou curioso para conhecer cada canto dessa Universidade"

    "Mas..."

    "Por onde eu começo?"

    show catarina happy ideia at right

    #ct "Saia daqui imediatamente se quer manter sua sanidade!"
    ct "Olá, Meu nome é Catarina, você é calouro?"

    eu "S-sim?!"

    ""

    ct "Não, vc não é, volte imediatamente"

menu d_guarita:
    "O que farei?"

    "Irei fugir":
        jump fugir
    
    "Não renunciarei":
        jump ficar
    
    "Ir para o terreo do L":
        jump terreo


label fugir:
    "Você decidiu que era uma boa ideia voltar e não entrar na Udesc"

    "Good Ending"

    return  

label ficar:
    "Você ficou, big mistake"
    return


label terreo:
    scene bg terreo
    show catarina happy ideia at right
    ct "Este é o Térreo do Bloco L"
    if terreo == 0:
        show catarina happy ideia
        ct "primeira vez no terreo ein fml parabéns woop"
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

        "Primeiro Andar":
            jump andar1

label labp2d:
    "Que "
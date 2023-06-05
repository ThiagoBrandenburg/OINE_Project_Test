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

image bg andar1:
    "bg andar1.jpg"
    zoom 0.5

#Backgrounds

label start:
    

    scene bg entrada

    eu "Nossa, é o meu primeiro dia na Udesc, estou ansioso!"

    "Estou curioso para conhecer cada canto dessa Universidade"

    "Mas..."

    "Por onde eu começo?"

    show catarina happy ideia at right

    #ct "Saia daqui imediatamente se quer manter sua sanidade!"
    ct "Olá, Meu nome é Catarina, você é CALOURO?"

    eu "S-sim?!"

    ct "Não, vc não é, volte imediatamente"

menu d_guarita:
    "O que farei?"

    "Irei fugir":
        jump fugir
    
    "Não renunciarei":
        jump ficar
    
    "Ir para o terreo do L":
        jump d_terreo


label fugir:
    "Você decidiu que era uma boa ideia voltar e não entrar na Udesc"

    "Good Ending"

    return  

label ficar:
    "Você ficou"


label terreo:
    "Este é o Térreo do Bloco L"
    menu:
        "Para onde devo ir?"

        "Primeiro Andar":
            jump andar1
    

label andar1:
    scene bg andar1
    "Este é o primeiro andar"
    menu:
        "Para onde devo ir?"

        "Terreo":
            jump terreo
        
        "Segundo Andar":
            jump andar2
    

label andar2:
    "Este é o Segundo Andar"
    menu:
        "Para onde devo ir?"

        "Primeiro Andar":
            jump andar1

label labp2d:
    "Que "
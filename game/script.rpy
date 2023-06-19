﻿define s = Character('Sylvie', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")
define ct = Character('Catarina', color="#34eb3a")
define eu = Character('Eu',color="#000000")
define hl = Character('Helena',color="#008cff")
define bia = Character('Beatriz',color="#ff9100")
define supochan = Character('Funcionaria do suporte',color="#ff0000")
define jas = Character('Jasmine',color="#ff0000")


#Define Images

#personagens
image catarina happy ideia:
    "catarina happy ideia.png"
    zoom 0.3

image catarina angry:
    "catarina serious standing.png"
    zoom 0.3    

image catarina felicidade:
    "catarina happy explaining.png"
    zoom 0.3  

image supochan angry:
    "supochan angry.png"
    zoom 0.3
    
image supochan angry pointing:
    "supochan angry pointing.png"
    zoom 0.3
    
image supochan flushed:
    "supochan flushed.png"
    zoom 0.3





#Backgrounds
image segundo_andar:
    "segundo andar.png"

image bg entrada:
    "bg entrada.png"
    zoom 2.6    

image colmeia:
    "colmeia.png"

image labp2d_bg:
    "labP2D.png"

image funcao:
    "funcao.png"

image bg andar1:
    "bg andar1.png"

image bg terreo:
    "bg terreo.png"

image biblioteca:
    "biblioteca.jpg"
    zoom 2.2

image restaurante:
    "bg_ru.jpeg"
    zoom 0.7

image placaF:
    "placaF.png"

image suporte dentro:
    "suporte_dentro.png"

image suporte fora:
    "suporte_fora.png"

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

        show catarina angry at right

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
    scene segundo_andar
    "Este é o Segundo Andar"
    if segundo_andar == 0:
        show catarina happy ideia
        ct "primeira vez no segundo ein fml parabéns woop"
        $ segundo_andar = 1
    menu:
        "Para onde devo ir?"

        "Auditório":
            jump auditorio
        
        "Suporte":
            jump suporte

        "Primeiro Andar":
            jump andar1
        



#salas no terreo
label labp2d:
    scene labp2d_bg
    
    

    ct "Esse é o LabP2D, eu conheço uma pessoa que trabalha aqui que pode apresentar apresentar esse lugar."

    helena "Hmpf, você por acaso está DISTRIBUINDO as responsabilidades de apresentar os laboratórios, Catarina?"

    ct "Ah, aqui está ela, essa é a Helena! Ela é bolsista de um dos professores do laboratório" 
    ct "Então, Helena, pode nos explicar o que se faz aqui?"

    helena "Hmmmmmmm" 

    helena "Ok, aceitarei essa requisição." 

    helena "O LabP2D é um laboratório de processamento paralelo e distribuído, que além de fazer pesquisa administra uma nuvem."

    helena "Uma das principais coisas que se faz aqui é gerenciar a nuvem do laboratório, estão hospedados diversos projetos da Universidade"

    "Helena aponta para os computadores no fundo da sala"

    helena "Aqueles são os servidores, esses servidores são computadores potentes que são utilizados por alguns projetos da universidade"

    helena "Projetos de Pesquisa as vezes precisam dessas máquinas para realizar cálculos avançados"

    eu "Que Legal, e de que projeto você faz parte Helena?"

    helena "."

    helena ".."

    helena "..."

    eu "Hã? Tá tudo bem?"

    helena "..."

    helena "...eu só faço o site"

    eu "Oh"

    "Helena parece muito decepcionada a respeito, talvez não seja uma boa ideia fazer mais perguntas"

    ct "O-ok, nós deixaremos você trabalhando Helena, vamos conhecer outro local, certo?"

    eu "Ah, ok, até mais Helena!"

    jump terreo

label function:
    scene funcao    
    "função"
    jump terreo

label colmeia:
    scene colmeia
    "colmeia"
    jump terreo


#salas no primeiro
label secretaria:
    "secretaria"
    jump andar1

label sala_prof:
    "sala prof"
    jump andar1

#salas no segundo
label auditorio:
    "auditório"
    jump andar2

label suporte:
    scene suporte fora
    show catarina felicidade at left
    ct "Ah! O Suporte é ui neste lugar é muito útil para o Departamento, podemos falar com alguém aqui dentro"

    "Vocês entram no suporte e se deparam com uma sala de recepção com uma campainha"

    eu "Hmmm, acho que devemos apertar a campainha para sermo atendidos"

    "Você aperta a campainha"

    "(Som genérico de campainha toca)"

    scene suporte dentro

    "Você e Catarina entram no suporte e são recebidos e são imediatamente abordados por uma pessoa"

    show supochan angry 

    supochan "QUEM SÃO VOCÊS?! EU NÃO VOU CONSERTAR SEU PC"
    
    show catarina felicidade at left

    show supochan angry at right

    show catarina angry 

    ct "O q-que? Nós não estamos aqui para consertar um PC!"

    show supochan angry at right

    supochan "..."

    ct "..."

    eu "..."

    supochan "...Impossível"

    ct "Claro que é possível, só queremos conhecer o Suporte"

    show supochan flushed

    supochan "tem certeza?"

    eu "Sim! Eu sou novo na universidade e gostaria de conhecer o espaço!"

    show supochan angry

    supochan "Hmpf, pessoas não autorizadas não podem entrar no suporte!"

    show catarina surprised

    ct "Ah!"

    ct "eu não sabia, peço desculpas, eu achava que podia apresentar o suporte..."

    eu "Ah, sem problema, eu queria ver mas se é a regra então não podemos"

    ct "Então, vamos conhecer outro laboratório ent-"

    show supochan flushed

    supochan "...Pera"

    "A pessoa com quem estamos falando para estar pensando em alguma solução."

    supochan "...E-eu não posso apresentar o suporte, mas posso falar um pouco do que fazemos aqui..."

    eu "Você pode? Muito obrigado!"

    show catarina happy ideia at left

    show supochan proud

    supochan "Hmpf, eu sou a Jasmine, e trabalho aqui no suporte, podem perguntar o que quiser!"

    "Ela uma atitude estranha, mas parece ser uma boa pessoa "

    eu "Olá Jasmine, eu gostaria de saber o que vocês fazem aqui!"

    jas "Aqui no suporte respondemos a chamados que podem ser abertos no HELPDESK no site do cct"

    jas "Se um computador, monitor, teclado ou qualquer equipamento de informática não estiver funcionando corretamente nas salas de aula, vocês podem acionar o suporte"

    jas "Lembrando que o suporte só mexe com equipamentos da Udesc, não fazemos serviços particulares!"

    show supochan flushed

    jas "M-Mas se você pedir com jeito e-eu formato seu pc"

    eu "Ok..."

    "Isso está começando a fica estranho, talvez seja uma boa hora de ir embora"

    ct "Obrigado pela atenção Jasmine, foi muito bom te conhecer!"

    eu "Obrigado, sei que podemos contar com você quando precisarmos!"

    jas "Hehe, podem contar comigo"

    "Assim saímos da recepção do suporte"

    jump andar2

#biblioteca e RU
label biblioteca:
    "Biblioteca"
    scene biblioteca
    bia "Olá! Bem-vindo à biblioteca universitária. O que você está achando do lugar?"
    #show bia at left
    show catarina happy ideia at right
    ct "È realmente impressionante! O ambiente é muito propício para o estudo. E essas estantes cheias de livros e artigos, são incríveis!"

    bia "Com certeza! E a melhor parte é que você pode levar esses livros para casa. A biblioteca oferece um sistema de empréstimo, então você pode levar os livros que precisar para continuar estudando fora daqui."

    eu "Isso é perfeito! Vou poder aproveitar os livros por mais tempo. E esses computadores, posso utilizá-los também?"

    bia "Sim, os computadores são disponibilizados para uso dos alunos da UDESC. Eles estão equipados com softwares específicos (as vezes) e acesso à internet para facilitar suas pesquisas e estudos."

    eu "Ótimo! Agora sei onde posso fazer minhas pesquisas. E se eu precisar de uma pausa, tem algum lugar para descansar?"

    bia "Claro! A biblioteca também oferece áreas de descanso e relaxamento. Há espaços com puffs, onde você pode deitar, ler um livro ou até mesmo dormir um pouco antes de retomar seus estudos."

    ct "Descansar um pouco entre as sessões de estudo é fundamental. E além dos livros físicos, eles também têm acervo digital"

    bia "Sim, a biblioteca conta com um acervo digital bastante abrangente. Eles têm parcerias com editoras e instituições, disponibilizando acesso a livros eletrônicos, revistas e periódicos científicos online."
    
    bia "É uma ótima opção para pesquisas rápidas ou quando você preferir consultar os materiais no formato digital."
    
    bia "Mas atente que para acessar remotamente é preciso usar uma VPN!"

    eu "Isso é realmente quase prático! Ter acesso aos recursos digitais facilita bastante o processo de pesquisa. Estou adorando todas essas facilidades que a biblioteca oferece."

    bia "Fico feliz em saber que você está gostando. A biblioteca universitária está aqui para apoiar seus estudos da melhor forma possível."
   
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
    ct "Este o restaurante universitário" 
    ct "Ou RU para os mais íntimos"

    eu "Decidi dar uma chance e ver como é. E você, já costuma vir aqui?"

    ct "Às vezes, quando estou com pouco tempo entre as aulas ou quando o dinheiro está curto. É uma opção conveniente para matar a fome rapidamente."

    eu "Entendi. E como é a comida por aqui?"

    ct "Bem, vamos dizer que não é a melhor culinária que já provei, mas pelo menos enche a barriga."

    eu "(Uhh. Pelo menos sei o que esperar)."   
    
    eu "E quanto aos preços, são realmente mais em conta que no shopping?"

    ct "Sim, os preços são bem mais baratos em comparação aos restaurantes próximos. É uma opção econômica para os estudantes, especialmente quando o dinheiro está apertado."

    eu "Já é algo então."

    ct "Com certeza. Às vezes, é mais uma questão de conveniência do que de qualidade da comida. Afinal, estamos aqui para estudar, não é mesmo?"

    eu "Suponho que sim..."

    "Você decide deixar suas aventuras gastronômicas para outra hora"
    menu:
        "Para onde devo ir?"
        "bibilioteca":
            jump biblioteca
        "terreo":
            jump terreo

#definição de personagens
define s = Character('Sylvie', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")
define ct = Character('Catarina', color="#34eb3a")
define eu = Character('Eu',color="#000000")
define hl = Character('Helena',color="#008cff")
define bia = Character('Beatriz',color="#ff9100")
define supochan = Character('Funcionaria do suporte',color="#ff0000")
define jas = Character('Jasmine',color="#ff0000")
define funfox = Character('Membro do função',color="#ff00ea")
define afonso = Character('Afonso',color="#ff00ea")
define albelha = Character('Alberto',color="#fff200")

##########################################################################################
#Define Images
#personagens

#catarina
image catarina happy ideia:
    "catarina happy ideia.png"
    zoom 0.3

image catarina angry:
    "catarina serious standing.png"
    zoom 0.3    

image catarina felicidade:
    "catarina happy explaining.png"
    zoom 0.3  

#suporte
image supochan angry:
    "supochan angry.png"
    zoom 0.3
    
image supochan angry pointing:
    "supochan angry pointing.png"
    zoom 0.3
    
image supochan flushed:
    "supochan flushed.png"
    zoom 0.3

image supochan proud:
    "supochan proud.png"
    zoom 0.3

#função
image funfox explaining:
    "fox_explain.png"
    zoom 0.3

image funfox thinking:
    "fox_think.png"
    zoom 0.3

#colmeia
image albelha happy:
    "abelha_happy.png"
    zoom 0.3

image albelha thinking:
    "abelha_think.png"
    zoom 0.3

#labP2D
image helena normal:
    "pd2chan serious.png"
    zoom 0.36

image helena vibes:
    "helena_vibes.png"
    zoom 0.36

##########################################################################################
#Backgrounds

image bg entrada:
    "bg entrada.png"
    zoom 2.6    

image bg terreo:
    "bg terreo.png"

image placaF:
    "placaF.png"

image segundo_andar:
    "segundo andar.png"

image colmeia:
    "colmeia.png"

image labp2d_bg:
    "labP2D.png"

image funcao:
    "funcao.png"

image bg andar1:
    "bg andar1.png"

image biblioteca:
    "biblioteca.jpg"
    zoom 2.2

image restaurante:
    "bg_ru.jpeg"
    zoom 0.7

image suporte dentro:
    "suporte_dentro.png"

image suporte fora:
    "suporte_fora.png"

image auditorio:
    "auditorio.png"

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
default anylab = 0

##########################################################################################
#VN STARTS HERE
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

    menu:
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

    if terreo == 0:
        show catarina happy ideia
        
        ct "Este é o Térreo do Bloco F"

        ct "No terreo, além das salas de aula e do ambiente de estudo, temos a maioria dos laboratórios de pesquisa e extensão"

        eu "Que tipo de laboratórios há aqui?"

        ct "Existem laboratório de Imagem, de software livre, de lógica... Nossa, existem tantos que não consigo lembrar agora!, vamos ter que explorar um por um"
        
        eu "Quero visitar um!"
        $ terreo = 1
        
    menu: 
        
        "Para onde devo ir?"

        "teste":
            $ terreo = 0
            jump terreo

        "Laboratório Função":
            $ anylab = 1
            jump function
        
        "Laboratório Colmeia":
            $ anylab = 1
            jump colmeia

        "Laboratório P2D":
            $ anylab = 1
            jump labp2d

        "Primeiro Andar":
            jump andar1
        
        "biblioteca":
            jump biblioteca
            
        "RU":
            jump ru
        
        "Como lab" if anylab == 1:
            eu "Como eu faço para me juntar a um laboratório?"

            ct "Os laboratórios abrem processos seletivos periodicamente, mas é interessante buscar serviços voluntários"

            ct "Falar com os professores responsáveis de cada laboratório também é uma boa ideia"

            ct "Você ainda pode achar várias informações nas redes sociais"

            eu "Vou começar a seguir vários laboratórios!"
            
            jump terreo
    

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
    
    show catarina felicidade at right

    ct "Esse é o LabP2D, eu conheço uma pessoa que trabalha aqui que pode apresentar apresentar esse lugar."
    
    show helena normal at left

    hl "Hmpf, você por acaso está DISTRIBUINDO as responsabilidades de apresentar os laboratórios, Catarina?"

    ct "Ah, aqui está ela, essa é a Helena! Ela é bolsista de um dos professores do laboratório" 

    ct "Então, Helena, pode nos explicar o que se faz aqui?"

    hl "Hmmmmmmm" 

    hl "Ok, aceitarei essa requisição." 

    hl "O LabP2D é um laboratório de processamento paralelo e distribuído, que além de fazer pesquisa administra uma nuvem."

    hl "Uma das principais coisas que se faz aqui é gerenciar a nuvem do laboratório, estão hospedados diversos projetos da Universidade"

    "Helena aponta para os computadores no fundo da sala"

    hl "Aqueles são os servidores, esses servidores são computadores potentes que são utilizados por alguns projetos da universidade"

    hl "Projetos de Pesquisa as vezes precisam dessas máquinas para realizar cálculos avançados"

    eu "Que Legal, e de que projeto você faz parte Helena?"

    show helena vibes

    hl "."

    hl ".."

    hl "..."

    eu "Hã? Tá tudo bem?"

    hl "..."

    hl "...eu só faço o site"

    eu "Oh"

    "Helena parece muito decepcionada a respeito, talvez não seja uma boa ideia fazer mais perguntas"

    ct "O-ok, nós deixaremos você trabalhando Helena, vamos conhecer outro local, certo?"

    eu "Ah, ok, até mais Helena!"

    jump terreo

label function:
    scene funcao    
    
    show catarina felicidade at right

    ct "Ah! Esse laboratório é o função! O pessoal deste laboratório atua na parte de lógica!"

    ct "Admito que não sei muito a respeito, então vai ser interessante para mim também saber o que fazem aqui."

    "Chegamos no Função e batemos na porta"

    "Nos somos recebidos por um membro do laboratório."

    show funfox explaining at left

    funfox "Hm? Oh, Catarina, seja bem vinda! E quem seria esse?"

    ct "Este aqui é um aluno novo da Computação, deseje boas vindas para ele"

    funfox "Olá, Meu nome é Afonso, e faço parte do Função, deseja conhecer o laboratório?"

    eu "Sim, o que vocês fazem no laboratório?"

    afonso "..."

    ct "?"

    afonso "...isso...pode um pouco difícil de explicar..."

    eu "P-Perdão, eu fiz uma pergunta que não devia?"

    afonso "Não, não há nada errado na sua pergunta, só preciso de um tempo para organizar essa resposta..."

    show funfox thinking

    afonso "..."

    "Afonso parece estar pensando muito a respeito de como apresentar o laboratório"

    afonso "O função é... um laboratório que estuda fundamentos matemáticos da computação..."

    afonso "...de forma geral, isso seria lógica, Teoria de Tipos e Teoria da Computação."

    show funfox explaining

    afonso "Mas também temos projetos que abrangem linguagens formais e teoria de linguagens de programação"

    afonso "No decorrer do curso, você irá fazer várias matérias que se aprofundam em áreas que o laboratório estuda."

    afonso "Matérias como Teoria da Computação e Compiladores, por exemplo."

    afonso "Agora no primeiro semestre, você terá Lógica Matemática, que introduzirá os conceitos que usamos aqui"

    eu "Eu não sei se entendo muito bem..."

    afonso "Não tem problema, você entenderá..."

    afonso "..."

    afonso "..queira você ou não."

    show catarina angry

    ct "EI! Nada de assustar os calouros!"

    show funfox explaining

    afonso "Perdão."

    afonso "Teriam mais alguma pergunta?"

    eu "Hmmmm, eu entendi que nós veremos muitos desses conceitos no curso"

    eu "Mas me parece que a lógica que vocês fazem com lógica aqui é um pouco diferente do que estou acostumado"

    eu "Vocês aplicam lógica em computação, como funciona isso?"

    afonso "Bem, essencialmente tem duas coisas que nós vemos em lógica:"

    afonso "Primeiro, como usar lógica para representar formalmente programas"

    afonso "Com isso, podemos provar propriedades sobre estes mesmos programas"

    afonso "Outra área de estudo é o que são sistemas lógicas e como podemos racíocinar {b}sobre lógicas{/b}, não apenas {b}com{/b} essas lógicas"

    afonso "Teria mais outra pergunta?"

    eu "Hmmmm, bem, quem é que está dormindo ali no canto?"

    afonso "Outra pergunta por favor"

    eu "errrr...quer saber? Talvez acho que é tudo por agora, vamos visitar outro laboratório, Catarina?"

    ct "Ah! Sim claro, vamos"

    "Assim você e Catarina saem do Função"
    jump terreo

label colmeia:
    scene colmeia
    
    show catarina felicidade at right

    ct "Ah, O Colmeia, conheço alguém que pode nós explicar tudo sobre o laboratório"

    "Você e Catarina batem na porta do laboratório e são atendidos por alguém"

    show albelha happy at left

    albelha "Hmmm, olá Catarina, quem está junto com você?"

    ct "Olá Alberto, ese é um novo aluno do campus, ele gostaria de conhecer os laboratórios!"

    albelha "Oh, posso apresentar o Colmeia para vocês."

    albelha "Nós somos um laboratório de extensão, com principal objetivo de disseminar o conhecimento e uso de software e hardware livres"

    eu "Software Livre? O que seria isso?"

    albelha "Software Livre é o software que permite ao usuário executar, acessar e modificar códigos fontes e redistribuir cópias do programa"

    albelha "Sofwares Livres permitem que softwares estejam ao alcance da comunidade de programadores, o que torna o conhecimento e as ferramentas mais acessíveis"

    eu "Que Legal, e como vocês disseminam o conhecimento de software e hardware livre?"

    albelha "Nos divulgamos por aulas e minicursos, visitando escolas e outras universidades"

    albelha "Também organizamos caravanas para eventos ligados ao Software Livre, e até mesmo programas para a rádio Udesc!"

    albelha "Os cursos preparados pelo Colmeia abragem diversos temas, como Desenvolvimento em Arduino, de Aplicativos com MIT App Inventor"

    ct "Alberto, onde ele pode encontrar esses materiais?"

    albelha "Todo o nosso material aberto pode ser encontrado na nossa página do Github, dá uma olhada lá"

    eu "ok, só mais uma pergunta..."

    albelha "O que foi?"

    eu "Posso segurar o pinguim?"

    show albelha thinking

    albelha "Só por uns momentos..."

    eu "hehe"

    "Você segura o pinguim, ele é tão macio quanto você esperava"

    albelha "d-devolve"

    "Você percebe que passou do limite e devolve o pinguim"

    eu "Então é isso, obrigado pelas explicações"

    ct "Obrigado Alberto"

    albelha "Claro, até mais!"

    "Você e Catarina saem do Colmeia"

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
    scene auditorio
    show catarina happy ideia at right
    ct "Acabamos de chegar no auditório do bloco de Computação."

    eu "Nosso bloco tem um auditório? Parece um espaço interessante. O que costuma acontecer aqui?"

    ct "Esse auditório é o local onde ocorrem os colóquios, reuniões e palestras do departamento de Computação. É um espaço muito utilizado para compartilhar conhecimentos e promover discussões acadêmicas."

    eu "Entendi. É um ambiente importante para trocar ideias e aprender mais sobre a área de Computação."

    ct "Com certeza! Os colóquios são eventos regulares em que pesquisadores e professores convidados apresentam suas pesquisas e avanços em diferentes áreas da Computação. São oportunidades valiosas para nos mantermos atualizados e ampliar nosso conhecimento."

    eu "Isso é ótimo! Gosto da ideia de ter acesso a palestras e apresentações de especialistas na nossa área."

    ct "Além disso, o auditório também é utilizado para reuniões de departamento, onde são discutidas questões administrativas e organizacionais do bloco de Computação. É um espaço importante para tomadas de decisão e planejamento de projetos."

    eu "Entendi. É bom saber que temos um lugar apropriado para essas atividades, onde podemos nos envolver nas discussões e contribuir para o desenvolvimento do bloco."

    ct "Com certeza. E ocasionalmente, o auditório também é usado para sessões de cinema, onde podemos assistir a filmes relacionados à tecnologia e ciência, proporcionando momentos de descontração e entretenimento."

    eu "Ah, legal! Uma pausa para relaxar e assistir a um bom filme também é importante. É bom saber que o auditório oferece essa diversidade de atividades."

    ct "Sim, é uma forma de unir o aprendizado com momentos de lazer. Fique de olho nas programações para não perder nenhuma sessão de cinema ou outro evento interessante que possa ocorrer aqui."

    eu "Certamente! Vou ficar atento às divulgações e aproveitar ao máximo todas as oportunidades que o auditório do bloco de Computação oferece, seja para participar de colóquios, palestras, reuniões ou até mesmo relaxar assistindo a um filme."

    ct "Excelente! Vamos aproveitar ao máximo todas essas oportunidades e enriquecer nossa experiência acadêmica aqui no auditório do bloco de Computação."
    jump andar2

label suporte:
    scene suporte fora
    show catarina felicidade at left
    ct "Ah! O Suporte é ui neste lugar é muito útil para o Departamento, podemos falar com alguém aqui dentro"

    "Vocês entram no suporte e se deparam com uma sala de recepção com uma campainha"

    eu "Hmmm, acho que devemos apertar a campainha para sermo atendidos"

    "Você aperta a campainha"



    play audio "doorbell-7.mp3"
    
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
        "Bibilioteca":
            jump biblioteca
        "Terreo":
            jump terreo
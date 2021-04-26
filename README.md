<h1>Locus x - Backend</h1>
<h2>Desenvolvimento de uma ferramenta de autoria
para a produção de material didático visando a
aprendizagem com base no contexto de localização
do aluno</h2>
<h3>Contexto e Motivação</h3>
Aulas de campo podem oferecer diversos benefícios para o processo de aprendizagem
do aluno, permitindo ampliar suas habilidades de observação, descoberta e assimilação da realidade com o objeto de aprendizagem estudado em seu ambiente natural,
além de fortalecer a interação professor-aluno [16]. Esse tipo de aula pode alavancar a aprendizagem em diversas áreas de estudos, por exemplo em assuntos como
ecologia e meio ambiente.
No entanto, durante atividades de campo, obstáculos podem surgir e dificultar
a dinâmica, por envolver uma série de tarefas a serem executadas em diferentes
meios. Até recentemente, o aluno tinha que carregar apostilas, câmeras fotográficas,
gravador de áudio, bússola, etc., o que dificultava a mobilidade do aluno e também
o acompanhamento individual dos alunos por parte do professor [18, 20].
Com a popularização de dispositivos móveis com maior capacidade de processamento, como já relatado por Hwang [9], incentivou-se a utilização e o desenvolvimento de ambientes ubíquos para a educação, permitido que os professores criassem
situações de aprendizado fora da sala de aula. Por exemplo, pode-se propor atividades em que os alunos interajam com o ambiente por meio de seus smartphones,
empregando ferramentas de geolocalização, como apresentado por Lopes et al [11].
Isso traz diversas vantagens ao processo de aprendizado dos alunos, permitindo que
apliquem o conhecimento em situações reais. Além disso, o material das aulas, câmera e GPS ficam todos num único dispositivo, facilitando transporte e mobilidade
do aluno.
A Computação Ubíqua permite informação e suporte computacional ao usuário
em qualquer espaço e tempo, de maneira invisível [4]. Assim, a computação e seus
diversos sistemas podem interagir com o ser humano a todo o momento não importando onde ele esteja, constituindo um ambiente altamente distribuído, heterogêneo,
dinâmico, móvel e interativo [22]. As principais características dos sistemas ubíquos
são: redes móveis, acesso móvel a informação, sensibilidade à localização, segurança
distribuída, sensibilidade ao contexto, escalabilidade localizada, capacidade de mascarar a má condição e invisibilidade [14].
A Internet das Coisas (Internet of Things - IoT) é um outro conceito que está
bastante relacionado aos sistemas ubíquos. O termo IoT foi cunhado originalmente
em 1999 por Kevin Ashton [2], ao descrever um sistema no qual dispositivos eletrônicos com conectividade entre si são anexados aos objetos do mundo físico, utilizando
sensores para captar informações deste mundo. Estes dispositivos do mundo físico se
integram em um ambiente conectado no qual são capazes de serem identificados, possuem conectividade, externam seus estados e, eventualmente, possuem capacidade
de processamento de tal modo a influenciar outros objetos, tanto virtuais quanto
físicos[1, 3]. A crescente demanda por este tipo de dispositivo tem despertado o interesse da indústria e das instituições acadêmicas em prover tecnologias compatíveis
com o conceito IoT [21].U-learning consiste na aplicação do paradigma e tecnologias da computação ubíqua para auxiliar o processo de ensino-aprendizagem, levando em consideração características da computação móvel, que disponibiliza acesso a qualquer hora e em
qualquer local, integrado com tecnologias de redes sem fio, sensores IoT e mecanismos de localização, para identificar e coletar informações sobre o contexto do aluno
e promover aprendizagem e conteúdos educacionais adaptados às características e
necessidades individuais do aluno [19, 12].
Um outro conceito importante nesse panorama é o de sensibilidade ao contexto,
que se refere à capacidade do software se adaptar à situação em que o usuário
se encontra. Essa capacidade traz ao usuário um estilo de interação que facilita
bastante a comunicação do homem com a máquina, já que o programa pode se
adaptar à sua necessidade [17]. De acordo com Dey [6], contexto é definido como
"qualquer informação que pode ser utilizada para caracterizar a situação de uma
entidade (pessoa, lugar ou objeto), informação essa considerada relevante para a
interação entre o usuário e a aplicação". que pode ser utilizada para caracterizar a
situação de entidades
Portanto, a união dos conceitos citados acima caracterizam os dispositivos móveis
como ferramentas essenciais para proporcionar aulas de campo em que o contexto
do aluno seja levado em consideração. Pode-se pensar em aplicações de software em
que o professor programe atividades sensíveis ao contexto a serem realizadas pelo
aluno quando se encontrar em uma determinada coordenada geográfica, permitindo
que o aluno associe a teoria vista em sala de aula com a prática em campo. Um
exemplo seria uma visita a patrimônios públicos, parques e outro locais de grande
importância histórica ou cultural, relacionando assuntos e eventos passados em aula
com estruturas do mundo real.
Esse tipo de aplicação de software para aprendizagem ubíqua pode fazer uso
de um conceito de engenharia de software chamado Arquitetura Orientada a Serviços (SOA – Service-Oriented Architecture). Por intermédio de Web Services, a
comunicação entre dispositivos e sistemas existentes é facilitada, permitindo sua interoperabilidade. É também permitida a utilização de funcionalidades distribuídas
que podem estar sob o domínio de proprietários distintos [13].
Entretanto, a programação de aulas para dispositivos móveis ainda carece de
ferramentas fáceis de utilizar pelos professores, que em geral tem conhecimentos
limitados na área de computação. Os ambientes tradicionais de educação na Web
tendem a exigir mais do professor no que diz respeito ao desenvolvimento de OAs
mais complexos, pois precisam prever diferentes situações de aprendizagem e buscar
meios mais adequados para apresentação do conteúdo instrucional [10]. Por isso,
ferramentas de auxílio à autoria se fazem cada vez mais necessárias, de forma a
facilitar o desenvolvimento do conteúdo [15].
Nesse sentido, em um trabalho de doutorado em andamento, foi proposta uma
arquitetura baseada em SOA [10], denominada MOA-RA, cujo objetivo é facilitar
o desenvolvimento de ferramentas de autoria voltadas ao professor que precisa criar objetos de aprendizagem (OA). A MOA-RA permite que isso seja feito de maneira
flexível, dinâmica e adaptada às necessidades do aluno, ao mesmo tempo de maneira
fácil para o professor, que deve priorizar a elaboração de conteúdo para seus alunos.
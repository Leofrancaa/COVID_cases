import os
from fpdf import FPDF


pdf = FPDF("P", "mm", "A4")
pdf.add_page()


def texto():
    pdf.set_text_color(0,0,0)
    pdf.set_font('Arial','',12)

def negrito():
    pdf.set_font('Arial','B',12)
def sublinhado():
    pdf.set_font('Arial','U',12)
def italico():
    pdf.set_font('Arial','I',12)

def titulo(titulo):
    pdf.ln()
    pdf.set_font('Arial','B',16)
    pdf.cell(190,5,txt=titulo, align='C')
    pdf.ln(10)
def subtitulo(subtitulo):
    pdf.ln()
    pdf.set_font('Arial','B',14)
    pdf.cell(190,5,txt=subtitulo, align='C')
    pdf.ln()
def p(paragrafo):
    texto()
    pdf.multi_cell(190,5,txt=paragrafo)
    pdf.ln(h=3)
def descricao(descricao):
    pdf.set_font('Arial','',10)
    pdf.multi_cell(190,5,txt=descricao)
    pdf.ln(h=3)
    

texto()
pdf.multi_cell(w=0,h=5, txt='Leonardo Franca Almeida Silva\nSalvador - BA\n2022\n', align='J')

pdf.line(5, 25, 205, 25)
titulo('As sequelas da pandemia ')

p('     Há muito tempo que o mundo não enfrentava uma pandemia igual a que estamos vivenciando. Isso nos mostra a gravidade  desse problema, e que por isso devemos continuar lutando contra esse vírus com tudo que temos, e torcer para que todo nosso esforço ajude a diminuir as sequelas que essa pandemia nos causou. Segundo o site "seade.gov.br" o número de casos registrados da covid chegou a mais de 360 milhões pelo mundo todo.')

pdf.image(name="tabela1.png", w=170, y=65, x=15)
pdf.ln(65)

p('     A grande quantidade de fatalidades que a Covid causou durante esses dois anos foi o maior problema gerado por ela, entretanto há outros problemas que prejudicam as pessoas que tiveram a doença e foram curados. Essas sequelas que permanecem complicam a vida mesmo muuito tempo depois. Existem relatos de pessoas que até hoje não recuperaram completamente seu olfato e seu paladar, além disso existem muitos  outros problemas relatados já que esse vírus se trasnmite muito fácil e contamina muita gente. De acordo com pesquisas, aproximadente 10% do estado de são Paulo foi contaminado pela Covid. Isso demonstra que existem espalhados pelo mundo todo pessoas que ainda sofrem com essa doença mesmo não tendo mais ela.')

subtitulo('Sequelas psicológicas')

pdf.cell(80, 5, '', 0, 1)

p('     Segundo o site "CNN Brasil", ansiedade e depressão estão entre sequelas psicológicas da Covid-19. Os sintomas neurológicos e psiquiátricos mais comuns foram perda de olfato, fraqueza, fadiga, perda do paladar, dor muscular, depressão, dor de cabeça e ansiedade. Estudos também apontam que, apesar de mais raro, doenças neurológicas mais graves, como AVC e convulsões podem afetar esses pacientes.')

p('     O neurocirurgião Fernando Gomes, em entrevista a CNN Brasil, confirmou que, em seu consultório, tem recebido diversos pacientes com esses sintomas que compõe a chamada síndrome pós-Covid. "O cornavírus atinge as pessoas de duas formas. Uma delas é através da própria infecção orgânica. O vírus rem a capacidade de entrar no sistema nervoso central e provocar até mesmo AVC e tromboses em pequenas veias do cérebro", afirmou o médico.')
pdf.ln(h=3)

p('     "A doença também afeta a saúde mental. Estamos vivendo em tempo de pandemia, é natural que todo mundo fique preocupado e essa ansiedade aumenta ainda mais quando a pessoa ou alguém próximo a ela pega o coronavírus. Medo de morte, de sofrimento, de não conseguir lidar com a situação, restrição ainda maior em relação ao distanciamento social, provocando algumas alterações psicológicas", concluiu Gomes.')

p('     Outros estudos sobre o mesmo tema também trazem dados preocupantes.')

p('     Um deles, publicado pela universidade de Oxford na plataforma científica medRxiv em meados de agosto  de 2020, mostrou que pacientes com quadros graves de Covid-19 poderiam desenvolver doenças psicológicas, como ansiedade e depressão, mesmo sem histórico psiquiátrico. Os pesquisadores avaliaram, entre janeiro e agosto de 2020, mais de 62 mil casos de Covid-19 através de registros eletrônicos de saúde, e constataram que as doenças podem ser observadas em até três meses depois da infecção. foi registrado o aumento nos diagnósticos principalmente de transtornos de ansiedade, como também de depressão, insônia, demência e esttresse pós-traumático.')

p('     Um relatório publicado pela OMS, aponta o Brasil como o país com a maior prevalência de transtornos de ansiedade no mundo: até 2017 o problema afetava mais de 18 milhões de pessoas, aproximadamente 9,3% da população.')

pdf.image(name="img-2.jpg", w=140, y=80, x=35)
pdf.ln(85)

p('     Este problema muito preocupante, infelizmente, foi agravado pela pandemia. Passamos quase 2 anos tendo centenas de notícias ruins e tivemos que ficar isolados dentro de casa, perdendo o contato com pessoas que poderiam nos ajudar, ficou muito complicado de criar estratégias alternativas para lidar com isso.')

negrito()
pdf.multi_cell(190,5,txt='Gráficos que representam o número de casos em alguns municípios de São Paulo.', align='C')
pdf.ln(h=3)

pdf.image(name="Casos-da-Covid-por-municipio.png", w=200, y=200, x=8)
pdf.ln(95)

negrito()
pdf.multi_cell(190,5,txt='Gráficos que representam o número de óbitos em alguns municípios de São Paulo.', align='C')
pdf.ln(h=3)

pdf.image(name="Grafico-Obitos-da-Covid-por-municipio.png", w=200, y=20, x=7)
pdf.ln(80)

p('     Esses números de casos e óbitos são muito alarmantes, pois nos dá uma noção de quantas pessoas sofreram e sofrem por conta da pandemia. O sofrimento de cada um que teve contato com esse vírus, mudou a vida da pessoa de alguma forma, ou a deixando mais forte ou até piorando algo que ela já tinha, isso mostra o porque do aumento de casos de doenças como depressão durante esses dois últimos anos.')

p('     Segundo o site "O DIA", um estudo feito pela Universidade do Estado do Rio de Janeiro, com 1460 pessoas em 23 estados diferentes, nos meses de março e abril de 2021, revelou um aumento de 90% nos casos de depressão, 40% em relação ao estresse agudo e 71% em crises durante a pandemia do novo coronavírus. Isso deveria ser mais noticiado pela mídia, para que com a ajuda de profissionais, pessoas que estiverem passando por esse tipo de problema possa ser ajduado o mais rápido possível.')

p('     O grande dilema que os profissionais de sáude tiveram que solucionar foi o fato de eles também terem sido afetados pela pandemia, por tanto verem pessoas todos os dias morrendo sem poderem fazer nada para salvar a vida delas e ainda tendo que saber que  muitos problemas poderiam ter sido resolvidos se não fosse pela incompetencia e indiligência dos governadores do nosso país ')

pdf.image(name="desvio.png", w=200, y=200, x=7)
pdf.ln(100)

p('     O próprio site do governo e diversos outros sites confiáveis, publicaram matérias sobre o descaso de governadores dos estados de Alagoas, Rio de Janeiro, São Paulo e Ceará, ao cometer um crime tão grave num momento em que tinham pessoas sofrendo nos hospitais precisando de respiradores. A quantidade de pessoas que morreu por conta do egóismo de políticos que quase nunca fazem nada pelo povo, causa sequelas ainda mais fortes nas pessoas que sofreram por causa disso. ')
pdf.ln(65)

pdf.add_page()
pdf.ln(150)

pdf.set_font('Arial','B',16)
pdf.multi_cell(190, 5, txt='As sequelas psicológicas que a pandemia causou não podem passar despercebidas, pois se não lidarmos com elas, haverão mais e mais fatalidades.', align='C')
pdf.add_page()

titulo('REFERÊNCIAS')
pdf.line(5, 25, 205, 25)
pdf.ln(10)

pdf.set_text_color(93,216,240)
sublinhado()

pdf.multi_cell(190,5,txt='CNN Brasil - Pesquisa observa sequelas psicológicas três meses após contaminação por Covid-19.', link='https://www.cnnbrasil.com.br/saude/pesquisa-observa-sequelas-psicologicas-tres-meses-apos-contaminacao-por-covid-19/')
pdf.ln(h=3)

pdf.multi_cell(190,5,txt='Seade.gov.br - SP CONTRA O NOVO CORONAVÍRUS.', link='http://www.seade.gov.br/coronavirus/')
pdf.ln(h=3)

pdf.multi_cell(190,5,txt='O DIA - Estudo revela aumento de 90% nos casos de depressão na pandemia', link='https://odia.ig.com.br/vida-saudavel/saude/2020/06/5933117-estudo-revela-aumento-de-90--nos-casos-de-depressao-na-pandemia--terapias-complementares-podem-ser-a-solucao.html')
pdf.ln(h=3)

pdf.multi_cell(190,5,txt='Governo federal - PF investiga desvios de recursos destinados ao enfrentamento do novo coronavírus', link='https://www.gov.br/pt-br/noticias/justica-e-seguranca/2020/05/pf-invstiga-desvios-de-recursos-destinados-ao-enfrentamento-do-novo-coronavirus')
pdf.ln(h=3)

pdf.output("Relatório.pdf")

print("O PDF foi criado com sucesso!")
os.system("pause")
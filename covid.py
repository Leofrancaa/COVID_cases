import os
import pandas as pd

from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()

pdf.set_font('times', 'B', 18)
pdf.cell(180, 20, 'Sequelas da Covid', 0, 1, align='C')

pdf.set_font('times', '', 14)
pdf.multi_cell(200, 8, 'Desde o ano de 2009 que o mundo não enfrentava uma pandemia igual a que estamos vivenciando. Isso nos mostra a gravidade  desse problema, e que por isso devemos continuar lutando contra esse vírus com tudo que temos, e torcer para que todo nosso esforço ajude a diminuir as sequelas que essa pandemia nos causou. Segundo o site "seade.gov.br" o número de casos registrados da covid chegou a mais de 360 milhões pelo mundo todo', 0, 1)

pdf.image(name="tabela1.png", x=40, y=70, w=135)

#espaçamento
pdf.cell(80, 50, '', 0, 1)

pdf.multi_cell(200, 8, 'A grande quantidade de fatalidades que a Covid causou durante esses dois anos foi o maior problema gerado por ela, entretanto há outros problemas que prejudicam as pessoas que tiveram a doença e foram curados. Essas sequelas que permanecem complicam a vida mesmo muuito tempo depois, existem relatos de pessoas que até hoje n recuperaram completamente seu olfato e seu paladar, entre tantos outros problemas relatados já que esse vírus se trasnmite muito fácil e contamina muita gente. De acordo com pesquisas, aproximadente 10% do estado de são Paulo foi contaminado pela Covid. Isso demonstra que existem espalhados pelo mundo todo pessoas que ainda sofrem com essa doença mesmo não tendo mais ela.', 0, 1)

pdf.image(name="tabela2.png", x=40, y=190, w=155)

pdf.cell(80, 60, '', 0, 1)

pdf.multi_cell(200, 8, 'As sequelas físicas e psicológicas que a Covid causa, é algo que vamos ter que lidar por muito tempo, mas felizmente estamos cada dia mais perto do fim de todo esse sofrimento.', 0, 1)

#espaçamento
pdf.cell(80, 7, '', 0, 1)



pdf.output('Dados_da_Covid.pdf')

print("O PDF foi criado com sucesso!")

os.system("pause")
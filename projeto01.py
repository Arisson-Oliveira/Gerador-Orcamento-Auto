from fpdf import FPDF

# Solicita a descrição do projeto ao usuário
projeto = input('Digite a descrição do projeto: ')

# Solicita a quantidade de horas previstas ao usuário
horas_previstas = input('Digite a quantidade de horas previstas: ')

# Solicita o valor da hora trabalhada ao usuário
valor_hora = input('Valor da hora trabalhada: ')

# Solicita o prazo estimado ao usuário
prazo = input('Digite o prazo estimado: ')

# Calcula o valor total com base nas horas previstas e no valor da hora
valor_total = int(horas_previstas) * int(valor_hora)

# Cria uma instância do objeto FPDF
pdf = FPDF()

# Adiciona uma nova página ao PDF
pdf.add_page()

# Define a fonte para o texto do PDF
pdf.set_font('arial')

# Adiciona uma imagem ao PDF, usada como template de fundo
pdf.image('template.png', x=0, y=0)

# Adiciona os textos no PDF nas coordenadas especificadas
pdf.text(115, 145, projeto)                          # Descrição do projeto
pdf.text(115, 160, horas_previstas + ' horas')       # Horas previstas
pdf.text(115, 175, valor_hora + '/hora')             # Valor da hora
pdf.text(115, 190, prazo)                            # Prazo estimado
pdf.text(115, 205, str(valor_total) + ' Reais')      # Valor total calculado

# Gera o arquivo PDF com o nome 'Orçamento.pdf'
pdf.output('Orçamento.pdf')

# Informa ao usuário que o orçamento foi gerado com sucesso
print('Orçamento gerado com sucesso!')

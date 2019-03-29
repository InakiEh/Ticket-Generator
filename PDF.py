from fpdf import FPDF
import time
from tkinter import * 


class CustomPDF(FPDF):
 
    def header(self):
        self.image('logo.png', 90, 8, 33)
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 5, 'Correo: mauconej@gmail.com - Fono: +(569) 53480893', 0, 0, 'C')
        self.ln(2)
        self.line(20, 280, 190, 280)
        page = 'Pag ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, align='C')

def create_pdf(pdf_path):

    a = time.strftime("%d/%m/%y")
    fecha = a.split('/')

    if fecha[1] == '01':
        mes = 'Enero'
    elif fecha[1] == '02':
        mes = 'Febrero'
    elif fecha[1] == '03':
        mes = 'Marzo'
    elif fecha[1] == '04':
        mes = 'Abril'
    elif fecha[1] == '05':
        mes = 'Mayo'
    elif fecha[1] == '06':
        mes = 'Junio'
    elif fecha[1] == '07':
        mes = 'Julio'
    elif fecha[1] == '08':
        mes = 'Agosto'
    elif fecha[1] == '09':
        mes = 'Septimbre'
    elif fecha[1] == '10':
        mes = 'Octubre'
    elif fecha[1] == '11':
        mes = 'Noviembre'
    elif fecha[1] == '12':
        mes = 'Diciembre'

    pdf = CustomPDF()
    
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Arial', '', 10.0)
    line_no = 1
    pdf.cell(25)
    pdf.cell(95, 5, 'Señor/a:')
    pdf.set_font('Arial','B',10.0)
    pdf.cell(0, 5, 'Santiago, '+fecha[0]+' de '+mes+' '+'20'+fecha[2], ln=1)
    pdf.set_font('Arial', '', 10.0)
    pdf.cell(25)
    
    effective_page_width = pdf.w - 2*pdf.l_margin

    pdf.set_font('Arial','B',10.0)
    pdf.cell(95, 5, '')
    pdf.cell(0, 5, 'Nº1 / Santiago / 2019', ln=1)
    pdf.cell(25)
    pdf.cell(0, 5, 'Director Regional', ln=1)
    pdf.cell(25)
    pdf.cell(0, 5, 'Dirección de Vialidad Metropolitana', ln=1)
    pdf.cell(25)
    pdf.set_font('Arial','U',10.0)
    pdf.cell(0, 5, 'Presente', ln=1)
    pdf.ln(3)
    pdf.set_font('Arial','',7)
    pdf.cell(120, 5, '')
    pdf.multi_cell((effective_page_width/2)-40, 5, 'Ref.:Conservación Periódica Camino Santa Inés, Rol G-364, DM 0.00 a DM 6,744, Comuna de Calera de Tango, Provincia de Maipo y Conservación Periódica Ruta G-251, Farellones-Valle Nevado, Km 2.0 al Km 6.0; Comuna de Lo Barbecha')
    pdf.ln(3)
    pdf.cell(120, 5, '')
    pdf.multi_cell((effective_page_width/2)-40, 5, 'MAT.:Solicita liquidación de contratos y reintegro de excedentes de garantías')
    pdf.ln(5)

    
    pdf.set_font('Arial', '', 10)
    pdf.cell(25, 5, '')
    pdf.multi_cell(140, 5, 'De Nuestra Consideración:\n\n        Nuestra sociedad Empresa Constructora Tipaume S.A., Rut 76.049.601-4 ejecutó para su servicio las obras:\n\n1.	Conservación Periódica Camino Santa Inés, Rol G-364, DM 0.00 a DM 6,744, Comuna de Calera de Tango, Provincia de Maipo, adjudicada según Res D.R.V.M. N° 55 del 20 de Septiembre del 2012, totalmente tramitada con fecha 12 de Octubre del 2012\n\n2.	Conservación Periódica Ruta G-251, Farellones-Valle Nevado, Km 2.0 al Km 6.0; Comuna de Lo Barbecha, adjudicada según Res D.R.V.M. N° 14 del 22 de Marzo del 2012, totalmente tramitada con fecha 25 de Junio del 2012\n\nLos dos contratos antes individualizados se encuentran a la fecha con sus recepciones ejecutadas pero están pendientes de su liquidación final la cual solicitamos a Uds., tenga a bien instruir a quien corresponda para que se ejecuten a la brevedad, teniendo en consideración el plazo absolutamente excesivo que ha transcurrido.\n\nHacemos notar a Uds., que existen garantías que fueron hechas efectivas de ambos contratos para proceder a cubrir las multas existentes y que una vez aplicadas las garantías a estas multas existe un excedente a favor de la empresa que debe ser reintegrado.\n\nSin otro particular,')
    pdf.ln(15)
    pdf.cell(120, 1, '')
    pdf.multi_cell((effective_page_width/2)-40, 5, 'Mauricio Conejero G.')
    pdf.cell(120, 1, '')
    pdf.multi_cell((effective_page_width/2)-40, 5, 'pp. Constructora Tipaume S.A.')
    pdf.ln(3)
    pdf.output(pdf_path)

window = Tk()
 
#nombre = Tk.StringVar()

label1 = Label(window,text="Nombre")
label2 = Label(window,text="    ")
nombre = Entry(window)

button = Button(window,text="Guardar",command=create_pdf(nombre))

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
nombre.grid(row=0, column=2)
button.grid(row=1, column=0)
 
window.mainloop()

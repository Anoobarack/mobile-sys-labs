import lab1, lab2
from PyPDF2 import PdfFileReader, PdfFileWriter
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.fonts import addMapping
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def main():
    temp = io.BytesIO()  # create a new PDF with Reportlab
    can = canvas.Canvas(temp, pagesize=letter)  # blank field in temp to write in
    pdfmetrics.registerFont(TTFont('roboto', 'roboto-regular.ttf'))  # add new font
    can.setFont('roboto', 10)
    can.drawString(34, 793, 'ПАО "ВТФ банк", г. НОВОСИБИРСК')
    can.drawString(70, 755, '5488630408')
    can.drawString(210, 755, '418317455')
    can.drawString(34, 743, 'ЗАО "Бердск"')
    can.drawString(350, 793, '765595926')
    can.drawString(350, 780, '14420852417974866405')
    can.drawString(350, 755, '79104504004495786967')
    pdfmetrics.registerFont(TTFont('roboto_b', 'roboto-bold.ttf'))  # add new font
    can.setFont('roboto_b', 14)
    can.drawString(158, 689, '77')
    can.setFontSize(12)
    can.drawString(190, 689, '17')
    can.setFontSize(13)
    can.drawString(204, 689, 'июня')
    can.setFontSize(13)
    can.drawString(250, 689, '12')
    can.setFontSize(9)
    can.drawString(105, 654, 'ЗАО "Бердск", ИНН 5488630408, КПП 418317455, 630055, Новосибирск г, МИЧУРИНА ул, дом №')
    can.drawString(105, 644, '14, корпус 1, тел:8(732)684-81-64')
    can.drawString(105, 621, 'ООО "Черуби", ИНН 9838387316, КПП 560968574, 630048, Новосибирск г, НЕКРАСОВА ул, ')
    can.drawString(105, 611, 'дом №135, строение а, тел:8(253)568-10-01')
    can.drawString(105, 586, '№ 58561702 от 17.06.2012')
    can.setFont('roboto', 9)
    can.drawString(59, 550, 'Оплата услуг интернет, СМС и телефонии за июнь 2012г')
    with open('data.csv', 'r') as tel_file:
        tel = lab1.parse(tel_file)
    with open('data', 'r') as inet_file:
        inet = lab2.parse(inet_file)
    sum = tel+inet
    can.drawString(408, 550, f'{sum}')
    can.drawString(482, 550, f'{sum}')
    can.setFont('roboto_b', 9)
    can.drawString(481, 496, f'{sum}')
    can.drawString(481, 484, "%.2f" % (sum*0.18))  # year is 2012
    can.drawString(481, 472, f'{sum}')
    can.setFont('roboto', 9)
    can.drawString(127, 456, f'1, на сумму {sum} руб.')
    can.setFillColorRGB(1,1,1)
    can.setFont("Courier", 14)
    can.drawString(33, 444, 'Закрываем напечатанный текст')
    can.drawString(39, 444, 'Закрываем напечатанный текст')
    can.setFillColorRGB(0, 0, 0)
    can.setFont('roboto_b', 9)
    can.drawString(34, 444, 'Восемь тысяч двести один рубль 22 копейки')
    can.setFont('roboto', 9)
    can.drawString(243, 340, 'Персунов С.Б.')
    can.drawString(460, 340, 'Вубников В.В.')
    can.save()
    temp.seek(0)  # add from beginning
    new_pdf = PdfFileReader(temp)  # read what's written inside
    inputFile = PdfFileReader(open("examp.pdf", "rb"))
    outputFile = PdfFileWriter()  # file will be connected later
    page = inputFile.getPage(0)
    page.mergePage(new_pdf.getPage(0))  # merge existing page with written text
    outputFile.addPage(page)
    outputStream = open("output.pdf", "wb")
    outputFile.write(outputStream)
    outputStream.close()


if __name__ == '__main__':
    main()

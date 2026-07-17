from pypdf import PdfWriter, PdfReader; from reportlab.pdfgen import canvas; c = canvas.Canvas("test_text.pdf"); c.drawString(100, 100, "Hello World"); c.save()

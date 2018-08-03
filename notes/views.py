import csv
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import PersonalNote
from rest_framework import viewsets
from .api import PersonalNoteSerializer

class PersonalNoteViewSet(viewsets.ModelViewSet):
	serializer_class = PersonalNoteSerializer
	queryset = PersonalNote.objects.none()

	def get_queryset(self):
		# import pdb; pdb.set_trace()
		user = self.request.user

		if user.is_anonymous:
			return PersonalNote.objects.none()
		else:
			return PersonalNote.objects.filter(user=user)

def generate_pdf(request):
	notes = PersonalNote.objects.all()
 	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="notes.pdf"'
	notes_title = u", ".join(str(note.title) for note in notes).split(", ")
	notes_content = u", ".join(str(note.content) for note in notes).split(", ") 
	# Create the PDF object, using the response object as its "file."
	p = canvas.Canvas(response)

	x = 10
	y = 800

	# Draw things on the PDF. Here's where the PDF generation happens.
	# See the ReportLab documentation for the full list of functionality.
	# p.drawString(10, 800, notes_title)
	# p.drawString(10, 700, notes_content)

	for n in range(0, len(notes)):
		p.drawString(x, y, "title: " + notes_title[n] + " " + "content: " + notes_content[n])
		y -= 50

	# Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()
	return response

def generate_csv(request):
	notes = PersonalNote.objects.all()
	# create HttpResponse obj with CSV header
	response = HttpResponse(content_type='text/csv') # tell browser document is a csv file
	response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

	notes_title = [str(note.title) + "\t" for note in notes]
	notes_content = [str(note.content) + "\t" for note in notes]

	writer = csv.writer(response)
	writer.writerow(notes_title)
	writer.writerow(notes_content)

	return response









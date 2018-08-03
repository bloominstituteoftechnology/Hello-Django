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
	notes_title = u", ".join(str(note.title) for note in notes)
	notes_content = u", ".join(str(note.content) for note in notes) 
	# Create the PDF object, using the response object as its "file."
	p = canvas.Canvas(response)

	# Draw things on the PDF. Here's where the PDF generation happens.
	# See the ReportLab documentation for the full list of functionality.
	p.drawString(10, 800, notes_title)
	p.drawString(10, 700, notes_content)

	# Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()
	return response

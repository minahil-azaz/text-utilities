from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")


def analyze(request):
    if request.method != "POST":
        return HttpResponse("Please submit the form correctly.")

    # Get input text
    text = request.POST.get("text", "")

    # Initialize analyzed_text FIRST (🔥 this fixes your error)
    analyzed_text = text
    purposes = []

    # Get checkbox values
    newlineremover = request.POST.get("newlineremover", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")
    countchar = request.POST.get("countchar", "off")

    # Remove new lines
    if newlineremover == "on":
        analyzed_text = analyzed_text.replace("\n", "").replace("\r", "")
        purposes.append("Removed New Lines")

    # Remove extra spaces
    if extraspaceremover == "on":
        analyzed_text = "".join(analyzed_text.split())
        purposes.append("Removed Extra Spaces")

    # Character count
    char_count = None
    if countchar == "on":
        char_count = len(analyzed_text)
        purposes.append("Character Count")

    if not purposes:
        return HttpResponse("Please select at least one option.")

    context = {
        "purpose": ", ".join(purposes),
        "analyzed_text": analyzed_text,
        "char_count": char_count,
    }

    return render(request, "analyze.html", context)

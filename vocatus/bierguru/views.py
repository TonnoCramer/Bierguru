import json
from django.http import JsonResponse
from django.shortcuts import render
from django_ratelimit.decorators import ratelimit



from .utils import ask_vocatus
from .models import AIRequestLog, ChatMessage




# Create your views here.
def home_page(request):
    # Renders the temporary "Bierguru is away on a study trip" landing page.
    return render(request, "bierguru/home.html")

def privacy_page(request):
    # Renders the privacy page linked from the temporary landing page.
    return render(request, "bierguru/privacy.html")


@ratelimit(key="user", rate="1500/d", block=True)
@ratelimit(key="ip", rate="10/m", block=True)
def vocatus_chat(request):
    """
    Ontvangt een chatbericht en geeft AI-antwoord terug als JSON.
    """

    if request.method != "POST":
        return JsonResponse(
            {"error": "POST required"},
            status=400
        )

    try:
        data = json.loads(request.body)
        user_input = data.get("message", "")
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )

    if not user_input:
        return JsonResponse(
            {"error": "Empty message"},
            status=400
        )

    answer, messages, cost_info = ask_vocatus(user_input)
    
    # zorg dat de sessie een key heeft
    if not request.session.session_key:
        request.session.create()

    AIRequestLog.objects.create(
        user=None,
        session_key=request.session.session_key,
        input_tokens=cost_info["input_tokens"],
        output_tokens=cost_info["output_tokens"],
        request_cost=cost_info["request_cost"],
    )
    
    # chat inhoud loggen
    ChatMessage.objects.create(
        user=request.user if request.user.is_authenticated else None,
        session_key=request.session.session_key,
        user_message=user_input,
        assistant_message=answer,
    )

    return JsonResponse({
        "answer": answer,
        "cost": cost_info
    })



def chat_page(request):
    return render(request, "bierguru/chat.html")






from django.urls import path
from .views import privacy_page, vocatus_chat, chat_page, home_page




urlpatterns = [
    # Temporary "Bierguru is away on a study trip" landing page route commented out.
    #path("", home_page, name="home_page"),
    # Privacy route is also commented out because the link only belonged to the temporary "Bierguru is away on a study trip" landing page, not to the chat route.
    #path("privacy/", privacy_page, name="privacy_page"),
    path("", chat_page, name="chat_page"),          # hoofdpagina
    path("chat/", vocatus_chat, name="vocatus_chat") # API endpoint
]


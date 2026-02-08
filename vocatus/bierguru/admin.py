from django.contrib import admin
from .models import AIRequestLog, ChatMessage


@admin.register(AIRequestLog)
class AIRequestLogAdmin(admin.ModelAdmin):
    list_display = (
        "timestamp",
        "user",
        "session_key",
        "request_cost",
    )
    list_filter = ("user", "timestamp")
    ordering = ("-timestamp",)
    search_fields = ("user__username", "session_key")
    
@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ("created_at", "user", "session_key")
    search_fields = ("user_message", "assistant_message")
    ordering = ("-created_at",)

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Représente une conversation entre un utilisateur et le chatbot
class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations')
    started_at = models.DateTimeField(auto_now_add=True)

# Représente un message dans une conversation
class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=50, choices=[("user", "User"), ("chatbot", "Chatbot")])
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

from contextlib import nullcontext
from distutils.command.upload import upload
from pyexpat import model
import smtplib
from venv import create
from django.db import models
from django.forms import SlugField
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import reverse
from django.utils.html import format_html
from smtplib import SMTPAuthenticationError
from django.core.mail import send_mail
from django.conf import settings

import sys


CATEGORIA = (
    ('Web Design', 'Web Design'),
    ('Web Development', 'Web Development'),
    ('Linguagens de Programação', 'Linguagens de Programação')
)


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    categoria = models.CharField(max_length=45, choices=CATEGORIA, null=False)
    img = models.ImageField(upload_to='posts', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"slug": self.slug})


class Imagens(models.Model):
    banner = models.ImageField(upload_to='banner', null=True, blank=True)
    logo = models.ImageField(upload_to='logo', null=True, blank=True)


class Contato(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=120, null=True)
	data = models.DateTimeField(auto_now_add=True, null=True)
	email = models.EmailField(null=True)
	telefone = models.CharField(max_length=20, null=True)
	assunto = models.CharField(max_length=100, null=True)
	mensagem = models.TextField(null=True)
	email_sent = models.BooleanField(default=False, null=True)


	def __str__(self):
		return self.nome

	def send_mail(self):
		message_admin = """
		Nova Mensagem - Tales of Web
		Nome: {0}
		Email: {1}
		Telefone: {2}
		Assunto: {3}
		Mensagem: {4}
		"""
		message_admin = message_admin.format(self.nome, self.email, self.telefone, self.assunto, self.mensagem)

		message = """
Olá {0},
Obrigado por entrar em contato
Entrarei em contato o mais breve possivel!
		"""
		message = message.format(self.nome,)

		try:
			send_mail(
				'Novo Contato | Tales of Web',
				message_admin,
				'Tales of Web <talesofweb@gmail.com>',
				settings.ADMINS,
				fail_silently=False,
			)
			send_mail(
				'Auto Mensagem - Tales of Web',
				message,
				'Tales of Web <talesofweb@gmail.com>',
				[self.email],
				fail_silently=False,
			)
			self.email_sent = True
			self.save()
		except smtplib.SMTPAuthenticationError:
			pass
def send_confirmation_email(sender, instance, created, **wkargs):
	if not instance.email_sent:
		instance.send_mail()

models.signals.post_save.connect(
	send_confirmation_email, sender=Contato, dispatch_uid='contato.Record')

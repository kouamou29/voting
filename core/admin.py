from django.contrib import admin

# Register your models here.
from core.models import Mility, PartiPolic, Voting


class AdminPartiPolitic(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('user', 'name')

admin.site.register(PartiPolic, AdminPartiPolitic)

class AdminMility(admin.ModelAdmin):
    list_display = ('user_mility', 'party', 'contry', 'city')


admin.site.register(Mility, AdminMility)

class AdminVoting(admin.ModelAdmin):
    
    list_display=(  'number_voting', 'date_create')


admin.site.register(Voting, AdminVoting)    
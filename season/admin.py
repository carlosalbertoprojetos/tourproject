from django.contrib import admin

<<<<<<< HEAD
from .models import Validity, Period, Season


@admin.register(Validity)
=======
from .models import Validity, Season, Period


@admin.register(Validity)
class SeasonAdmin(admin.ModelAdmin):
    pass    
    
@admin.register(Season)
>>>>>>> novo_transport
class SeasonAdmin(admin.ModelAdmin):
    pass

<<<<<<< HEAD
@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    ...
    

@admin.register(Period)
class PeriodSeasonsDestiniesAdmin(admin.ModelAdmin):
    ...
=======
@admin.register(Period)
class PeriodSeasonsDestiniesAdmin(admin.ModelAdmin):
    pass
>>>>>>> novo_transport

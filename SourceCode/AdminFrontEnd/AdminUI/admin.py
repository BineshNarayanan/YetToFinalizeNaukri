from django.contrib import admin

from AdminUI.models import Applications, Industrygroupmaster, Industrymaster, Industrysectormaster, Posts, Postviewstats, Profileviewstats
from AdminUI.models import Provider, Providergroup, Providersubscriptiondetails, Seeker, Seekerdetails, Seekersubscriptiondetails, Subscriptionmaster, Subscriptionpaymentdetails, Subscriptiontoindustrydetails

admin.site.register(Applications)
admin.site.register(Industrygroupmaster)
admin.site.register(Industrymaster)
admin.site.register(Industrysectormaster)
admin.site.register(Posts)
admin.site.register(Postviewstats)
admin.site.register(Profileviewstats)
admin.site.register(Provider)
admin.site.register(Providergroup)
admin.site.register(Providersubscriptiondetails)
admin.site.register(Seeker)
admin.site.register(Seekerdetails)
admin.site.register(Seekersubscriptiondetails)
admin.site.register(Subscriptionmaster)
admin.site.register(Subscriptionpaymentdetails)
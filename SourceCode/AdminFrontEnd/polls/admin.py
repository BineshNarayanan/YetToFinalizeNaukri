from django.contrib import admin
from polls.models import Poll
from polls.models import Applications, Industrygroupmaster, Industrymaster, Industrysectormaster, Posts, Postviewstats, Profileviewstats
from polls.models import Provider, Providergroup, Providersubscriptiondetails, Seeker, Seekerdetails, Seekersubscriptiondetails, Subscriptionmaster, Subscriptionpaymentdetails, Subscriptiontoindustrydetails

admin.site.register(Poll)
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
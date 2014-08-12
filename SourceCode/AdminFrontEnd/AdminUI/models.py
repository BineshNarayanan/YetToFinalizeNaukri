from django.db import models

class Applications(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True) # Field name made lowercase.
    seeker_id = models.FloatField(db_column='Seeker_Id') # Field name made lowercase.
    posts_id = models.FloatField(db_column='Posts_Id') # Field name made lowercase.
    applicationdate = models.DateField(db_column='ApplicationDate', blank=True, null=True) # Field name made lowercase.
    isviewed = models.TextField(db_column='IsViewed', blank=True) # Field name made lowercase. This field type is a guess.
    createdate = models.DateField(db_column='CreateDate', blank=True, null=True) # Field name made lowercase.
    vieweddate = models.DateField(db_column='ViewedDate', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'applications'

class Industrygroupmaster(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True) # Field name made lowercase.
    industrysectormaster_id = models.FloatField(db_column='IndustrySectorMaster_Id') # Field name made lowercase.
    groupcode = models.FloatField(db_column='GroupCode', blank=True, null=True) # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'industrygroupmaster'

class Industrymaster(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True) # Field name made lowercase.
    industrygroupmaster_id = models.FloatField(db_column='IndustryGroupMaster_Id') # Field name made lowercase.
    industrycode = models.FloatField(db_column='IndustryCode', blank=True, null=True) # Field name made lowercase.
    industryname = models.CharField(db_column='IndustryName', max_length=200, blank=True) # Field name made lowercase.
    industrydescription = models.CharField(db_column='IndustryDescription', max_length=500, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'industrymaster'

class Industrysectormaster(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True) # Field name made lowercase.
    sectorcode = models.FloatField(db_column='SectorCode', blank=True, null=True) # Field name made lowercase.
    sectorname = models.CharField(db_column='SectorName', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'industrysectormaster'

class Posts(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True) # Field name made lowercase.
    providergroup_id = models.FloatField(db_column='ProviderGroup_Id') # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200) # Field name made lowercase.
    description = models.IntegerField(db_column='Description') # Field name made lowercase.
    creationdate = models.DateField(db_column='CreationDate', blank=True, null=True) # Field name made lowercase.
    domain = models.CharField(db_column='Domain', max_length=50, blank=True) # Field name made lowercase.
    postviewcount = models.FloatField(db_column='PostViewCount', blank=True, null=True) # Field name made lowercase.
    applicationcount = models.FloatField(db_column='ApplicationCount', blank=True, null=True) # Field name made lowercase.
    skillsetsrequired = models.CharField(db_column='SkillSetsRequired', max_length=1000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'posts'

class Postviewstats(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True) # Field name made lowercase.
    posts_id = models.FloatField(db_column='Posts_Id') # Field name made lowercase.
    postviewedon = models.DateField(db_column='PostViewedOn', blank=True, null=True) # Field name made lowercase.
    postviewedby = models.FloatField(db_column='PostViewedBy', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'postviewstats'

class Profileviewstats(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True) # Field name made lowercase.
    seeker_id = models.FloatField(db_column='Seeker_Id') # Field name made lowercase.
    profileviewedon = models.DateField(db_column='ProfileViewedOn', blank=True, null=True) # Field name made lowercase.
    viewedby = models.FloatField(db_column='ViewedBy', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'profileviewstats'

class Provider(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True) # Field name made lowercase.
    providergroup_id = models.FloatField(db_column='ProviderGroup_Id') # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True) # Field name made lowercase.
    providertype = models.CharField(db_column='ProviderType', max_length=20, blank=True) # Field name made lowercase.
    registrationdate = models.DateField(db_column='RegistrationDate', blank=True, null=True) # Field name made lowercase.
    createdate = models.DateField(db_column='CreateDate', blank=True, null=True) # Field name made lowercase.
    updatedate = models.DateField(db_column='UpdateDate', blank=True, null=True) # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive', blank=True) # Field name made lowercase. This field type is a guess.
    primaryemail = models.CharField(db_column='PrimaryEmail', max_length=100, blank=True) # Field name made lowercase.
    secondaryemail = models.CharField(db_column='SecondaryEmail', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'provider'

class Providergroup(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True) # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True) # Field name made lowercase.
    providertype = models.CharField(db_column='ProviderType', max_length=100, blank=True) # Field name made lowercase.
    createdate = models.DateField(db_column='CreateDate', blank=True, null=True) # Field name made lowercase.
    createdby = models.FloatField(db_column='CreatedBy', blank=True, null=True) # Field name made lowercase.
    updatedate = models.DateField(db_column='UpdateDate', blank=True, null=True) # Field name made lowercase.
    updatedby = models.FloatField(db_column='UpdatedBy', blank=True, null=True) # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive', blank=True) # Field name made lowercase. This field type is a guess.
    primaryemail = models.CharField(db_column='PrimaryEmail', max_length=100, blank=True) # Field name made lowercase.
    secondaryemail = models.CharField(db_column='SecondaryEmail', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'providergroup'

class Providersubscriptiondetails(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True) # Field name made lowercase.
    providergroup_id = models.FloatField(db_column='ProviderGroup_Id') # Field name made lowercase.
    subscriptionmaster_id = models.FloatField(db_column='SubscriptionMaster_Id') # Field name made lowercase.
    subscriptionstartdate = models.DateField(db_column='SubscriptionStartDate', blank=True, null=True) # Field name made lowercase.
    subscriptionenddate = models.DateField(db_column='SubscriptionEndDate', blank=True, null=True) # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive', blank=True) # Field name made lowercase. This field type is a guess.
    createdate = models.DateField(db_column='CreateDate', blank=True, null=True) # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=20, blank=True) # Field name made lowercase.
    updatedate = models.DateField(db_column='UpdateDate', blank=True, null=True) # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=20, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'providersubscriptiondetails'

class Seeker(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True) # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True) # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=100) # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=100, blank=True) # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100, blank=True) # Field name made lowercase.
    contactnumber1 = models.CharField(db_column='ContactNumber1', max_length=16) # Field name made lowercase.
    contactnumber2 = models.CharField(db_column='ContactNumber2', max_length=16, blank=True) # Field name made lowercase.
    contactnumber3 = models.CharField(db_column='ContactNumber3', max_length=16, blank=True) # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth') # Field name made lowercase.
    creationdate = models.DateField(db_column='CreationDate', blank=True, null=True) # Field name made lowercase.
    updatedate = models.DateField(db_column='UpdateDate', blank=True, null=True) # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive', blank=True) # Field name made lowercase. This field type is a guess.
    noticeperiodstartdate = models.DateField(db_column='NoticePeriodStartDate', blank=True, null=True) # Field name made lowercase.
    noticeperiodenddate = models.DateField(db_column='NoticePeriodEndDate', blank=True, null=True) # Field name made lowercase.
    isimmediatejoinee = models.TextField(db_column='IsImmediateJoinee', blank=True) # Field name made lowercase. This field type is a guess.
    isworkingcurrently = models.TextField(db_column='IsWorkingCurrently', blank=True) # Field name made lowercase. This field type is a guess.
    tentativejoiningdate = models.DateField(db_column='TentativeJoiningDate', blank=True, null=True) # Field name made lowercase.
    highestqualification = models.CharField(db_column='HighestQualification', max_length=100, blank=True) # Field name made lowercase.
    profileviewcount = models.IntegerField(db_column='ProfileViewCount', blank=True, null=True) # Field name made lowercase.
    primaryemail = models.CharField(db_column='PrimaryEmail', max_length=100, blank=True) # Field name made lowercase.
    secondaryemail = models.CharField(db_column='SecondaryEmail', max_length=100, blank=True) # Field name made lowercase.
    yearsofexperience = models.IntegerField(db_column='YearsOfExperience', blank=True, null=True) # Field name made lowercase.
    skillsets = models.CharField(db_column='SkillSets', max_length=1000, blank=True) # Field name made lowercase.
    industrycode = models.FloatField(db_column='IndustryCode', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'seeker'

class Seekerdetails(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True) # Field name made lowercase.
    seeker_id = models.FloatField(db_column='Seeker_Id') # Field name made lowercase.
    resume = models.TextField(db_column='Resume', blank=True) # Field name made lowercase.
    registrationdate = models.DateField(db_column='RegistrationDate', blank=True, null=True) # Field name made lowercase.
    registrationtype = models.CharField(db_column='RegistrationType', max_length=10, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'seekerdetails'

class Seekersubscriptiondetails(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True) # Field name made lowercase.
    seeker_id = models.FloatField(db_column='Seeker_Id') # Field name made lowercase.
    subscriptionmaster_id = models.FloatField(db_column='SubscriptionMaster_Id') # Field name made lowercase.
    subscriptionstartdate = models.DateField(db_column='SubscriptionStartDate', blank=True, null=True) # Field name made lowercase.
    subscriptionenddate = models.DateField(db_column='SubscriptionEndDate', blank=True, null=True) # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive', blank=True) # Field name made lowercase. This field type is a guess.
    createdate = models.DateField(db_column='CreateDate', blank=True, null=True) # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=20, blank=True) # Field name made lowercase.
    updatedate = models.DateField(db_column='UpdateDate', blank=True, null=True) # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=20, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'seekersubscriptiondetails'

class Subscriptionmaster(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True) # Field name made lowercase.
    subscriptionfor = models.CharField(db_column='SubscriptionFor', max_length=20, blank=True) # Field name made lowercase.
    subscriptionname = models.CharField(db_column='SubscriptionName', max_length=50, blank=True) # Field name made lowercase.
    subscriptiontype = models.CharField(db_column='SubscriptionType', max_length=20, blank=True) # Field name made lowercase.
    subscriptionamount = models.FloatField(db_column='SubscriptionAmount', blank=True, null=True) # Field name made lowercase.
    isactive = models.TextField(db_column='isActive', blank=True) # Field name made lowercase. This field type is a guess.
    createdate = models.DateField(db_column='CreateDate', blank=True, null=True) # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=25, blank=True) # Field name made lowercase.
    updatedate = models.DateField(db_column='UpdateDate', blank=True, null=True) # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=25, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'subscriptionmaster'

class Subscriptionpaymentdetails(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True) # Field name made lowercase.
    subscriptionmaster_id = models.FloatField(db_column='SubscriptionMaster_Id') # Field name made lowercase.
    subscriberid = models.FloatField(db_column='SubscriberId', blank=True, null=True) # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True) # Field name made lowercase.
    paymentgateway = models.CharField(db_column='PaymentGateway', max_length=100, blank=True) # Field name made lowercase.
    transactionid = models.CharField(db_column='TransactionId', max_length=100, blank=True) # Field name made lowercase.
    paymentstatus = models.TextField(db_column='PaymentStatus', blank=True) # Field name made lowercase. This field type is a guess.
    paymentdate = models.DateField(db_column='PaymentDate', blank=True, null=True) # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True) # Field name made lowercase.
    updateddate = models.DateField(db_column='UpdatedDate', blank=True, null=True) # Field name made lowercase.
    updatedby = models.FloatField(db_column='UpdatedBy', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'subscriptionpaymentdetails'

class Subscriptiontoindustrydetails(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True) # Field name made lowercase.
    industrymaster_id = models.FloatField(db_column='IndustryMaster_Id') # Field name made lowercase.
    providersubscriptiondetails_id = models.FloatField(db_column='ProviderSubscriptionDetails_Id') # Field name made lowercase.
    createdate = models.DateField(db_column='CreateDate', blank=True, null=True) # Field name made lowercase.
    createdby = models.FloatField(db_column='CreatedBy', blank=True, null=True) # Field name made lowercase.
    updatedate = models.DateField(db_column='UpdateDate', blank=True, null=True) # Field name made lowercase.
    updatedby = models.FloatField(db_column='UpdatedBy', blank=True, null=True) # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'subscriptiontoindustrydetails'


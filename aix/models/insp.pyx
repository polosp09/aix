class Axles(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'axles'


class Clientlocations(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    contactperson = models.CharField(db_column='contactPerson', max_length=255, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    clientid = models.ForeignKey('Clients', models.DO_NOTHING, db_column='ClientId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientlocations'


class Clients(models.Model):
    name = models.CharField(max_length=255)
    notifyparty = models.CharField(db_column='notifyParty', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactperson = models.CharField(db_column='contactPerson', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clients'


class Currencies(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currencies'


class Deptviews(models.Model):
    status = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    systemviewid = models.ForeignKey('Systemviews', models.DO_NOTHING, db_column='SystemViewId', blank=True, null=True)  # Field name made lowercase.
    userdepartmentid = models.ForeignKey('Userdepartments', models.DO_NOTHING, db_column='UserDepartmentId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deptviews'


class Doctypes(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctypes'


class Documents(models.Model):
    issuedate = models.DateField(db_column='issueDate', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateField(db_column='expiryDate', blank=True, null=True)  # Field name made lowercase.
    details = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    doctypeid = models.ForeignKey(Doctypes, models.DO_NOTHING, db_column='DocTypeId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'documents'


class Driverassignments(models.Model):
    status = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    vehicleid = models.ForeignKey('Vehicles', models.DO_NOTHING, db_column='VehicleId', blank=True, null=True)  # Field name made lowercase.
    driverid = models.ForeignKey('Drivers', models.DO_NOTHING, db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'driverassignments'


class Drivers(models.Model):
    names = models.CharField(unique=True, max_length=255)
    dob = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    datejoin = models.DateField(db_column='dateJoin', blank=True, null=True)  # Field name made lowercase.
    contacts = models.CharField(max_length=255, blank=True, null=True)
    deployment = models.CharField(max_length=255, blank=True, null=True)
    imageurl = models.TextField(db_column='imageUrl', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    nationalityid = models.ForeignKey('Nationalities', models.DO_NOTHING, db_column='NationalityId', blank=True, null=True)  # Field name made lowercase.

    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'drivers'


class Expensetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'expensetypes'


class Incidents(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    workordertruckid = models.ForeignKey('Workordertrucks', models.DO_NOTHING, db_column='WorkOrderTruckId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    incidenttypeid = models.ForeignKey('Incidenttypes', models.DO_NOTHING, db_column='IncidentTypeId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'incidents'


class Incidenttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'incidenttypes'


class Manufacturers(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manufacturers'


class Nationalities(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nationalities'


class Revenuetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'revenuetypes'


class Servicetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicetypes'


class Systemviews(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'systemviews'


class Trailerassignments(models.Model):
    status = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    vehicleid = models.ForeignKey('Vehicles', models.DO_NOTHING, db_column='VehicleId', blank=True, null=True)  # Field name made lowercase.
    trailerid = models.ForeignKey('Trailers', models.DO_NOTHING, db_column='TrailerId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trailerassignments'


class Trailers(models.Model):
    regno = models.CharField(db_column='regNo', unique=True, max_length=255)  # Field name made lowercase.
    yom = models.DateField(blank=True, null=True)
    model = models.CharField(max_length=255)
    maxweight = models.CharField(db_column='maxWeight', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    nationalityid = models.ForeignKey(Nationalities, models.DO_NOTHING, db_column='NationalityId', blank=True, null=True)  # Field name made lowercase.
    trailertypeid = models.ForeignKey('Trailertypes', models.DO_NOTHING, db_column='TrailerTypeId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trailers'


class Trailertypes(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trailertypes'


class Jobcardexpenses(models.Model):
    expense = models.IntegerField(blank=True, null=True)
    expenseref = models.CharField(db_column='expenseRef', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paymentstatus = models.CharField(db_column='paymentStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    expensetypeid = models.ForeignKey(Expensetypes, models.DO_NOTHING, db_column='ExpenseTypeId', blank=True, null=True)  # Field name made lowercase.
    currencyid = models.ForeignKey(Currencies, models.DO_NOTHING, db_column='CurrencyId', blank=True, null=True)  # Field name made lowercase.
    workordertruckid = models.ForeignKey('Workordertrucks', models.DO_NOTHING, db_column='WorkOrderTruckId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jobcardexpenses'


class Jobcardfuels(models.Model):
    fuel = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    station = models.CharField(max_length=255, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    fueltype = models.CharField(db_column='fuelType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    currencyid = models.ForeignKey(Currencies, models.DO_NOTHING, db_column='CurrencyId', blank=True, null=True)  # Field name made lowercase.
    workordertruckid = models.ForeignKey('Workordertrucks', models.DO_NOTHING, db_column='WorkOrderTruckId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jobcardfuels'


class Jobcardrevenues(models.Model):
    revenue = models.IntegerField(blank=True, null=True)
    financeref = models.CharField(db_column='financeRef', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invoicestatus = models.CharField(db_column='invoiceStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paymentstatus = models.CharField(db_column='paymentStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    currencyid = models.ForeignKey(Currencies, models.DO_NOTHING, db_column='CurrencyId', blank=True, null=True)  # Field name made lowercase.
    workordertruckid = models.ForeignKey('Workordertrucks', models.DO_NOTHING, db_column='WorkOrderTruckId', blank=True, null=True)  # Field name made lowercase.
    revenuetypeid = models.ForeignKey(Revenuetypes, models.DO_NOTHING, db_column='RevenueTypeId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jobcardrevenues'


class Turnmanassignments(models.Model):
    status = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    vehicleid = models.ForeignKey('Vehicles', models.DO_NOTHING, db_column='VehicleId', blank=True, null=True)  # Field name made lowercase.
    turnmanid = models.ForeignKey('Turnmans', models.DO_NOTHING, db_column='TurnmanId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turnmanassignments'


class Turnmans(models.Model):
    names = models.CharField(unique=True, max_length=255)
    dob = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    datejoin = models.DateField(db_column='dateJoin', blank=True, null=True)  # Field name made lowercase.
    contacts = models.CharField(max_length=255, blank=True, null=True)
    deployment = models.CharField(max_length=255, blank=True, null=True)
    imageurl = models.TextField(db_column='imageUrl', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    nationalityid = models.ForeignKey(Nationalities, models.DO_NOTHING, db_column='NationalityId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turnmans'


class Useraccesses(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'useraccesses'


class Useraccessviews(models.Model):
    status = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    systemviewid = models.ForeignKey(Systemviews, models.DO_NOTHING, db_column='SystemViewId', blank=True, null=True)  # Field name made lowercase.
    useraccessid = models.ForeignKey(Useraccesses, models.DO_NOTHING, db_column='UserAccessId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'useraccessviews'


class Userdepartments(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userdepartments'


class Users(models.Model):
    fullnames = models.CharField(db_column='fullNames', max_length=255, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(unique=True, max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    userdepartmentid = models.ForeignKey(Userdepartments, models.DO_NOTHING, db_column='UserDepartmentId', blank=True, null=True)  # Field name made lowercase.
    useraccessid = models.ForeignKey(Useraccesses, models.DO_NOTHING, db_column='UserAccessId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'


class Vehicles(models.Model):
    regno = models.CharField(db_column='regNo', unique=True, max_length=255)  # Field name made lowercase.
    yom = models.DateField(blank=True, null=True)
    model = models.CharField(max_length=255)
    horsepower = models.CharField(db_column='horsePower', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True)
    fulldetails = models.CharField(db_column='fullDetails', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fuelratio = models.FloatField(db_column='fuelRatio', blank=True, null=True)  # Field name made lowercase.
    chassis = models.CharField(max_length=255, blank=True, null=True)
    engineno = models.CharField(db_column='engineNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    axleid = models.ForeignKey(Axles, models.DO_NOTHING, db_column='AxleId', blank=True, null=True)  # Field name made lowercase.
    manufacturerid = models.ForeignKey(Manufacturers, models.DO_NOTHING, db_column='ManufacturerId', blank=True, null=True)  # Field name made lowercase.

    vehicletypeid = models.ForeignKey('Vehicletypes', models.DO_NOTHING, db_column='VehicleTypeId', blank=True, null=True)  # Field name made lowercase.
    nationalityid = models.ForeignKey(Nationalities, models.DO_NOTHING, db_column='NationalityId', blank=True, null=True)  # Field name made lowercase.
    driverid = models.ForeignKey(Drivers, models.DO_NOTHING, db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
    turnmanid = models.ForeignKey(Turnmans, models.DO_NOTHING, db_column='TurnmanId', blank=True, null=True)  # Field name made lowercase.
    trailerid = models.ForeignKey(Trailers, models.DO_NOTHING, db_column='TrailerId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicles'


class Vehicletypes(models.Model):
    name = models.CharField(max_length=255)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicletypes'


class Workclassifications(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    abbreviation = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workclassifications'


class Workorders(models.Model):
    workorderno = models.CharField(db_column='workOrderNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(max_length=255, blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    truckloads = models.IntegerField(db_column='truckLoads', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)
    clientref = models.CharField(db_column='clientRef', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    worktypeid = models.ForeignKey('Worktypes', models.DO_NOTHING, db_column='WorkTypeId', blank=True, null=True)  # Field name made lowercase.
    clientid = models.ForeignKey(Clients, models.DO_NOTHING, db_column='ClientId', blank=True, null=True)  # Field name made lowercase.
    currencyid = models.ForeignKey(Currencies, models.DO_NOTHING, db_column='CurrencyId', blank=True, null=True)  # Field name made lowercase.
    workclassificationid = models.ForeignKey(Workclassifications, models.DO_NOTHING, db_column='WorkClassificationId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workorders'


class Workorderservices(models.Model):
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    workorderid = models.ForeignKey(Workorders, models.DO_NOTHING, db_column='WorkOrderId', blank=True, null=True)  # Field name made lowercase.
    servicetypeid = models.ForeignKey(Servicetypes, models.DO_NOTHING, db_column='ServiceTypeId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workorderservices'


class Workorderstatuses(models.Model):
    status = models.CharField(max_length=255, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    worktypeid = models.ForeignKey('Worktypes', models.DO_NOTHING, db_column='WorkTypeId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workorderstatuses'


class Workordertrucks(models.Model):
    jobcardno = models.CharField(db_column='jobcardNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(max_length=255, blank=True, null=True)
    pickup = models.CharField(max_length=255, blank=True, null=True)
    currentstatus = models.CharField(db_column='currentStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(max_length=255, blank=True, null=True)
    jobcarddistance = models.FloatField(db_column='jobcardDistance', blank=True, null=True)  # Field name made lowercase.
    fuel = models.FloatField(blank=True, null=True)
    startmileage = models.IntegerField(db_column='startMileage', blank=True, null=True)  # Field name made lowercase.
    endmileage = models.IntegerField(db_column='endMileage', blank=True, null=True)  # Field name made lowercase.
    statusdate = models.DateTimeField(db_column='statusDate', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    workorderid = models.ForeignKey(Workorders, models.DO_NOTHING, db_column='WorkOrderId', blank=True, null=True)  # Field name made lowercase.
    vehicleid = models.ForeignKey(Vehicles, models.DO_NOTHING, db_column='VehicleId', blank=True, null=True)  # Field name made lowercase.
    clientlocationid = models.ForeignKey(Clientlocations, models.DO_NOTHING, db_column='ClientLocationId', blank=True, null=True)  # Field name made lowercase.
    trailerid = models.ForeignKey(Trailers, models.DO_NOTHING, db_column='TrailerId', blank=True, null=True)  # Field name made lowercase.
    driverid = models.ForeignKey(Drivers, models.DO_NOTHING, db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workordertrucks'


class Workordertruckstatuses(models.Model):
    remarks = models.CharField(max_length=255, blank=True, null=True)
    notifyclient = models.IntegerField(db_column='notifyClient', blank=True, null=True)  # Field name made lowercase.
    notifydept = models.IntegerField(db_column='notifyDept', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    workorderstatusid = models.ForeignKey(Workorderstatuses, models.DO_NOTHING, db_column='WorkOrderStatusId', blank=True, null=True)  # Field name made
lowercase.
    workordertruckid = models.ForeignKey(Workordertrucks, models.DO_NOTHING, db_column='WorkOrderTruckId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    userdepartmentid = models.ForeignKey(Userdepartments, models.DO_NOTHING, db_column='UserDepartmentId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workordertruckstatuses'


class Worktypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'worktypes'
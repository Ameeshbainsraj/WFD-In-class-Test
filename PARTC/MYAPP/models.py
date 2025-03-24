from django.db import models

# Customer Model
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Car Model
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=50)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    car_for_sale = models.BooleanField()

    def __str__(self):
        return f'{self.year} {self.make} {self.model}'

# Salesperson Model
class Salesperson(models.Model):
    salesperson_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Sales Invoice Model
class SalesInvoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=50)
    date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)

    def __str__(self):
        return f'Invoice {self.invoice_number}'

# Mechanic Model
class Mechanic(models.Model):
    mechanic_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Service Ticket Model
class ServiceTicket(models.Model):
    service_ticket_id = models.AutoField(primary_key=True)
    service_ticket_number = models.CharField(max_length=50)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_received = models.DateField()
    date_returned_to_customer = models.DateField()
    comments = models.TextField()

    def __str__(self):
        return f'Service Ticket {self.service_ticket_number}'

# Service Model
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name

# Service Mechanic Model
class ServiceMechanic(models.Model):
    service_mechanic_id = models.AutoField(primary_key=True)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2)  # New rate field
    comment = models.TextField()

    def __str__(self):
        return f'Service Mechanic {self.service_mechanic_id}'


# Parts Model
class Parts(models.Model):
    part_id = models.AutoField(primary_key=True)
    part_number = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.part_number

# Parts Used Model
class PartsUsed(models.Model):
    parts_used_id = models.AutoField(primary_key=True)
    part = models.ForeignKey(Parts, on_delete=models.CASCADE)
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    number_used = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Parts Used {self.parts_used_id}'

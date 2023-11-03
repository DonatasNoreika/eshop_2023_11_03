from django.contrib import admin

# Register your models here.
from .models import Product, Status, Order, OrderLine


class OrderLineInLine(admin.TabularInline):
    model = OrderLine
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'date', 'status']
    inlines = [OrderLineInLine]

admin.site.register(Product)
admin.site.register(Status)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
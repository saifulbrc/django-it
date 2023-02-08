from django import template
register=template.Library()

@regiater.filter(name='currency')
def currency(num):
    return 'Tk.' + str(num)

@register.filter(name='discount')
def discount(num):
    return 'Discount:' + str(num) + '%'

@register.filter(name='price')
def price(num,num1):
    price=num-((num*num1)/100)
    return 'Tk.' + str(price)

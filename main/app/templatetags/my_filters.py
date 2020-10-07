from django import template

register = template.Library()

def cut(value, word):
    """ 
    This will cut given {word} from {value}
    """
    return value.replace(word, "")

register.filter("cut", cut)


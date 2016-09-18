from django import template

register = template.Library()


class Extra:

    @register.filter
    def get_key(value, arg):
        """Retrieve key "arg" from dict "value" (useful for retrieving keys
        containing dots from within Django templates)."""
        return value.get(arg, None)

    register.filter('get_key', get_key)

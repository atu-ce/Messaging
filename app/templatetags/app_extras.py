from django import template
register = template.Library()


@register.filter(name='filtered_sender_messages')
def filtered_sender_messages(all_messages, user):
    return all_messages.filter(sender=user)


@register.filter(name='filtered_receiver_messages')
def filtered_receiver_messages(all_messages, user):
    return all_messages.filter(receiver=user)

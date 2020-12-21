from rest_framework.decorators import api_view
from apps.drawings.models.tickets import Ticket
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.db.models import Q


# TODO: Optimize it!
@api_view(['GET'])
def get_tickets_redemption_amount(request, pk):
    all_tickets = Ticket.objects.filter(product__pk=pk)
    tickets = all_tickets.filter(~Q(user=None))

    if tickets:
        data = {
            'all_ticks': all_tickets.count(),
            'bought': tickets.count(),
            'percent': int((tickets.count() / all_tickets.count()) * 100),
            'user_bought': tickets.filter(user=request.user).count() if request.user.is_authenticated else None
        }
        return Response(data=data, status=HTTP_200_OK)

    # Return `None` if product is not available for drawing.
    return Response(data=None, status=HTTP_200_OK)

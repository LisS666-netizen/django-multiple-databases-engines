from django.core.management.base import BaseCommand

from bsolutions.domain.models.notifications import NotificacionFactory
from bsolutions.domain.models.purchase import CompraProductoFactory


class Command(BaseCommand):
    help = '--iteraciones para asignar un numero maximo de iteraciones'

    def add_arguments(self, parser):
        parser.add_argument(
            '--iteraciones',
            default=100000,
            type=int,
            help='numero de iteraciones'
        )

    def handle(self, *args, **options):
        for i in range(options['iteraciones']):
            CompraProductoFactory()
            NotificacionFactory()
            if i % 10000 == 0:
                print(f"elementos creados iteracion # {i}")

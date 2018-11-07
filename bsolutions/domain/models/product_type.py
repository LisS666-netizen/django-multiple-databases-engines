from django.db import models
import factory
import factory.django
import factory.fuzzy


class TipoProducto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    # idProductType

    class Meta:
        db_table = "tipo_producto"
        verbose_name_plural = "product_types"

    def __str__(self):
        return '%s' % self.nombre


class TipoProductoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TipoProducto

    nombre = factory.Faker('word')

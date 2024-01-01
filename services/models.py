from django.db import models
from django.urls import reverse
from django.conf import settings

from modules.servicess.utils import unique_slugify


class CategoryService(models.Model):
    """Категории услуг"""
    name = models.CharField("Имя", max_length=50, unique=True)
    slug = models.SlugField('URL', max_length=100, db_index=True, unique=True, )
    icon = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    objects = models.Manager()
    
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("servece_by_category", kwargs={"slug": self.slug})
     
    class Meta:
         verbose_name = "Категория услуг"
         verbose_name_plural ='Категории услуг'


class ServiceModer(models.Manager):
    """метод вывода видимых объявлений"""
    def moderation(self):
        return self.filter(moderation=True)

class Service(models.Model):
    """Послуги"""
    category = models.ForeignKey(CategoryService, verbose_name="Категорія*", on_delete=models.CASCADE,
                                related_name='services_category')
    brend = models.CharField("Бренд", max_length=50, blank=True)
    subject = models.CharField("Назва послуги*", max_length=200)
    description = models.TextField("Опис посуги*", max_length=10000)
    images = models.ImageField('Фото', upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, blank=True)
    location = models.CharField('Адреса*', max_length=100)
    name = models.CharField("Ваше ім'я*", max_length=50)
    email = models.EmailField(verbose_name='эл.почта', blank=True)
    telefon = models.CharField('номер телефона', blank=True, max_length=13)
    moderation = models.BooleanField("Модерация", default=True)
    slug = models.CharField(verbose_name='Альт.название', max_length=255, blank=True, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE,
                            related_name='services_user')
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    #views = models.IntegerField('количество просмотров', default=0)

    objects = models.Manager()
    custom_serv = ServiceModer()

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.subject)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.subject)

    def get_absolute_url(self):
        return reverse("detail_service", kwargs={ "slug": self.slug})

    class Meta:
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"



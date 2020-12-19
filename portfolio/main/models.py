from django.db import models

# Create your models here.


class Menu(models.Model):
    menu_name = models.CharField(max_length=256, null=True, blank=True)
    menu_link = models.CharField(max_length=256, null=True, blank=True)
    except_link = models.CharField(max_length=256, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.menu_name

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'


class HeadFoot(models.Model):
    logo = models.FileField(null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    profile_img = models.FileField(null=True, blank=True)
    head_btn = models.CharField(null=True, blank=True, max_length=256)
    quest = models.CharField(null=True, blank=True, max_length=256)
    foot_btn = models.CharField(max_length=256, null=True, blank=True)
    foot_icon = models.FileField(null=True, blank=True)
    foot_info = models.CharField(max_length=256, null=True, blank=True)
    foot_photo = models.FileField(null=True, blank=True)
    photo_class = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.foot_info

    class Meta:
        verbose_name = 'HeadFoot Item'
        verbose_name_plural = 'HeadFoot Items'


class Gallery(models.Model):
    photo = models.FileField(null=True, blank=True)
    photo2 = models.FileField(null=True, blank=True)
    photo_class = models.CharField(max_length=256, null=True, blank=True)
    photo_class2 = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.photo_class

    class Meta:
        verbose_name = 'Gallery Item'
        verbose_name_plural = 'Gallery Items'


class Client(models.Model):
    f_name = models.CharField(max_length=256, null=True, blank=True)
    l_name = models.CharField(max_length=256, null=True, blank=True)
    btn = models.CharField(max_length=256, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    n_info = models.CharField(max_length=256, null=True, blank=True)
    l_info = models.CharField(max_length=256, null=True, blank=True)
    quest_info = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
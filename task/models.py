from django.db import models

class Image(models.Model):
    link = models.URLField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    # def save(self, *args, **kwargs):
    #     if self.id == None:
    #         if Image.objects.filter(ad=self.ad).count() > 3:
    #             raise Exception(f'{self.ad.name} has already 3 images. No more are allowed.')
    #     return super(Image, self).save(*args, **kwargs)

class Ad(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Advertisement'
        verbose_name_plural = 'Advertisements'


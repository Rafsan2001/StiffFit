from django.core.mail import message
from django.db import models

from django.contrib.auth.models import User
from django.utils.html import mark_safe

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Banners(models.Model):
	img=models.ImageField(upload_to="banners/" ,null=True)
	alt_text=models.CharField(max_length=150,null=True)

	class Meta:
		verbose_name_plural='Banners'

	def __str__(self):
		return self.alt_text

	def image_tag(self):
		return mark_safe('<img src="%s" width="80" />' % (self.img.url))
    
class Trainer(models.Model):
    CATEGORY = (
                ('Yoga Trainer', 'Yoga Trainer'),
                ('Gym Master', 'Gym Master'),
                ('Nutritionist', 'Nutritionist'),
                )
    trainer = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=100, null=True)
    pwd = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=False)
    salary = models.IntegerField(default=0)
    img = models.ImageField(upload_to="trainers/", null=True)

    facebook = models.CharField(max_length=200, null=True)
    twitter = models.CharField(max_length=200, null=True)
    pinterest = models.CharField(max_length=200, null=True)
    youtube = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.trainer

    def Image_tag(self):
        if self.img:
            return mark_safe('<img src="%s" width="80" />' % (self.img.url))
        else:
            return 'no-image'


class Package(models.Model):
    TYPE = (
                ('Yoga', 'Yoga'),
                ('Gym', 'Gym'),
                ('Balanced Nutrition Diet', 'Balanced Nutrition Diet'),
                )
    package = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    type = models.CharField(max_length=200, null=True, choices=TYPE)

    def __str__(self):
        return self.package


class Progress(models.Model):
    STATUS = (
('Pending', 'Pending'),
                ('Progressing', 'Progressing'),
                ('Completed', 'Completed'),
)
    trainer = models.ForeignKey(Trainer, null=True, on_delete=models.SET_NULL)
    package = models.ForeignKey(Package, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.trainee.trainee


class Page(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()

    def __str__(self):
        return self.title


class Faq(models.Model):
    quest = models.TextField()
    ans = models.TextField()

    def __str__(self):
        return self.quest


class Enquiry(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    detail = models.TextField()

    def __str__(self):
        return self.full_name


class Notify(models.Model):
    notify_detail = models.TextField()
    read_by_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.notify_detail)


class NotifUserStatus(models.Model):
	notif = models.ForeignKey(Notify, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = 'Notification Status'

# Gallery Model


class Gallery(models.Model):
    title = models.CharField(max_length=150)
    details = models.TextField()
    img = models.ImageField(upload_to="gallery/", null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))

# Gallery Images


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True)
    alt_text = models.CharField(max_length=150)
    img = models.ImageField(upload_to="gallery_imgs/", null=True)

    def __str__(self):
        return self.alt_text

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))

# Plans
# Subscription Plans


class SubPlan(models.Model):
	title = models.CharField(max_length=150)
	price = models.IntegerField()
	max_member = models.IntegerField(null=True)
	highlight_status = models.BooleanField(default=False, null=True)
	validity_days = models.IntegerField(null=True)

	def __str__(self):
		return self.title

# Subscription Plans Features


class SubPlanFeature(models.Model):
	subplan = models.ManyToManyField(SubPlan)
	title = models.CharField(max_length=150)

	def __str__(self):
		return self.title

# Package Discounts


class PlanDiscount(models.Model):
	subplan = models.ForeignKey(SubPlan, on_delete=models.CASCADE, null=True)
	total_months = models.IntegerField()
	total_discount = models.IntegerField()

	def __str__(self):
		return str(self.total_months)


class Subscriber(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	mobile = models.CharField(max_length=20, null=True)
	address = models.TextField(null=True)
	img = models.ImageField(upload_to="Subscriber/", null=True)

	def __str__(self):
		return str(self.user)

	def image_tag(self):
		if self.img:
			return mark_safe('<img src="%s" width="80" />' % (self.img.url))
		else:
			return 'no-image'


@receiver(post_save, sender=User)
def create_subscriber(sender, instance, created, **kwrags):
	if created:
		Subscriber.objects.create(user=instance)


# Subscription
class Subscription(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	plan=models.ForeignKey(SubPlan, on_delete=models.CASCADE,null=True)
	price=models.CharField(max_length=50)
	reg_date=models.DateField(auto_now_add=True,null=True)


# TrainerSalary Model

class TrainerSalary(models.Model):
    trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE)
    amt=models.IntegerField()
    amt_date=models.DateField()
    remarks=models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural='Trainer Salary'
    
    def __str__(self):
        return str (self.trainer.trainer)


# Assign Subscriber to Trainer
class AssignSubscriber(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user)
    
#Trainer Notification
class TrainerNotification(models.Model):
    notif_msg=models.TextField()
    
    def __str__(self):
        return str(self.notif_msg)
    
#Marks read Notification by trainer
class NotifTrainerStatus(models.Model):
    notif_msg=models.ForeignKey(TrainerNotification, on_delete=models.CASCADE)
    trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    class Meta:
        verbose_name_plural='Trainer Notification Status'

#Trainer Achivement
class TrainerAchivement(models.Model):
	trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	detail=models.TextField()
	img=models.ImageField(upload_to="trainers_achivements/")

	def __str__(self):
		return str(self.title)

	def image_tag(self):
		if self.img:
			return mark_safe('<img src="%s" width="80" />' % (self.img.url))
		else:
			return 'no-image'
        
#SubscriberMsg
class TrainerMsg(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True)
    message=models.TextField()
    class Meta:
        verbose_name_plural='Messages For Trainer'


class TrainerSubscriberReport(models.Model):
	report_for_trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True,related_name='report_for_trainer')
	report_for_user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='report_for_user')
	report_from_trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True,related_name='report_from_trainer',blank=True)
	report_from_user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='report_from_user',blank=True)
	report_msg=models.TextField()

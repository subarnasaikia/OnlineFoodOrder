from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import UserProfile, User


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('user profile created')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # create the userprofile if not exits
            UserProfile.objects.create(user=instance)
            print('User profile is not exits, But now created')
        print('user profile updated')

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'This user is being saved')

# post_save.connect(post_save_create_profile, sender=User)
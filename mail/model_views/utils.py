from django.urls import reverse


class ProfileSuccessUrl:
    def get_success_url(self):
        """Перенаправление на страницу """
        return reverse('users:profile', args=[self.object.autor.pk])

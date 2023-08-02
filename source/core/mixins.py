from typing import Optional
from django.contrib.auth.mixins import UserPassesTestMixin

class SuperUsuarioAutorMixin(UserPassesTestMixin):
    def test_func(self):
        usuario = self.request.user
        obj = self.get_object()
        
        if hasattr(obj, 'autor'):
            return usuario == obj.relacion_post.autor or usuario == obj.autor or usuario.es_admin or usuario.es_superuser

class ColabUsuarioMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.es_admin or self.request.user.es_colab or self.request.user.is_superuser
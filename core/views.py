from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from core.models import Usuario, Tarefas, Grupos
from core.serializers import UsuarioSerializer, UsuarioCreateSerializer, TarefasSerializer, DetailTarefasSerializer, GruposSerializer, DetailGruposSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['id'] = self.user.id
        data['email'] = self.user.email
        data['is_superuser'] = self.user.is_superuser
        
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["create"]:
            return UsuarioCreateSerializer
        return UsuarioSerializer


class TarefasViewSet(ModelViewSet):
    queryset = Tarefas.objects.all()
    serializer_class = TarefasSerializer 
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailTarefasSerializer
        return TarefasSerializer

class GruposViewSet(ModelViewSet):
    queryset = Grupos.objects.all()
    serializer_class = GruposSerializer 
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailGruposSerializer
        return GruposSerializer
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from core.models import Usuario, Tarefas, Grupos, Topic, conjTopic, CreateGp, Chats
from core.serializers import (
    UsuarioSerializer,
    UsuarioCreateSerializer,
    TarefasSerializer,
    DetailTarefasSerializer,
    GruposSerializer,
    DetailGruposSerializer,
    TopicSerializer,
    DetailTopicSerializer,
    conjTopicSerializer,
    DetailconjTopicSerializer,
    CreateGpSerializer,
    DetailCreateGpSerializer,
    ChatsSerializer,
    DetailChatsSerializer,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["username"] = self.user.username
        data["id"] = self.user.id
        data["email"] = self.user.email
        data["is_superuser"] = self.user.is_superuser

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


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailTopicSerializer
        return TopicSerializer


class conjTopicViewSet(ModelViewSet):
    queryset = conjTopic.objects.all()
    serializer_class = conjTopicSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailconjTopicSerializer
        return conjTopicSerializer


class CreateGpViewSet(ModelViewSet):
    queryset = CreateGp.objects.all()
    serializer_class = CreateGpSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailCreateGpSerializer
        return CreateGpSerializer


class ChatsViewSet(ModelViewSet):
    queryset = Chats.objects.all()
    serializer_class = ChatsSerializer 
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailChatsSerializer
        return ChatsSerializer
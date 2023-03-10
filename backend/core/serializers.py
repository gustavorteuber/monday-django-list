from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from core.models import Usuario, Grupos, Tarefas, Topic, conjTopic, CreateGp, Chats
from uploader.models import Image
from uploader.serializers import ImageSerializer


class GruposSerializer(ModelSerializer):
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True, default=None)
    class Meta:
        model = Grupos
        fields = "__all__"


class TarefasSerializer(ModelSerializer):
    class Meta:
        model = Tarefas
        fields = "__all__"


class UsuarioSerializer(ModelSerializer):
    password_confirmation = serializers.CharField(max_length=150, write_only=True)
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True, default=None)
    id = serializers.IntegerField(read_only=True, required=False)
    grupos = GruposSerializer(many=True)
    tarefas = TarefasSerializer(many=True)

    class Meta:
        model = Usuario
        read_only_fields = ("id",)
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "password_confirmation",
            "foto",
            "foto_attachment_key",
            "grupos",
            "tarefas",
        )

    def validate(self, args):
        email = args.get("email", None)
        username = args.get("username", None)
        password = args.get("password")
        password_confirmation = args.get("password_confirmation")
        print(username)
        print(password)
        print(password_confirmation)
        if password != password_confirmation:
            raise serializers.ValidationError(
                {"password": ("as senhas n??o s??o iguais")}
            )
        if Usuario.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": ("esse email j?? est?? cadastrado")}
            )
        if Usuario.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"username": ("esse nome de usuario j?? est?? em uso")}
            )

        return super().validate(args)


class UsuarioCreateSerializer(ModelSerializer):
    password_confirmation = serializers.CharField(max_length=150, write_only=True)
    id = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Usuario
        read_only_fields = ("id",)
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "password_confirmation",
        )

    def validate(self, args):
        email = args.get("email", None)
        username = args.get("username", None)
        password = args.get("password")
        password_confirmation = args.get("password_confirmation")
        if password != password_confirmation:
            raise serializers.ValidationError(
                {"password": ("As senhas n??o s??o iguais")}
            )
        if Usuario.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": ("o email ja existe")})
        if Usuario.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"username": ("esse nome de usuario ja est?? em uso")}
            )

        return super().validate(args)

    def create(self, validated_data):
        validated_data.pop("password_confirmation")
        newUser = Usuario.objects.create_user(**validated_data)
        newUser.foto = None
        newUser.save()
        return newUser


class DetailGruposSerializer(ModelSerializer):
    class Meta:
        model = Grupos
        fields = "__all__"
        depth = 2


class DetailTarefasSerializer(ModelSerializer):
    class Meta:
        model = Tarefas
        fields = "__all__"
        depth = 2


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class DetailTopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"
        depth = 1


class conjTopicSerializer(ModelSerializer):
    class Meta:
        model = conjTopic
        fields = "__all__"


class DetailconjTopicSerializer(ModelSerializer):
    class Meta:
        model = conjTopic
        fields = "__all__"
        depth = 2


class CreateGpSerializer(ModelSerializer):
    class Meta:
        model = CreateGp
        fields = "__all__"


class DetailCreateGpSerializer(ModelSerializer):
    class Meta:
        model = CreateGp
        fields = "__all__"
        depth = 2

class ChatsSerializer(ModelSerializer):
    class Meta:
        model = Chats
        fields = "__all__"
        
        
class DetailChatsSerializer(ModelSerializer):
    class Meta:
        model = Chats
        fields = "__all__"
        depth = 1
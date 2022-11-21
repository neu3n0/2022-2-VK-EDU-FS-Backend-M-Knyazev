from messageschat.models import Message

from .serializers import MessageSerializer, MessageCreateSerializer, MessageEditSerializer

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView


class MessageCreate(CreateAPIView):
    serializer_class = MessageCreateSerializer
    queryset = Message.objects.all()


class MessageRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return MessageEditSerializer
        return MessageSerializer


# @require_GET
# def get_messages_from_chat(request, chat_pk):
#     get_object_or_404(Chat, pk=chat_pk)
#     messages = Message.objects.filter(chat_id=chat_pk)
#     if request.GET.get('user'):
#         messages = messages.filter(author_id=request.GET['user'])
#     messages_ar = []
#     for mess in messages:
#         messages_ar.append({
#             'user': mess.author.username,
#             'text': mess.text,
#             'date': mess.pub_date,
#             'readed': mess.is_readed
#         })
#     messages_ar = messages_ar[0:20]
#     return JsonResponse({'messages': messages_ar})


# def messages_list(request, user_id):
#     author = get_object_or_404(User, id=user_id)
#     messages = Message.objects.filter(author__id=user_id)
#     data = MessageListSerializer(messages, many=True).data
#     return JsonResponse({'messages': data})


# class MessageUserList(ListAPIView):
#     serializer_class = MessageSerializer
#     # queryset = Message.objects.all()

#     def get_queryset(self):
#         user_id = self.kwargs['user_id']
#         user = get_object_or_404(User, id=user_id)
#         return Message.objects.filter(author=user)

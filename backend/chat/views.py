from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import ChatMessage as Message
from .serializers import MessageSerializer, UserSerializer

User = get_user_model()

class ChatRoomAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, room_name, format=None):
        search_query = request.GET.get('search', '')
        # Get users except the logged-in user
        users = User.objects.exclude(id=request.user.id)
        
        # Filter messages where sender or receiver username matches the room_name
        chats = Message.objects.filter(
            (Q(sender=request.user) & Q(receiver__username=room_name)) |
            (Q(receiver=request.user) & Q(sender__username=room_name))
        )
        if search_query:
            chats = chats.filter(Q(content__icontains=search_query))
        chats = chats.order_by('timestamp')
        
        # For each user, get the last message exchanged with request.user.
        user_last_messages = []
        for user in users:
            last_message = Message.objects.filter(
                (Q(sender=request.user) & Q(receiver=user)) |
                (Q(receiver=request.user) & Q(sender=user))
            ).order_by('-timestamp').first()
            serialized_last_message = MessageSerializer(last_message).data if last_message else None
            user_last_messages.append({
                'user': UserSerializer(user).data,
                'last_message': serialized_last_message
            })
            
        # Sort the last messages descending by timestamp (if exists)
        user_last_messages.sort(
            key=lambda x: x['last_message']['timestamp'] if x['last_message'] else '',
            reverse=True
        )
        
        response_data = {
            'room_name': room_name,
            'chats': MessageSerializer(chats, many=True).data,
            'users': UserSerializer(users, many=True).data,
            'user_last_messages': user_last_messages,
            'search_query': search_query,
        }
        return Response(response_data)
    

class UserSearchAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = request.GET.get('q', '')
        if query:
            users = User.objects.filter(
                Q(username__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )
        else:
            users = User.objects.none()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


# New API view: returns distinct chats for the current user
class AvailableChatsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        messages = Message.objects.filter(
            Q(sender=request.user) | Q(receiver=request.user)
        ).order_by('-timestamp')
        
        chats = {}
        for msg in messages:
            partner = msg.receiver if msg.sender == request.user else msg.sender
            room_name = "_".join(sorted([request.user.username, partner.username]))  # Generate room name
            
            if partner.id not in chats:
                chats[partner.id] = {
                    'id': partner.id,
                    'name': f"{partner.first_name} {partner.last_name}",
                    'room_name': room_name,  # Add this
                    'lastMessage': msg.content if msg else "No messages",
                    'time': msg.timestamp.isoformat() if msg else "",
                    'user': UserSerializer(partner).data
                }
        return Response(list(chats.values()))
    
class CreateMessageAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, receiver_id):
        try:
            receiver = User.objects.get(pk=receiver_id)
            message = Message.objects.create(
                sender=request.user,
                receiver=receiver,
                content=request.data['content']
            )
            return Response(MessageSerializer(message).data, status=201)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
from django.shortcuts import render

def chatindex(request):
    return render(request,'chat/chatindex.html')

def room(request,room_name):
    return render(request, 'chat/room.html', {
        'room_name':room_name
    })
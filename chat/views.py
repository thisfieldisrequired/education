from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


@login_required
def course_chat_room(request, course_id):
    """запрос курса по id, с текущим пользователем"""
    try:
        course = request.user.courses_joined.get(id=course_id)
    except ValueError:
        return HttpResponseForbidden()  # пользователь не является студентом курса
    return render(request, "chat/room.html", {"course": course})

from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse


def staff_group_required(view_func):
    """
    Decorator for views that checks if the user is a member of the 'staff group'.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse('access-denied'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view

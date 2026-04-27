import os
import sys
import traceback
import django

print("CREATE_ADMIN.PY STARTED", flush=True)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "starbright.settings")

print("SETTINGS MODULE SET", flush=True)

try:
    django.setup()
    print("DJANGO SETUP COMPLETE", flush=True)

    from django.contrib.auth import get_user_model

    User = get_user_model()

    username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
    email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
    password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "starbright2026!")

    print(f"Checking if user '{username}' exists...", flush=True)

    if User.objects.filter(username=username).exists():
        print(f"Superuser '{username}' already exists.", flush=True)
    else:
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"Superuser '{username}' created successfully.", flush=True)

except Exception:
    print("ERROR OCCURRED:", flush=True)
    traceback.print_exc()
    sys.exit(1)

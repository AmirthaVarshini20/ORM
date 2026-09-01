# Ex01 Django ORM Web Application
# Date:20-08-2026
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 cars

# PROGRAM
```
admin.py:

from django.contrib import admin
from .models import Employee,EmployeeAdmin
admin.site.register(Employee,EmployeeAdmin)
```
```
urls.py:

urlpatterns = [
    path('admin/', admin.site.urls),
   
]
```
# OUTPUT

<img width="1917" height="1087" alt="Screenshot 2026-08-30 203626" src="https://github.com/user-attachments/assets/eff2789c-9b77-4277-9566-056afad78370" />

<img width="1917" height="1081" alt="Screenshot 2026-08-30 203724" src="https://github.com/user-attachments/assets/0c0b4771-e042-4988-9da7-464c449bc5c8" />

<img width="1917" height="1088" alt="Screenshot 2026-08-30 203749" src="https://github.com/user-attachments/assets/2d397f27-c34d-4356-911f-692a1b45d87d" />

<img width="1917" height="1080" alt="Screenshot 2026-08-30 203813" src="https://github.com/user-attachments/assets/da499817-6378-46a8-a3eb-053a2a5df11f" />


# RESULT
Thus the program for creating a database using ORM hass been executed successfully

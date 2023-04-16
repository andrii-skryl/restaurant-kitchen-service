# restaurant-kitchen-service

This project was created for managing restaurant's kitchen which combines relations between cooks, dishes which they make, and dish types that every dish is related to.

Using this project you can create, update and delete samples of each object - cook, dish type and dish.
Also, you can search through the lists of existing objects by their name (dish types and dishes) and by username (cooks).

## Check it out!

[Kitchen Service project deployed to Render](https://restaurant-kitchen-service-44uq.onrender.com/)

## Set up

1. Copy this repository on your PC using the next command in your IDEA terminal:

```
git clone https://github.com/andrii-skryl/restaurant-kitchen-service
```

2. Change directory ot the root project folder:

```
cd restaurant-kitchen-service
```

3. Install venv, with the next command:

```
python -m venv venv
```

4. Activate venv with following commands:

- for Windows:

```
venv/Scripts/activate
```

- for Linux or macOS:

```
source venv/bin/activate
```
4. Install dependencies from requirements.txt:

```
pip install -r requirements.txt
```

5. Create .env file in the project's root directory.
6. Write a SECRET_KEY environmental variable inside .env file (example of how it should be written you can find at ".env_sample" file) 

7. Run migrations into db:

```
python manage.py migrate
```

8. Run the server:

```
python manage.py runserver
```
9. To use the website you will need to sign in into the system. Use the next login and password:
  - Login: `test_user`
  - Password: `user12345`

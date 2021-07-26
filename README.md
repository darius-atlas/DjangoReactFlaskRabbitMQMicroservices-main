Clone this project as 'main' folder<br>


# Migrate
1. docker-compose up
2. docker-compose exec main sh
3. python manager.py db init
4. python manager.py db migrate
5. python manager.py db upgrade

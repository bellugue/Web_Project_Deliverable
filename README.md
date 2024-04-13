# CarRentingUdL
<p align="center">
  <p align="center">
    <BR>
  Web Project assignment 2023/2024 <BR>
Universtat de Lleida
</p>


Developers
-------------
- Arnau Martí Sanchez - [arnaums02](https://github.com/arnaums02)
- Quim Sanchez Benet - [quimsb03](https://github.com/quimsb03)
- Ramon Segarra Riu - [bellugue](https://github.com/bellugue)
- Theo Moreno Lomero - [MoreTheo](https://github.com/MoreTheo)
- Eloi Vergé Ponsarnau - [elvepo029](https://github.com/elvepo029)
- Joel Sambola Farran -

Implementation
-------------
- [x] Allow users to register to the website
- [x] Allow users that have an account to sign-up
- [x] Allow users to find a specific car in a selected authorised dealer
- [x] Allow registered users to rent a car for a time

Usage
---------

**To Build the web:**
1. Build:
```
docker build -t deliverable1
```
2. Run:
```
docker run -p 8000:8000 deliverable1
```
3. Do makemigrations  & migrate in the container:

&ensp; Use ```Docker ps``` in another Terminal to see running containers and ```docker exec -t -i container_id bash``` to open container's terminal.
```
python manage.py makemigrations
```
```
python manage.py migrate
```
4. Create superuser in the container:
```
python manage.py createsuperuser
```
5. Go to [LocalHost](http://localhost:8000/)

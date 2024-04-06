# CarRentingUdL
<p align="center">
  <p align="center">
    <BR>
  Web Project assignment 2022/2023 <BR>
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

Usage
---------

**To Build the web:**
1. Build:
```
docker-compose up -d --build  
```
2. Run:
```
docker-compose up
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
5. Go to [LocalHost](http://0.0.0.0/)

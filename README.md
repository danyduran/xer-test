# Tecnologias
- Python 3.10
- Postgresql
- Docker
- Django
- Django rest framework
- Django filters

# Instrucciones
- Tener instalado docker en la pc
- moverse al folder del proyecto en la terminal
- correr **docker-compose build**
- Aplicar migratons usando **docker run django python manage.py migrate**
- Correr **docker-compose up**
- Opcional: crear un superuser para entrar al admin **docker run django python manage.py creatersuperuser**

Con esto ya el REST API esta levantado en **localhost:8000** y podemos hacer uso de y el API ROOT **http://localhost:8000/league/** donde encontraremos dos endpoints uno para equipos y otro para jugadores.

# Testing Endpoints
## Endpoint Teams
### Obteniendo team(s)
**Endpoint**:  http://localhost:8000/league/teams/
**Endpoint**:  http://localhost:8000/league/teams/{id}
Podemos obtener resources team usando el verbo HTTP GET con los EP de arriba, el primero es para obtener todos los teams y el segundo es para obtener un team especifico usando su id.
#### Query params de Team
podemos filtrar usando query params de la siguiente forma
> http://localhost:8000/league/teams/?name=Pumas&city=Mexico city

Solo podemos filtrar por los siguientes query params:
    - city
    - name
### creando team
**Endpoint**:  http://localhost:8000/league/teams/
podemos crear un resource player usando el verbo HTTP POST y mandando el body:
```json
{
	"name": "Cruz Azul",
	"city": "Mexico city"
}
```
### Actualizando team
**Endpoint**:  http://localhost:8000/league/teams/{id}/
podemos actualizar un resource player usando el verbo HTTP PUT or PATCH y mandando el body:
```json
{
	"name": "Cruz Azul",
	"city": "Mexico city"
}
```
### Borrando team
**Endpoint**:  http://localhost:8000/league/teams/{id}/
podemos borrar un resource player usando el verbo HTTP DELETE.

## Endpoint PLAYERS
### Obteniendo players(s)
**Endpoint**:  http://localhost:8000/league/players/
**Endpoint**:  http://localhost:8000/league/players/{id}
Podemos obtener resources players usando el verbo HTTP GET con los EP de arriba, el primero es para obtener todos los players y el segundo es para obtener un player especifico usando su id.
#### Query params de players
podemos filtrar usando query params de la siguiente forma
> http://localhost:8000/league/players/?team=Pumas&name=Ronaldo&goals=4

Solo podemos filtrar por los siguientes query params:
    - name
    - goals
    - team
### creando player
**Endpoint**:  http://localhost:8000/league/players/
podemos crear un resource player usando el verbo HTTP POST y mandando el body:
```json
    {
        "name": "Ronaldo",
        "team": 2,
        "goals": 5
    }
```
### Actualizando Player
**Endpoint**:  http://localhost:8000/league/players/{id}/
podemos actualizar un resource player usando el verbo HTTP PUT or PATCH y mandando el body:
```json
{
	"name": "Ronaldo",
	"team": 2,
	"goals": 5
}
```
### Borrando team
**Endpoint**:  http://localhost:8000/league/players/{id}/
podemos borrar un resource player usando el verbo HTTP DELETE.

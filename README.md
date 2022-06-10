# Python-Schema

<h3>:construction: Entorno de trabajo: :warning:ATENCIÓN: comandos válidos en Windows 10. Es posible que otros sistemas operativos necesiten usar otras formas de instalación:warning:</h3>
<li>Instalamos <b>Python 3.9</b></li> 
<li>Creamos con: <b>py -m venv env_Q_API</b> #Ya viene creado desde el repositorio!!</li> 
<li>Activamos en WINDOWS con: <b>env_Q_API\Scripts\activate</b></li>
<li>Activamos en MAC con: <b>source env_Q_API/bin/activate</b></li>
<h3>:books: Dependencias</h3>
<li>Instalamos librerías con: <b>pip3 install -r requirements.txt</b></li>
<h3>:mag_right: Testing</h3>
<li>Lanzamos los tests con <b>pytest -W ignore::DeprecationWarning</b></li>
<h3>:rocket: Lanzamos el proyecto con:</h3>
<li><b>uvicorn main:app --reload</b></li>
<h3>:chart_with_upwards_trend: Documentación API</h3>
<li>Abrir <b>http://127.0.0.1:8000/docs</b> en un navegador</li>

<h3>Despliegue en Heroku :warning:ATENCIÓN: NO USAR ESTOS COMANDOS SIN PERMISO</h3>
<li>heroku login</li>
<li>git add .</li>
<li>git commit -am "make it better"</li>
<li>git push heroku master</li>
<li>Abrir <b>...</b> en un navegador</li>
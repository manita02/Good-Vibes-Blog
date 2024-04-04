<section align="center">
    <h1 align="center">🌅🌊GOOD VIBES BLOG🤙🍹</h1>
    <img src="https://i.pinimg.com/564x/76/7f/a0/767fa07bca549f5a5f2f25c910f58e7e.jpg">
   <section align="center">
        <img src="https://img.shields.io/badge/STATE-FINISHED-green" alt="Estado del Proyecto">
   </section>
</section>


# Índice
- [Sobre Good Vibes Blog :call_me_hand::ocean::sunglasses:](#sobre-good-vibes-blog-call_me_handoceansunglasses)
- [Programas necesarios :memo:](#white_check_mark-programas-necesariosmemo)
- [Descargar proyecto :inbox_tray:](#white_check_mark-descargar-proyectoinbox_tray) 
- [Crear Base de Datos :wrench:](#white_check_mark-crear-base-de-datoswrench)
- [Configurar el archivo configuracion.py :nut_and_bolt:](#white_check_mark-configurar-el-archivo-configuracionpynut_and_bolt)
- [Ejecutar el proyecto :rocket:](#white_check_mark-ejecutar-el-proyectorocket)
- [Funcionalidades :clipboard:](#funcionalidades-clipboard)
- [Tecnologías utilizadas :hammer:](#tecnologías-utilizadas-hammer)
- [Autor :black_nib:](#autor-black_nib)


## Sobre Good Vibes Blog :call_me_hand::ocean::sunglasses:
<p align="justify">
    Aplicación web desarrollada con Python, MySQL, Flask, SQLAlchemy,  HTML y CSS que permite que distintos usuarios👤 agreguen, editen o eliminen publicaciones✍️ en el blog. Además los usuarios pueden editar🖋️ o eliminar🗑️ su perfil.
</p>


### :white_check_mark: `Programas necesarios`:memo:
- Descargar e Instalar :arrow_down_small: 
  - <a href="https://www.youtube.com/watch?v=hUZKNsnHe_A" target="_blank"> 
        MySQL & Workbench
    </a> 
  - <a href="https://www.youtube.com/watch?v=QSATSrXuDIM" target="_blank"> 
        Pyhton & Visual Studio Code
    </a> 
- Verificar que se hallan instalado correctamente✅ MySQl y Python:
  - Ejecutar los siguientes comandos en una nueva <a href="https://www.downloadsource.es/uploaded/News%20July%202015/Simbolo%20del%20sistema%20Como%20administrador/simbolo%20del%20sistema%20Windows%207.jpg" target="_blank">terminal</a>:
    ```bash
        mysql --version
        py --version
        py -m pip install flask 
        py -m pip install --upgrade pip
        py -m pip install flask_sqlalchemy
        py -m pip install pymysql
    ``` 

### :white_check_mark: `Descargar proyecto`:inbox_tray:
- [Descargar proyecto](https://github.com/manita02/Good-Vibes-Blog/archive/refs/heads/main.zip):anger:


### :white_check_mark: `Crear Base de Datos`:wrench: 
- Abrir Workbench y entrar en Local Instance MySQL💽
- <a href="https://www.youtube.com/watch?v=aoEoOFgneJE" target="_blank"> Crear la base de datos, ponerle un nombre.</a> ⚠️ IMPORTANTE NO AGREGARLE TABLAS A LA BD, tiene que estar VACÍA ⚠️  


### :white_check_mark: `Configurar el archivo configuracion.py`:nut_and_bolt:
- Abrir Workbench📀
- En Local Instance de MySQL chequear el puerto, el nombre de usuario y su contraseña para luego colocarlos en el archivo configuracion.py según corresponda🧑‍💻
- Abrir la carpeta📁 donde se descargó anteriormente el proyecto con el Visual Studio Code
- Buscar el archivo "configuracion.py"
  <section align="center">
    <img src="https://imgfz.com/i/pAhwoNX.jpeg" alt="conexionBD">
  </section>
- Donde dice "database name" hay que poner el nombre de la base de datos creada anteriormente :link:
- Donde dice "port" hay que colocar el puerto de conexión 📈
- Donde dice "root" hay que poner el nombre de usuario con el que se conectará a la BD. Si tenemos un usuario con diferente nombre al de root, modificarlo y escribir el nombre que corresponda:bangbang: 
- Escribir la contraseña del usuario donde dice "password" 🔐
    

### :white_check_mark: `Ejecutar el proyecto`:rocket:
- Abrir la carpeta📁 donde se encuentra el proyecto con Visual Studio Code
- Abrir una nueva <a href="https://damiandeluca.com.ar/como-usar-la-terminal-integrada-de-visual-studio-code" target="_blank">terminal💾</a>
- Ejecutar los siguientes comandos: 
  - Activar el entorno: 
    ```bash
        env\Scripts\activate
    ```
  - Ejecutar la aplicación♻️:
    ```bash
        py main.py
    ```
    <section align="center">
      <img src="https://i.ibb.co/k6j6mbB/corriendo.jpg" alt="running">
    </section>

 - Abrir su navegador de Internet🌐 y en el buscador🔎 pegar el siguiente enlace: 
    ```
      http://127.0.0.1:5000
    ```


## Funcionalidades :clipboard:
### :red_circle: `Sin cuenta de usuario (sin iniciar sesión)`
- Visualizar información de diferentes publicaciones realizadas por usuarios🕵️. 
  <section align="center">
    <img src="https://i.pinimg.com/564x/3c/e8/1f/3ce81f802820c8415bfe04415a0bde3a.jpg">
  </section>
### :large_blue_circle: `Con cuenta de usuario creada (con sesión activa y logeado en el sitio) `
- El usuario podrá agregar, editar o eliminar sus propias publicaciones en el blog🖥️. 
- Cada usuario podrá editar✍️ su información de perfil seleccionando su foto de perfil en el ménu de navegación. 
- También podrá eliminar❌ su cuenta de usuario.

## Tecnologías utilizadas :hammer:
<section align="center">
<a href="https://www.python.org/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" alt="python" width="90" height="90"/> </a> 👀
<a href="https://www.ionos.es/digitalguide/servidores/know-how/que-es-mysql/#:~:text=MySQL%20es%20un%20sistema%20de,por%20ejemplo%2C%20WordPress%20y%20TYPO3." target="_blank"> <img class="img" src="https://styles.redditmedia.com/t5_2qm6k/styles/communityIcon_dhjr6guc03x51.png" alt="mysql" width="90" height="90"/> </a> 👀
<a href="https://flask.palletsprojects.com/en/3.0.x/installation/#install-flask" target="_blank"> <img class="img" src="https://static-00.iconduck.com/assets.00/flask-icon-2048x1826-nxzeqh6a.png" alt="flask" width="90" height="90"/> </a> 👀
<a href="https://www.sqlalchemy.org/" target="_blank"> <img class="img" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/SQLAlchemy.svg/768px-SQLAlchemy.svg.png" alt="sqlAlchemy" width="150" height="90"/> </a> 👀
<a href="https://developer.mozilla.org/es/docs/Web/HTML" target="_blank"> <img src="https://cdn-icons-png.flaticon.com/128/5968/5968267.png" alt="html" width="90" height="80"/> </a> 👀
<a href="https://developer.mozilla.org/es/docs/Web/CSS" target="_blank"> <img class="img" src="https://cdn-icons-png.flaticon.com/128/5968/5968242.png" alt="css" width="90" height="80"/> </a> 
</section>


## Autor :black_nib:
| [<img src="https://i.pinimg.com/564x/59/de/e4/59dee44e1eb2dbf9bbb6ef1c2c396e0b.jpg" width=115><br><sub>Ana Lucia Juarez</sub>](https://github.com/manita02) | 
| :---: |
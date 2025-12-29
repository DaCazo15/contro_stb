<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="./assets/logo.png" alt="Project logo"></a>
</p>

<h3 align="center">Control Remoto</h3>

---

<p align="center"> Aplicación Python para controlar un carrito mediante una interfaz gráfica y conexión serial con Arduino.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

Este proyecto es una aplicación para controlar un carrito, desarrollada en Python. Utiliza una interfaz gráfica creada con CustomTkinter para enviar comandos de navegación (arriba, abajo, izquierda, derecha) y permite cargar códigos de acceso. La comunicación se realiza a través de una conexión serial con un dispositivo Arduino.

## 🏁 Getting Started <a name = "getting_started"></a>

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para desarrollo y pruebas.

### Prerequisites

Necesitas tener instalado Python 3.6 o superior. También se requieren las siguientes bibliotecas:

- pyserial
- customtkinter
- Pillow (PIL)

### Installing

1. Instala las dependencias:
```
pip install pyserial customtkinter pillow
```

2. Asegúrate de que tu Arduino esté conectado y no use el puerto COM3 (el código lo excluye automáticamente).

3. Ejecuta la aplicación:
```
python control.py
```

## 🎈 Usage <a name="usage"></a>

1. Ejecuta `control.py` para abrir la interfaz gráfica.
2. Usa los botones de navegación para enviar comandos al Robot.
4. Ingresa un código de acceso en el campo correspondiente y presiona "Cargar" para enviarlo.

La aplicación se conecta automáticamente al primer puerto serial disponible (excluyendo COM3).

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Lenguaje de programación
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Framework para interfaz gráfica
- [Pillow](https://pillow.readthedocs.io/en/stable/) - Procesamiento de imágenes
- [PySerial](https://pythonhosted.org/pyserial/) - Comunicación serial

## ✍️ Authors <a name = "authors"></a>

- [@DaCazo15](https://github.com/DaCazo15) - Desarrollo inicial

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Inspiración en proyectos de control remoto con Python y Arduino
- Iconos y recursos utilizados en la interfaz

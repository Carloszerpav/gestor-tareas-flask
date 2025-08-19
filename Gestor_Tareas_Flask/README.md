# 📝 Gestor de Tareas con Flask

Una aplicación web moderna y elegante para gestionar tareas diarias, desarrollada con Flask y diseñada con un tema oscuro profesional.

## ✨ Características

### 🎯 Funcionalidades Principales
- **Gestión completa de tareas** - Crear, editar, completar y eliminar tareas
- **Sistema de horarios** - Asignar fechas y horas específicas a cada tarea
- **Interfaz moderna** - Diseño oscuro con Material Design
- **Responsive** - Funciona perfectamente en dispositivos móviles y de escritorio
- **Estadísticas en tiempo real** - Seguimiento del progreso con métricas detalladas

### 🕐 Sistema de Horarios
- **Fechas personalizables** - Selecciona la fecha para cada tarea
- **Horarios específicos** - Asigna horas exactas para mejor organización
- **Información de completado** - Registra cuándo se completó cada tarea
- **Tareas vencidas** - Identifica automáticamente tareas con fecha pasada

### 📊 Estadísticas Avanzadas
- **Total de tareas** - Conteo general de todas las tareas
- **Tareas completadas** - Seguimiento del progreso
- **Tareas pendientes** - Tareas por realizar
- **Tareas para hoy** - Tareas programadas para el día actual
- **Tareas vencidas** - Tareas pendientes con fecha pasada
- **Barra de progreso** - Visualización del avance general

### 🎨 Diseño y UX
- **Modo oscuro** - Tema elegante y profesional
- **Animaciones suaves** - Transiciones fluidas y modernas
- **Validación de formularios** - Verificación en tiempo real
- **Confirmaciones** - Diálogos de confirmación para acciones importantes
- **Auto-focus** - Enfoque automático en campos de entrada

## 🚀 Instalación

### Prerrequisitos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/gestor-tareas-flask.git
   cd gestor-tareas-flask
   ```

2. **Crea un entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

3. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta la aplicación**
   ```bash
   python app.py
   ```

5. **Abre tu navegador**
   ```
   http://localhost:5000
   ```

## 📁 Estructura del Proyecto

```
gestor-tareas-flask/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Documentación del proyecto
├── templates/            # Plantillas HTML
│   └── index.html        # Plantilla principal
├── static/               # Archivos estáticos
│   ├── css/              # Hojas de estilo
│   └── js/               # JavaScript
└── .gitignore           # Archivos a ignorar en Git
```

## 🛠️ Tecnologías Utilizadas

### Backend
- **Flask** - Framework web ligero y flexible
- **Python** - Lenguaje de programación principal
- **datetime** - Manejo de fechas y horas

### Frontend
- **HTML5** - Estructura semántica
- **CSS3** - Estilos modernos con Grid y Flexbox
- **JavaScript** - Interactividad y validaciones
- **Material Design** - Principios de diseño

### Características Técnicas
- **Responsive Design** - Adaptable a cualquier dispositivo
- **Progressive Enhancement** - Funciona sin JavaScript
- **Accessibility** - Diseño accesible
- **Performance** - Optimizado para velocidad

## 📖 Uso de la Aplicación

### Agregar una Nueva Tarea
1. Escribe el texto de la tarea en el campo principal
2. Selecciona la fecha (opcional - por defecto es hoy)
3. Selecciona la hora (opcional - por defecto es la hora actual)
4. Haz clic en "Agregar Tarea"

### Gestionar Tareas Existentes
- **Completar**: Haz clic en el botón "Completar" para marcar como terminada
- **Eliminar**: Haz clic en "Eliminar" y confirma la acción
- **Ver detalles**: Cada tarea muestra su fecha, hora y estado

### Estadísticas
- **Panel de estadísticas**: En la parte inferior de la página
- **Barra de progreso**: Visualización del avance general
- **Métricas detalladas**: Conteos específicos por categoría

## 🔧 Personalización

### Modificar el Tema
Los estilos están en el archivo `templates/index.html`. Puedes modificar:
- Colores del tema oscuro
- Tipografías
- Espaciados y tamaños
- Animaciones

### Agregar Funcionalidades
El código está organizado en funciones modulares:
- `agregar_tarea()` - Lógica para agregar tareas
- `completar_tarea()` - Lógica para completar tareas
- `obtener_estadisticas()` - Cálculo de métricas
- `formatear_fecha()` - Formateo de fechas

## 🐛 Solución de Problemas

### Error: "No module named 'flask'"
```bash
pip install -r requirements.txt
```

### Error: "Port already in use"
Cambia el puerto en `app.py`:
```python
app.run(debug=True, port=5001)
```

### Problemas de permisos (Linux/macOS)
```bash
chmod +x app.py
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Tu Nombre**
- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- Email: tu-email@ejemplo.com

## 🙏 Agradecimientos

- Flask por el excelente framework web
- La comunidad de desarrolladores por las inspiraciones
- Material Design por los principios de diseño

---

⭐ **Si te gusta este proyecto, ¡dale una estrella en GitHub!**

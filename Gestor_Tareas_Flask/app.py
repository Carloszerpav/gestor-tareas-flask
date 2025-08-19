from flask import Flask, request, redirect, url_for, render_template
from datetime import datetime

app = Flask(__name__)

# ========================================
# GESTIÓN DE TAREAS - FUNCIONES GLOBALES
# ========================================

# Lista global de tareas
tareas = []
contador_id = 1

def agregar_tarea(texto, fecha=None, hora=None):
    """
    Agrega una nueva tarea a la lista global
    Args:
        texto (str): El texto de la tarea
        fecha (str): Fecha de la tarea (opcional)
        hora (str): Hora de la tarea (opcional)
    Returns:
        dict: La tarea creada con id, texto, estado y horarios
    """
    global contador_id
    
    # Obtener fecha y hora actual si no se proporcionan
    ahora = datetime.now()
    fecha_creacion = ahora.strftime("%Y-%m-%d")
    hora_creacion = ahora.strftime("%H:%M")
    
    nueva_tarea = {
        'id': contador_id,
        'texto': texto.strip(),
        'hecho': False,
        'fecha_creacion': fecha_creacion,
        'hora_creacion': hora_creacion,
        'fecha_tarea': fecha if fecha else fecha_creacion,
        'hora_tarea': hora if hora else hora_creacion
    }
    
    tareas.append(nueva_tarea)
    contador_id += 1
    
    return nueva_tarea

def completar_tarea(id):
    """
    Marca una tarea como completada
    Args:
        id (int): El ID de la tarea a completar
    Returns:
        bool: True si se encontró y completó la tarea, False si no existe
    """
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['hecho'] = True
            tarea['fecha_completada'] = datetime.now().strftime("%Y-%m-%d")
            tarea['hora_completada'] = datetime.now().strftime("%H:%M")
            return True
    return False

def eliminar_tarea(id):
    """
    Elimina una tarea de la lista
    Args:
        id (int): El ID de la tarea a eliminar
    Returns:
        bool: True si se encontró y eliminó la tarea, False si no existe
    """
    global tareas
    tareas_original = len(tareas)
    tareas = [tarea for tarea in tareas if tarea['id'] != id]
    return len(tareas) < tareas_original

def obtener_tarea(id):
    """
    Obtiene una tarea específica por ID
    Args:
        id (int): El ID de la tarea
    Returns:
        dict: La tarea encontrada o None si no existe
    """
    for tarea in tareas:
        if tarea['id'] == id:
            return tarea
    return None

def obtener_estadisticas():
    """
    Obtiene estadísticas de las tareas
    Returns:
        dict: Diccionario con estadísticas
    """
    total = len(tareas)
    completadas = sum(1 for tarea in tareas if tarea['hecho'])
    pendientes = total - completadas
    
    # Estadísticas por fecha
    tareas_hoy = sum(1 for tarea in tareas if tarea['fecha_tarea'] == datetime.now().strftime("%Y-%m-%d"))
    tareas_vencidas = sum(1 for tarea in tareas 
                         if not tarea['hecho'] and tarea['fecha_tarea'] < datetime.now().strftime("%Y-%m-%d"))
    
    return {
        'total': total,
        'completadas': completadas,
        'pendientes': pendientes,
        'hoy': tareas_hoy,
        'vencidas': tareas_vencidas
    }

def ordenar_tareas():
    """
    Ordena las tareas: incompletas primero, luego completadas
    Returns:
        list: Lista de tareas ordenadas
    """
    return sorted(tareas, key=lambda t: (t['hecho'], t['fecha_tarea'], t['hora_tarea']))

def formatear_fecha(fecha_str):
    """
    Formatea una fecha para mostrar de manera amigable
    Args:
        fecha_str (str): Fecha en formato YYYY-MM-DD
    Returns:
        str: Fecha formateada
    """
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        hoy = datetime.now().date()
        ayer = hoy.replace(day=hoy.day - 1)
        
        if fecha.date() == hoy:
            return "Hoy"
        elif fecha.date() == ayer:
            return "Ayer"
        else:
            return fecha.strftime("%d/%m/%Y")
    except:
        return fecha_str

def formatear_hora(hora_str):
    """
    Formatea una hora para mostrar de manera amigable
    Args:
        hora_str (str): Hora en formato HH:MM
    Returns:
        str: Hora formateada
    """
    try:
        hora = datetime.strptime(hora_str, "%H:%M")
        return hora.strftime("%I:%M %p")  # Formato 12 horas con AM/PM
    except:
        return hora_str

# ========================================
# RUTAS DE FLASK OPTIMIZADAS
# ========================================

@app.route('/')
def index():
    """
    Ruta principal optimizada: muestra tareas ordenadas
    - Incompletas primero, luego completadas
    - Estadísticas en tiempo real
    """
    tareas_ordenadas = ordenar_tareas()
    stats = obtener_estadisticas()
    
    # Obtener fecha y hora actual para los campos del formulario
    ahora = datetime.now()
    today = ahora.strftime("%Y-%m-%d")
    now = ahora.strftime("%H:%M")
    
    return render_template('index.html', 
                         tareas=tareas_ordenadas, 
                         stats=stats,
                         formatear_fecha=formatear_fecha,
                         formatear_hora=formatear_hora,
                         today=today,
                         now=now)

@app.route('/agregar', methods=['POST'])
def agregar():
    """
    Ruta optimizada para agregar tareas
    - Validación de entrada
    - Manejo de errores
    - Redirección eficiente
    """
    texto_tarea = request.form.get('texto_tarea', '').strip()
    fecha_tarea = request.form.get('fecha_tarea', '').strip()
    hora_tarea = request.form.get('hora_tarea', '').strip()
    
    if texto_tarea and len(texto_tarea) <= 100:
        nueva_tarea = agregar_tarea(texto_tarea, fecha_tarea, hora_tarea)
        print(f"✅ Tarea agregada: ID={nueva_tarea['id']}, Texto='{nueva_tarea['texto']}', Fecha={nueva_tarea['fecha_tarea']}, Hora={nueva_tarea['hora_tarea']}")
    else:
        print(f"❌ Tarea no válida: '{texto_tarea}'")
    
    return redirect('/')

@app.route('/completar/<int:id>')
def completar(id):
    """
    Ruta optimizada para completar tareas
    - Validación de ID
    - Feedback en consola
    - Redirección directa
    """
    if completar_tarea(id):
        print(f"✅ Tarea {id} marcada como completada")
    else:
        print(f"❌ Tarea {id} no encontrada")
    
    return redirect('/')

@app.route('/eliminar/<int:id>')
def eliminar(id):
    """
    Ruta optimizada para eliminar tareas
    - Validación de ID
    - Feedback en consola
    - Redirección directa
    """
    if eliminar_tarea(id):
        print(f"🗑️ Tarea {id} eliminada")
    else:
        print(f"❌ Tarea {id} no encontrada para eliminar")
    
    return redirect('/')

@app.route('/toggle/<int:id>')
def toggle(id):
    """
    Ruta para alternar estado de tareas
    """
    tarea = obtener_tarea(id)
    if tarea:
        tarea['hecho'] = not tarea['hecho']
        if tarea['hecho']:
            tarea['fecha_completada'] = datetime.now().strftime("%Y-%m-%d")
            tarea['hora_completada'] = datetime.now().strftime("%H:%M")
        else:
            tarea.pop('fecha_completada', None)
            tarea.pop('hora_completada', None)
        
        estado = "completada" if tarea['hecho'] else "pendiente"
        print(f"🔄 Tarea {id} marcada como {estado}")
    
    return redirect('/')

# ========================================
# EJECUCIÓN PRINCIPAL
# ========================================

if __name__ == '__main__':
    print("🚀 Iniciando aplicación optimizada de Gestión de Tareas...")
    print("📱 Abre tu navegador en: http://localhost:5000")
    print("✨ Características implementadas:")
    print("   - Plantilla HTML separada y organizada")
    print("   - Modo oscuro con Material Design")
    print("   - Ordenamiento automático de tareas")
    print("   - Validación de formularios")
    print("   - Interfaz responsive y moderna")
    print("   - Barra de progreso visual")
    print("   - Confirmación para eliminar")
    print("   - Auto-focus en formularios")
    print("   - Animaciones suaves")
    print("   - 🕐 SISTEMA DE HORARIOS Y FECHAS")
    print("📋 Funciones globales disponibles:")
    print("   - agregar_tarea(texto, fecha, hora)")
    print("   - completar_tarea(id)")
    print("   - ordenar_tareas()")
    print("   - obtener_estadisticas()")
    print("   - formatear_fecha(fecha)")
    print("   - formatear_hora(hora)")
    print("📁 Estructura de archivos:")
    print("   - prueba.py (aplicación Flask)")
    print("   - templates/index.html (plantilla)")
    app.run(debug=True)





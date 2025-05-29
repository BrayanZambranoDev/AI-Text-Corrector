# AI Text Corrector - Documentación Técnica

## Descripción del Sistema

El Corrector de Texto Automatizado es una aplicación que combina técnicas de procesamiento de lenguaje natural con modelos de IA para ofrecer corrección ortográfica y gramatical en tiempo real mientras el usuario escribe.

## Requisitos Técnicos

### Dependencias principales

* Python 3.10 o superior
* Bibliotecas esenciales (instalables via pip):

  ```bash
  pip install pyautogui pynput pyspellchecker nltk openai python-dotenv mysql-client
  ```

### Configuración de entorno

1. Crear archivo `.env` en el directorio raíz:

   ```ini
   OPENAI_API_KEY=su_clave_api_aqui
   ```
2. Descargar recursos de lenguaje para NLTK:

   ```bash
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/BrayanZambranoDev/AI-Text-Corrector.git
   cd AI-Text-Corrector
   ```
2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Arquitectura del Sistema

### Componentes principales

1. **Módulo de Captura de Teclado**: Utiliza `pynput` para detectar pulsaciones.
2. **Corrector Ortográfico**: Basado en `pyspellchecker` con diccionario en español.
3. **Motor Gramatical**: Integración con API de OpenAI (configurable mediante `python-dotenv`).
4. **Interfaz de Sistema**: `pyautogui` para simular escritura y mostrar correcciones.
5. **Persistencia**: Conexión opcional a MySQL para almacenamiento de estadísticas.

### Flujo de trabajo

1. Captura de texto mediante el listener de teclado.
2. Procesamiento en capas:

   * Corrección ortográfica básica.
   * Mejora contextual con llamadas a OpenAI.
3. Escritura automatizada de texto corregido al usuario.

## Configuración Avanzada

### Variables de entorno

| Variable         | Descripción                    | Ejemplo            |
| ---------------- | ------------------------------ | ------------------ |
| `OPENAI_API_KEY` | Clave para API de OpenAI       | `sk-...`           |
| `OPENAI_ENGINE`  | Modelo de OpenAI a utilizar    | `text-davinci-003` |
| `MYSQL_HOST`     | Host de la base de datos MySQL | `localhost`        |
| `MYSQL_USER`     | Usuario de la base de datos    | `root`             |
| `MYSQL_PASSWORD` | Contraseña de MySQL            | `password`         |
| `MYSQL_DATABASE` | Nombre de la base de datos     | `corrector_db`     |

### Parámetros ajustables

```python
# En core del script:
palabras_correctas = {"términos", "específicos"}    # Diccionario personalizado
stop_words = set(stopwords.words('spanish'))           # Palabras vacías
OPENAI_ENGINE = os.getenv('OPENAI_ENGINE', 'text-davinci-003')
```

## Uso del Sistema

### Iniciar la aplicación

```bash
python corrector.py
```

### Atajos de teclado

* **Espacio/Enter**: Activa la corrección del texto acumulado.
* **Backspace**: Elimina el último carácter del buffer.

## Consideraciones de Seguridad

1. **Manejo de API Keys**:

   * Nunca incluir claves directamente en el código.
   * Utilizar siempre variables de entorno.
   * Revocar claves comprometidas inmediatamente.

2. **Privacidad de datos**:

   * El texto procesado se envía a los servidores de OpenAI.
   * No utilizar con información sensible o confidencial.

## Limitaciones Conocidas

1. Dependencia de conexión a Internet para funciones de IA.
2. Latencia en correcciones complejas.
3. Soporte limitado para lenguaje técnico o especializado.

## Roadmap de Desarrollo

1. Implementación de caché local para correcciones frecuentes.
2. Soporte para múltiples idiomas.
3. Versión como servicio en segundo plano (daemon).
4. Integración con editores de texto populares (VSCode, Sublime, etc.).

## Soporte Técnico

Para reportar problemas o solicitar características:

1. Crear un issue en el repositorio de GitHub.
2. Incluir detalles:

   * Versión de Python.
   * Sistema operativo.
   * Pasos para reproducir el error.
   * Mensajes de error completos.

## Licencia

Este proyecto se distribuye bajo la **licencia MIT**. El uso de la API de OpenAI está sujeto a los Términos de Servicio de OpenAI.


# Prácticas de Sistemas Inteligentes — curso 2026-27

Universidad de Castilla-La Mancha · E.S. de Ingeniería Informática de Albacete
Grado en Ingeniería Informática, 3.º curso

Las prácticas se publican **una a una, cuando empieza cada una**. Todas se instalan en la
misma carpeta, `SSII-practicas-26-27/`, que va creciendo a lo largo del curso. Este README
describe la carpeta **completa**, tal y como quedará al final: si todavía no ves alguna de
las carpetas que aparecen abajo, es que esa práctica aún no se ha publicado.

## Estructura de la carpeta de prácticas

```
SSII-practicas-26-27/
├── ssii_estacion/      Paquete de apoyo, común a las tres prácticas.
│                       Lo da el profesorado y NO se modifica
├── catalogo/           Las instancias de cada práctica, en JSON
│   ├── pr1/            Búsqueda en espacio de estados
│   ├── pr2/            Aprendizaje por refuerzo
│   └── pr3/            Metaheurísticas, con las matrices de distancias
├── PR1/                Búsqueda en espacio de estados
│   ├── Lab1_26-27_ES.ipynb · Lab1_26-27_EN.ipynb
│   └── pruebas/        Pruebas públicas
├── PR2/                Aprendizaje por refuerzo (misma estructura)
├── PR3/                Metaheurísticas (misma estructura)
├── formato-json.md     Formato de instancias y soluciones (json-format-EN.md en inglés)
├── README.md · README-EN.md
└── requirements.txt
```

De cada práctica tienes el cuaderno en **español** (`_ES`) y en **inglés** (`_EN`): usa el
de tu grupo. Son el mismo enunciado.

## La primera vez

Descomprime el `.zip` donde quieras y trabaja siempre dentro de la carpeta que se crea:
las rutas de los cuadernos son relativas y dan por hecho esta estructura. Necesitas
Python 3.10 o posterior. Desde la carpeta `SSII-practicas-26-27/`:

```bash
python3 -m venv .venv
source .venv/bin/activate        # en Windows:  .venv\Scripts\activate
pip install -r requirements.txt
```

Y para abrir el cuaderno de la práctica:

```bash
cd PR1
jupyter notebook Lab1_26-27_ES.ipynb
```

También puedes usar VS Code, PyCharm o Colab, pero si trabajas en Colab tendrás que subir
la carpeta entera para que el cuaderno encuentre el paquete y el catálogo.

## Cuando se publique una práctica nueva

El `.zip` de cada práctica nueva trae su carpeta `PRn/`, su parte del catálogo y la última
versión del paquete `ssii_estacion/`. **No trae las prácticas anteriores**, así que no
puede pisar tu trabajo. Para incorporarla:

1. Descomprime el `.zip` en un sitio **aparte** (no encima de tu carpeta: según el sistema,
   te crearía una carpeta duplicada o te preguntaría por cada fichero).
2. Copia en tu `SSII-practicas-26-27/` la carpeta `PRn/` nueva y la carpeta
   `catalogo/prn/`.
3. **Sustituye** tu `ssii_estacion/` por la nueva, y también los `README` y
   `requirements.txt`. Como el paquete no se modifica, no pierdes nada.
4. Si `requirements.txt` ha cambiado, vuelve a ejecutar `pip install -r requirements.txt`
   con tu entorno activado.

## Las pruebas públicas

Cada práctica trae una batería de pruebas que puedes ejecutar tú, tantas veces como
quieras, para saber si tu implementación cumple lo que se espera. Desde la carpeta
`SSII-practicas-26-27/`:

```bash
python3 -m pytest PR1/pruebas -q          # y lo mismo con PR2 y PR3
```

Por defecto prueban el cuaderno en español; para probar el inglés:

```bash
SSII_ENTREGA=PR1/Lab1_26-27_EN.ipynb python3 -m pytest PR1/pruebas -q
```

No hace falta que el cuaderno esté ejecutado: de él se toman solo las celdas que definen
funciones. **Pasarlas es el mínimo, no la nota**: en la corrección se ejecutan además
otras pruebas que no ves. En el `README.md` de cada carpeta `pruebas/` tienes el detalle.

## Qué se entrega

El cuaderno completado y los ficheros JSON de solución que genera, tal y como explica la
sección de entrega de cada enunciado.

## Problemas frecuentes

* **`ModuleNotFoundError: ssii_estacion`**: estás ejecutando el cuaderno desde otra
  carpeta. Ábrelo desde `PRn/`, que es donde la primera celda añade la carpeta superior al
  `sys.path`.
* **Resultados que no cuadran tras editar una celda**: reinicia el kernel y ejecuta todo
  de arriba abajo (*Kernel → Restart & Run All*). La mitad de los errores raros son estado
  viejo.
* **No se ven las figuras**: comprueba que has instalado `matplotlib` en el entorno desde
  el que arrancas Jupyter.

Cualquier duda, a las tutorías o al foro de la asignatura en Campus Virtual.

Proyecto Pluviometría - Asesor de Riego Inteligente
Este proyecto es una aplicación web creada con Streamlit que funciona como un asesor agronómico digital. Su objetivo principal es responder a la pregunta: ¿cuánto, cuándo y dónde regar?

La aplicación calcula el balance hídrico del suelo y genera recomendaciones de riego precisas, considerando datos clave como la precipitación, las necesidades del cultivo y el pronóstico del tiempo.

🚀 Cómo ejecutar el proyecto localmente
Clonar el repositorio:

git clone <URL-de-tu-repositorio-github>
cd pluviometria

Crear un entorno virtual (recomendado):

python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

Instalar las dependencias:

pip install -r requirements.txt

Ejecutar la aplicación Streamlit:

streamlit run app.py

Abre tu navegador y ve a http://localhost:8501.

🧪 Cómo ejecutar las pruebas
Para asegurar que la lógica de negocio funciona correctamente, puedes ejecutar las pruebas unitarias con pytest:

pytest

📂 Estructura del Proyecto
pluviometria/
├── .gitignore
├── README.md
├── app.py                  # Archivo principal de la aplicación Streamlit
├── requirements.txt        # Dependencias de Python
├── src/
│   ├── __init__.py
│   └── core/
│       ├── __init__.py
│       ├── balance_hidrico.py  # Lógica para el cálculo del balance
│       └── recomendador.py     # Lógica para generar recomendaciones
└── tests/
    ├── test_balance_hidrico.py
    └── test_recomendador.py

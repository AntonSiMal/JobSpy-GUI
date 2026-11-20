<h1 align="center">
  <a href="https://github.com/speedyapply/JobSpy"><img src="https://github.com/user-attachments/assets/dcb90340-9469-4808-bc51-868e59a000e0" alt="JobSpy" width="320"></a>
</h1>

<p align="center">
  <a href="https://pypi.org/project/python-jobspy/"><img src="https://img.shields.io/pypi/v/python-jobspy" alt="PyPI version"></a>
  <a href="https://pypi.org/project/python-jobspy/"><img src="https://img.shields.io/pypi/pyversions/python-jobspy" alt="Python versions"></a>
  <a href="https://pepy.tech/projects/python-jobspy"><img src="https://static.pepy.tech/badge/python-jobspy/month" alt="Downloads per month"></a>
  <a href="https://github.com/speedyapply/JobSpy/actions/workflows/ci.yml"><img src="https://github.com/speedyapply/JobSpy/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI"></a>
  <a href="https://github.com/speedyapply/JobSpy/blob/main/LICENSE"><img src="https://img.shields.io/pypi/l/python-jobspy" alt="License: MIT"></a>
  <a href="https://discord.gg/v7WdHnrNcN"><img src="https://img.shields.io/discord/1227411661221269565?label=discord&logo=discord&logoColor=white" alt="Discord"></a>
</p>

**JobSpy** es una librería de *scraping* de empleos que reúne ofertas de bolsas de trabajo populares en una sola herramienta:

- Extrae vacantes de **LinkedIn**, **Indeed**, **ZipRecruiter**, **Glassdoor**, **SEEK** (con **JobStreet** y **Jobsdb**), **Naukri**, **HelloWork**, **Bayt** y **BDJobs** de forma concurrente
- Consolida las ofertas laborales en un *DataFrame*
- Soporte de *proxies* para evitar bloqueos

<p align="center">
  <a href="https://github.com/speedyapply/JobSpy"><img src="https://github.com/cullenwatson/JobSpy/assets/78247585/ec7ef355-05f6-4fd3-8161-a817e31c5c57" alt="Demostración de JobSpy"></a>
</p>

## Instalación

```bash
pip install -U python-jobspy

```

*Se requiere Python versión >= [3.10*](https://www.python.org/downloads/release/python-3100/)

## Uso

```python
from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["linkedin", "indeed", "zip_recruiter", "glassdoor"],  # también "seek", "naukri", "hellowork", "bayt", "bdjobs"
    search_term="software engineer",
    location="San Francisco, CA",
    results_wanted=20,
    hours_old=72,
    country_indeed="USA",
    # fetch_description=True,  # lee la página de cada vacante en portales cuyos resultados no incluyen descripción (más lento)
    # proxies=["user:pass@host:port", "localhost"],
)
print(f"Se encontraron {len(jobs)} vacantes")
print(jobs.head())
jobs.to_csv("jobs.csv", index=False)

```

## Salida

```text
SITE           TITLE                             COMPANY           LOCATION                JOB_TYPE  INTERVAL  MIN_AMOUNT  MAX_AMOUNT  JOB_URL                                            DESCRIPTION
indeed         Software Engineer                 AMERICAN SYSTEMS  Arlington, VA, USA      None      yearly    150000      200000      [https://www.indeed.com/viewjob?jk=5e409e577046](https://www.indeed.com/viewjob?jk=5e409e577046)...  THIS POSITION COMES WITH A 10K SIGNING BONUS!...
indeed         Senior Software Engineer          TherapyNotes.com  Philadelphia, PA, USA   fulltime  yearly    110000      135000      [https://www.indeed.com/viewjob?jk=da39574a40cb](https://www.indeed.com/viewjob?jk=da39574a40cb)...  About Us TherapyNotes is the national leader i...
linkedin       Software Engineer - Early Career  Lockheed Martin   Sunnyvale, CA, USA      fulltime  yearly    None        None        [https://www.linkedin.com/jobs/view/3693012711](https://www.linkedin.com/jobs/view/3693012711)      Description:By bringing together people that u...
linkedin       Full-Stack Software Engineer      Rain              New York, NY, USA       fulltime  yearly    None        None        [https://www.linkedin.com/jobs/view/3696158877](https://www.linkedin.com/jobs/view/3696158877)      Rain’s mission is to create the fastest and ea...
zip_recruiter  Software Engineer - New Grad      ZipRecruiter      Santa Monica, CA, USA   fulltime  yearly    130000      150000      [https://www.ziprecruiter.com/jobs/ziprecruiter](https://www.ziprecruiter.com/jobs/ziprecruiter)...  We offer a hybrid work environment. Most US-ba...
zip_recruiter  Software Developer                TEKsystems        Phoenix, AZ, USA        fulltime  hourly    65          75          [https://www.ziprecruiter.com/jobs/teksystems-0](https://www.ziprecruiter.com/jobs/teksystems-0)...  Top Skills' Details• 6 years of Java developme...

```

## Interfaz gráfica y lanzadores (`app.py`, `Linux-run.sh`, `Windows-run.bat`)

Este repositorio incluye una interfaz gráfica interactiva en **Streamlit** (`app.py`) junto con *scripts* de arranque que preparan el entorno virtual, instalan dependencias y lanzan la aplicación:

* **`app.py`**: Interfaz web local para configurar portales, términos de búsqueda, ubicación, antigüedad, tipo de jornada, modo remoto, *proxies*, filtrar resultados, revisar errores/advertencias y descargar los datos en CSV.
* **`Linux-run.sh`**: *Script* para Linux que verifica `python3`, crea/reutiliza `.venv`, instala o actualiza `python-jobspy`, `streamlit` y `openpyxl`, y ejecuta `app.py`.
* **`Windows-run.bat`**: *Script* para Windows que localiza Python (`py -3` o `python`), crea/reutiliza `.venv`, instala o actualiza las dependencias y lanza `app.py`.

### Ejecución en Linux

```bash
chmod +x Linux-run.sh
./Linux-run.sh

```

### Ejecución en Windows

Haz doble clic en `Windows-run.bat` o ejecútalo desde terminal:

```bat
Windows-run.bat

```

## Línea de comandos

El paquete instala el comando `jobspy` con opciones equivalentes a los parámetros de `scrape_jobs()`; `jobspy -h` muestra las opciones disponibles, los campos de salida y los códigos de salida.

```bash
uv tool install python-jobspy

jobspy "software engineer" --site indeed,linkedin --location Chicago -n 20
jobspy nurse --site indeed,linkedin --hours-old 24 -o jobs.jsonl
jobspy "data analyst" --remote --fields title,company,job_url

```

## Servidor MCP

[`mcp-jobspy`](https://pypi.org/project/mcp-jobspy/) es un servidor MCP que se ejecuta con `uvx mcp-jobspy@latest`. Consulta [mcp/README.md](https://github.com/speedyapply/JobSpy/blob/main/mcp/README.md) para ver la configuración, herramientas y uso de *proxies*.

**Configuración estándar** compatible con la mayoría de los clientes:

```json
{
  "mcpServers": {
    "jobspy": {
      "command": "uvx",
      "args": ["mcp-jobspy@latest"]
    }
  }
}

```

## Parámetros de `scrape_jobs()`

```plaintext
Opcionales
├── site_name (list|str): 
|    linkedin, indeed, zip_recruiter, glassdoor, seek, naukri, hellowork, bayt, bdjobs, google
|    (por defecto son todos)
│
├── search_term (str)
|
├── google_search_term (str)
|     término de búsqueda para Google Jobs. Es el único parámetro para filtrar vacantes de Google.
│
├── location (str)
│
├── distance (int): 
|    en millas, por defecto 50
│
├── job_type (str): 
|    fulltime, parttime, contract, temporary, internship, perdiem, other, volunteer
│
├── proxies (list|str): 
|    en formato ['user:pass@host:port', 'localhost'], o un solo proxy como cadena
|    cada scraper rotará en round-robin entre los proxies
|    los proxies SOCKS en LinkedIn, Indeed y BDJobs requieren pip install "requests[socks]"
│
├── is_remote (bool)
│
├── results_wanted (int): 
|    cantidad de vacantes a obtener por cada sitio indicado en 'site_name'
│
├── easy_apply (bool): 
|    filtra vacantes alojadas directamente en la bolsa de empleo
│
├── user_agent (str): 
|    reemplaza el user agent por defecto si está desactualizado
│
├── description_format (str): 
|    markdown, html, plain (Formato de las descripciones. Por defecto es markdown.)
│
├── offset (int): 
|    omite esa cantidad de resultados (ej. 25 omite los primeros 25 y empieza en el 26)
│
├── hours_old (int): 
|    filtra vacantes según las horas transcurridas desde su publicación
|    (Glassdoor filtra por días completos, por lo que redondea hacia el siguiente día.)
│
├── verbose (int) {0, 1, 2}: 
|    Controla el nivel de detalle de los mensajes en consola
|    (0 muestra solo errores, 1 errores+advertencias, 2 todos los registros. Por defecto es 1.)
│
├── fetch_description (bool): 
|    para portales cuyos resultados iniciales no incluyen la descripción: consulta la página de cada
|    vacante para obtener descripción y otros detalles (ej. tipo de empleo). Sin esta opción quedan vacíos
|    en esos portales. Añade una petición por vacante, por lo que conviene usar proxies en búsquedas grandes
│
├── linkedin_fetch_description (bool): 
|    obsoleto; usar fetch_description (aún funciona; se eliminará en la versión 2.0)
│
├── linkedin_company_ids (list[int]): 
|    busca vacantes de LinkedIn para IDs de empresa específicos
|
├── country_indeed (str): 
|    elige el sitio del país en Indeed, Glassdoor y SEEK (por defecto es usa; ver nombres abajo)
|
├── enforce_annual_salary (bool): 
|    convierte los salarios a monto anual
|
├── ca_cert (str)
|    ruta al archivo de certificado CA para proxies

```

## Países compatibles para búsqueda de empleo

### LinkedIn

LinkedIn busca a nivel mundial. `location` acepta cualquier lugar.

### Indeed

Indeed busca en un país. `location` acepta una ubicación dentro de ese país, por ejemplo ciudad y estado.
`country_indeed` (por defecto `usa`) selecciona el país:

|  |  |  |  |
| --- | --- | --- | --- |
| Argentina | Australia | Austria | Bahrain |
| Belgium | Brazil | Canada | Chile |
| China | Colombia | Costa Rica | Czech Republic |
| Denmark | Ecuador | Egypt | Finland |
| France | Germany | Greece | Hong Kong |
| Hungary | India | Indonesia | Ireland |
| Israel | Italy | Japan | Kuwait |
| Luxembourg | Malaysia | Mexico | Morocco |
| Netherlands | New Zealand | Nigeria | Norway |
| Oman | Pakistan | Panama | Peru |
| Philippines | Poland | Portugal | Qatar |
| Romania | Saudi Arabia | Singapore | South Africa |
| South Korea | Spain | Sweden | Switzerland |
| Taiwan | Thailand | Turkey | UK |
| Ukraine | United Arab Emirates | Uruguay | USA |
| Venezuela | Vietnam |  |  |

### ZipRecruiter

ZipRecruiter busca en EE. UU. y Canadá. `location` acepta un lugar en cualquiera de ambos.

### Glassdoor

Glassdoor busca a nivel mundial. `location` acepta cualquier lugar, en cualquier país, por ejemplo `"Berlin"` o `"Vietnam"`.
`country_indeed` (por defecto `usa`) selecciona el sitio de Glassdoor; sin `location` busca en el país de ese sitio:

|  |  |  |  |
| --- | --- | --- | --- |
| Argentina | Australia | Austria | Belgium |
| Brazil | Canada | France | Germany |
| Hong Kong | India | Ireland | Italy |
| Mexico | Netherlands | New Zealand | Singapore |
| Spain | Switzerland | UK | USA |

### SEEK / JobStreet / Jobsdb

SEEK busca en un país. `location` acepta un suburbio, ciudad o región en ese país, por ejemplo `"Melbourne"` o `"Jakarta"`.
`country_indeed` selecciona el país; indícalo explícitamente, ya que el valor por defecto `usa` no forma parte de esta lista:

|  |  |  |  |
| --- | --- | --- | --- |
| Australia | Hong Kong | Indonesia | Malaysia |
| New Zealand | Philippines | Singapore | Thailand |

### Naukri

Naukri busca en India. `location` acepta una ciudad, por ejemplo `"Pune"`.

### HelloWork

HelloWork busca en Francia. `location` acepta una ciudad, código postal o región francesa, por ejemplo `"Lyon"`. La mayoría de las vacantes están publicadas en francés, por lo que buscar con términos en francés arroja más resultados.

### Bayt

Bayt busca a nivel mundial, con la mayor parte de sus ofertas en Medio Oriente e India. `location` acepta un país, o una ciudad junto con su país, por ejemplo `"Saudi Arabia"` o `"Dubai, UAE"`.

### BDJobs

BDJobs busca en Bangladés. `location` acepta una división o distrito, por ejemplo `"Dhaka"` o `"Chattogram Division"`.

## Notas

* Indeed es actualmente el *scraper* más estable y sin límite de tasa (*rate limiting*).
* El campo `date_posted` de Indeed corresponde al día en que la oferta se añadió a Indeed, la misma fecha que utiliza `hours_old` para filtrar.
* La mayoría de los *endpoints* de bolsas de empleo tienen un límite cercano a 1,000 vacantes por búsqueda.
* LinkedIn aplica límites de tasa (*429*) ante ráfagas de peticiones, los cuales suelen liberarse en cerca de un minuto. Usa *proxies* para búsquedas grandes.
* Glassdoor aplica límites de tasa por encima de aproximadamente 2 peticiones por segundo.

## Preguntas frecuentes

**P: ¿Cómo distingo un portal bloqueado de uno sin vacantes?**

**R:** Los fallos y opciones ignoradas se registran al ocurrir, y el atributo `attrs` del resultado conserva esos mensajes para que tu código pueda leerlos:

```py
jobs.attrs["errors"]    # {"linkedin": "response status code 429 (blocked: use a proxy)"}
jobs.attrs["warnings"]  # {"bdjobs": ["job_type internship isn't supported, ignoring it"]}

```

---

**P: ¿Por qué Indeed devuelve puestos poco relacionados?**

**R:** Indeed también busca dentro de la descripción.

* Usa `-` para excluir palabras
* Usa `""` para coincidencia exacta

Ejemplo de una buena consulta en Indeed

```py
search_term='"engineering intern" software summer (java OR python OR c++) 2025 -tax -marketing'

```

Esto busca en descripción o título y exige incluir `software`, `summer`, `2025`, alguno de los lenguajes, la frase exacta `engineering intern`, y excluir `tax` y `marketing`.

---

**P: ¿No obtengo resultados al usar `"google"`?**

**R:** Google Jobs no está disponible actualmente.

---

**P: ¿Recibiste el código de respuesta 429?**

**R:** El portal te bloqueó por enviar demasiadas peticiones. Todos los portales de empleo son estrictos con los bloqueos. Recomendamos:

* Esperar un tiempo entre extracciones (según el sitio).
* Probar el parámetro `proxies` para cambiar tu dirección IP.

---

## Esquema de `JobPost`

```plaintext
JobPost
├── id
├── site
├── job_url
├── job_url_direct
├── title
├── company
├── location
├── date_posted
├── job_type: fulltime, parttime, internship, contract, temporary, ...
├── salary_source: direct_data, description (parsed from posting), estimated (Glassdoor's own estimate)
├── interval: yearly, monthly, weekly, daily, hourly
├── min_amount
├── max_amount
├── currency
├── is_remote
├── job_level
├── job_function
├── listing_type
├── emails
├── description
├── company_industry
├── company_url
├── company_logo
├── company_url_direct
├── company_addresses
├── company_num_employees
├── company_revenue
├── company_description
├── skills
├── experience_range
├── company_rating
├── company_reviews_count
├── vacancy_count
└── work_from_home_type

```

Una columna queda vacía cuando la bolsa de empleo no proporciona ese dato.

```

```

import pandas as pd
import streamlit as st
from jobspy import scrape_jobs

st.set_page_config(page_title="JobSpy UI", layout="wide")
st.title("Buscador de Vacantes — JobSpy")

with st.sidebar:
    st.header("Parámetros de búsqueda")
    sites = st.multiselect(
        "Portales",
        ["indeed", "linkedin", "glassdoor", "zip_recruiter", "bayt", "naukri", "bdjobs", "hellowork", "seek"],
        default=["indeed", "linkedin"],
    )
    search_term = st.text_input("Puesto / Palabras clave", value="software engineer")
    location = st.text_input("Ubicación", value="Torreon, Coahuila, Mexico")
    country_indeed = st.text_input("País (Indeed / Glassdoor / SEEK)", value="Mexico")

    col1, col2 = st.columns(2)
    with col1:
        results_wanted = st.number_input("Resultados por sitio", min_value=1, max_value=200, value=20)
    with col2:
        hours_old = st.number_input("Antigüedad (horas)", min_value=1, max_value=720, value=72)

    job_type = st.selectbox(
        "Tipo de jornada",
        ["", "fulltime", "parttime", "contract", "temporary", "internship"],
    )
    is_remote = st.checkbox("Solo remoto", value=False)
    fetch_description = st.checkbox("Obtener descripción completa (más lento)", value=False)
    proxies_raw = st.text_area("Proxies (uno por línea, opcional)", placeholder="user:pass@host:port")

    run_btn = st.button("Buscar vacantes", type="primary", use_container_width=True)

if "jobs_df" not in st.session_state:
    st.session_state["jobs_df"] = None
    st.session_state["errors"] = {}
    st.session_state["warnings"] = {}

if run_btn:
    if not sites or not search_term.strip():
        st.warning("Selecciona al menos un portal e ingresa un término de búsqueda.")
    else:
        proxies = [p.strip() for p in proxies_raw.splitlines() if p.strip()] or None

        with st.spinner("Extrayendo vacantes..."):
            try:
                jobs = scrape_jobs(
                    site_name=sites,
                    search_term=search_term.strip(),
                    location=location.strip() or None,
                    country_indeed=country_indeed.strip() or "usa",
                    results_wanted=int(results_wanted),
                    hours_old=int(hours_old),
                    job_type=job_type or None,
                    is_remote=is_remote,
                    fetch_description=fetch_description,
                    proxies=proxies,
                    verbose=0,
                )
                st.session_state["jobs_df"] = jobs
                st.session_state["errors"] = jobs.attrs.get("errors", {})
                st.session_state["warnings"] = jobs.attrs.get("warnings", {})
            except Exception as e:
                st.error(f"Error al ejecutar JobSpy: {e}")

jobs = st.session_state["jobs_df"]
if jobs is not None:
    if st.session_state["errors"]:
        st.error(f"Errores por portal: {st.session_state['errors']}")
    if st.session_state["warnings"]:
        st.warning(f"Advertencias: {st.session_state['warnings']}")

    st.success(f"Se encontraron {len(jobs)} vacantes.")

    if not jobs.empty:
        filtro = st.text_input("Filtrar resultados por puesto o empresa:")
        df_view = jobs.copy()
        if filtro:
            mask = (
                df_view["title"].fillna("").str.contains(filtro, case=False, na=False)
                | df_view["company"].fillna("").str.contains(filtro, case=False, na=False)
            )
            df_view = df_view[mask]

        cols_preferidas = [
            "site", "title", "company", "location", "job_type",
            "min_amount", "max_amount", "currency", "date_posted", "job_url",
        ]
        cols_existentes = [c for c in cols_preferidas if c in df_view.columns]

        st.dataframe(
            df_view[cols_existentes],
            use_container_width=True,
            column_config={"job_url": st.column_config.LinkColumn("Enlace")},
        )

        csv_data = df_view.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            "Descargar CSV",
            data=csv_data,
            file_name="vacantes.csv",
            mime="text/csv",
        )

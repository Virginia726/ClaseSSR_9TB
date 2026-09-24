from fastapi import FastAPI, HTTPException
from database import get_connection

app = FastAPI(
    title="Clase SSR",
    description="Tarea creación de tablas",
    version="1.0"
)

@app.get("/db-test")
def probar_base_datos():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT current_database() AS base_datos,
                           current_user AS usuario,
                           NOW() AS fecha_hora;
                """)
                resultado = cursor.fetchone()
                return {
                    "conexion": "correcta",
                    "informacion": resultado            
                }
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"No fue posible conectarse con Postgres: {error}"
        )

@app.get("/personal")
def obtener_personal():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id, nombre, area, turno
                    FROM personal
                    ORDER BY id;
                """)
                personal = cursor.fetchall()
                return personal
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Error al consultar personal: {error}"
        )

@app.get("/maestros")
def obtener_maestros():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id, nombre, correo, turno
                    FROM maestros
                    ORDER BY id;
                """)
                maestros = cursor.fetchall()
                return maestros
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Error al consultar maestros: {error}"
        )

@app.get("/personal")
def obtener_personal():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id, nombre, area, turno
                    FROM personal
                    ORDER BY id;
                """)
                personal = cursor.fetchall()
                return personal
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Error al consultar personal: {error}"
        )
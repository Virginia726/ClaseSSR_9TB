from fastapi import FastAPI, HTTPException
from database import get_connection

app = FastAPI(
    title="Clase SSR",
    description="Primera conexion entre FASTAPI y Postgres",
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
            detail=f"No fue posible conectarse con Postgres {error}"
        )

@app.get("/estudiantes")
def obtener_estudiantes():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT
                        id,
                        nombre,
                        correo,
                        creado_en
                    FROM estudiantes
                    ORDER BY id;
                """)
                
                estudiantes = cursor.fetchall()
                return estudiantes
            
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Error al consultar estudiantes {error}"
        )
def generar_recomendacion_riego(agua_disponible: float, umbral_optimo: float, pronostico_lluvia_mm: float) -> str:
    """
    Genera una recomendación de riego basada en el balance hídrico y el pronóstico de lluvia.

    Args:
        agua_disponible (float): El agua disponible actualmente en el suelo (en mm).
        umbral_optimo (float): El nivel mínimo de agua deseado para el cultivo (en mm).
        pronostico_lluvia_mm (float): La cantidad de lluvia pronosticada (en mm).

    Returns:
        str: Un mensaje con la recomendación de riego.

    Raises:
        ValueError: Si los valores de agua o el umbral son negativos.
    """
    if agua_disponible < 0 or umbral_optimo < 0:
        raise ValueError("El agua disponible y el umbral óptimo no pueden ser negativos.")

    if agua_disponible >= umbral_optimo:
        return "Nivel de humedad óptimo. No se requiere riego."

    # Si el agua está por debajo del umbral, se calcula la necesidad
    necesidad_agua = umbral_optimo - agua_disponible

    # Lógica de "Riego Inteligente"
    if pronostico_lluvia_mm > 0:
        return f"Alerta: Nivel de humedad bajo, pero hay un pronóstico de {pronostico_lluvia_mm} mm de lluvia. Se recomienda esperar."
    else:
        return f"Alerta: Se recomienda aplicar {necesidad_agua:.1f} mm de agua para volver a la capacidad de campo."

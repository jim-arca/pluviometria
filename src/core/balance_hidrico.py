def calcular_balance_hidrico(
    agua_ayer: float,
    lluvia_efectiva: float,
    riego_aplicado: float,
    evapotranspiracion: float
) -> float:
    """
    Calcula el balance hídrico del suelo para un día.

    Args:
        agua_ayer (float): El agua disponible en el suelo del día anterior (en mm).
        lluvia_efectiva (float): La lluvia registrada que efectivamente se infiltra (en mm).
        riego_aplicado (float): El riego que se ha añadido (en mm).
        evapotranspiracion (float): El agua perdida por evaporación y transpiración (en mm).

    Returns:
        float: El agua disponible en el suelo para el día actual (en mm).

    Raises:
        ValueError: Si alguno de los inputs (lluvia, riego, evapotranspiración) es negativo.
    """
    if lluvia_efectiva < 0 or riego_aplicado < 0 or evapotranspiracion < 0:
        raise ValueError("Las mediciones de lluvia, riego y evapotranspiración no pueden ser negativas.")

    agua_hoy = agua_ayer + lluvia_efectiva + riego_aplicado - evapotranspiracion
    return agua_hoy

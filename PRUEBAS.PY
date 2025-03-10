def slot_esta_libre_fecha_determinada(self, fecha):
        if self.fecha_despegue is None or self.fecha_aterrizaje is None:
            # Si el slot no tiene asignada ninguna fecha, está libre
            return 0
        # Convertimos la fecha proporcionada a un objeto datetime si es necesario
        if isinstance(fecha, str):
            fecha = pd.to_datetime(fecha)
        
        # Verificamos si la fecha está fuera del intervalo de [fecha_despegue, fecha_aterrizaje]
        if fecha <= self.fecha_despegue or fecha >= self.fecha_aterrizaje:
            return 0  # El slot está libre
        
        return 1
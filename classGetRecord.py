# classGetRecord.py
import requests

class GetRecord:
    __url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"

    @staticmethod
    def obtener_ultimo_registro():
        try:
            response = requests.get(GetRecord.__url)
            response.raise_for_status()  # Verifica si hubo un error en la solicitud
            data = response.json()

            # Retorna el último registro o un mensaje de error
            if data:
                return data[-1]
            else:
                return {"error": "No se encontraron registros."}
        except Exception as e:
            return {"error": f"Error: {e}"}

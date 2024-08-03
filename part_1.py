# Instalar yfinance si aún no está instalado
!pip install yfinance --upgrade --no-cache-dir

# Importar las librerías necesarias
import yfinance as yf

# Descargar los datos bursátiles de Tesla
tesla_data = yf.download('TSLA')

# Restablecer el índice del DataFrame
tesla_data_reset = tesla_data.reset_index()

# Mostrar las primeras cinco filas del DataFrame
print(tesla_data_reset.head())

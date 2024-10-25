#!/bin/bash

# Activar el entorno virtual
source /home/user/python/mi_entorno/bin/activate

# Ejecutar el script Python
python3 /home/user/python/crypto.py

# Comprobar si la ejecución fue exitosa
if [ $? -eq 0 ]; then
    # Ruta del archivo de log
    LOG_FILE="/home/soyra/python/registro_crypto.log"

    # Registrar la ejecución exitosa
    echo "$(date '+%Y-%m-%d %H:%M:%S') - El archivo ejecutar_crypto.sh se ha ejecutado correctamente." >> $LOG_FILE
else
    # Registrar la falla
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Error al ejecutar el archivo ejecutar_crypto.sh." >> $LOG_FILE
fi


# Desactivar el entorno virtual
deactivate

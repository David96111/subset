import logging
import os  
  
from flask import Flask, url_for, request, render_template_string 
# from Dominio
import time   


from infra.infra import queryDatabase
from dominio.algoritmos import algoritmos

# Configuración de Logs  
log = logging.getLogger()
log.setLevel(logging.INFO)   

# Creamos la aplicación Flask para publicación de servicio
app = Flask(__name__) 
obj = algoritmos(52)

@app.route("/<model_id>") 
def get(model_id): 
    try:
        dta = queryDatabase(f"SELECT subset FROM subsets WHERE id = {model_id}")
        dta_aux = dta[0][0][0]
        print(dta_aux) 
        subset = dta_aux
        return render_template_string(f'''<!doctype html>
                    <html>
                        <head>
                            <link rel="stylesheet" href="css url"/>
                        </head>
                        <body>
                            <h1>id<h1>
                            <p>{str(model_id)}</p>
                            <h1>subset<h1>
                            <p>{subset}</p>
                        </body>
                    </html>
                ''')    
    except:
        return render_template_string(f'''<!doctype html>
                    <html>
                        <head>
                            <link rel="stylesheet" href="css url"/>
                        </head>
                        <body>
                            <h1>404 NOT FOUND<h1> 
                        </body>
                    </html>
                ''')    
 

# Función main para lanzar ejecución del proceso
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True) 

#TODO: Caso de Prueba TC4.1 - Visualización de tareas ordenadas por fecha de vencimiento

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime

# Configuración de opciones para Chrome
chrome_options = Options()
# chrome_options.add_argument("--headless")

# Usar webdriver_manager para gestionar el driver automáticamente
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

try:
    # Abre la aplicación
    driver.get("http://localhost:8000")
    driver.maximize_window()
    time.sleep(2)

    # Datos de prueba: tareas con diferentes fechas
    test_tasks = [
        {
            "name": "Tarea más próxima",
            "desc": "Descripción tarea 1",
            "date": "15/06/2024"
        },
        {
            "name": "Tarea intermedia",
            "desc": "Descripción tarea 2",
            "date": "20/09/2024"
        },
        {
            "name": "Tarea más lejana",
            "desc": "Descripción tarea 3",
            "date": "31/12/2024"
        }
    ]

    # Agregar las tareas de prueba
    for task in test_tasks:
        task_name = driver.find_element(By.ID, "task-name")
        task_desc = driver.find_element(By.ID, "task-desc")
        task_due_date = driver.find_element(By.ID, "task-due-date")
        add_button = driver.find_element(By.XPATH, "//button[text()='Agregar tarea']")

        task_name.send_keys(task["name"])
        task_desc.send_keys(task["desc"])
        task_due_date.send_keys(task["date"])
        add_button.click()
        time.sleep(1)

    # Obtener todas las tareas de la lista
    task_list = driver.find_element(By.ID, "task-list")
    tasks = task_list.find_elements(By.TAG_NAME, "li")

    # Extraer las fechas y nombres de las tareas
    task_dates = []
    for task in tasks:
        task_text = task.text
        print(f"Tarea encontrada: {task_text}")  # Debug
        
        # Buscar la fecha en el texto de la tarea
        for test_task in test_tasks:
            if test_task["name"] in task_text:
                task_dates.append({
                    "date": datetime.strptime(test_task["date"], "%d/%m/%Y"),
                    "name": test_task["name"]
                })
                break

    # Verificar que hay al menos las tareas que agregamos
    assert len(task_dates) >= len(test_tasks), "No se encontraron todas las tareas agregadas"

    # Verificar que las fechas están en orden ascendente
    is_ordered = all(
        task_dates[i]["date"] <= task_dates[i+1]["date"]
        for i in range(len(task_dates)-1)
    )

    assert is_ordered, "Las tareas no están ordenadas por fecha de vencimiento"

    # Verificar que cada tarea muestra toda la información necesaria
    for task in tasks:
        task_text = task.text
        has_name = any(test_task["name"] in task_text for test_task in test_tasks)
        has_desc = any(test_task["desc"] in task_text for test_task in test_tasks)
        has_status = "Pendiente" in task_text or "Completada" in task_text

        assert has_name, "Falta el nombre en alguna tarea"
        assert has_desc, "Falta la descripción en alguna tarea"
        assert has_status, "Falta el estado en alguna tarea"

    print("Caso de Prueba TC4.1: PASADO ✅")
    print("✅ Todas las tareas fueron agregadas correctamente")
    print("✅ Las tareas están ordenadas por fecha de vencimiento")
    print("✅ Cada tarea muestra toda la información requerida")

except AssertionError as ae:
    print(f"Caso de Prueba TC4.1: FALLADO ❌")
    print(f"Error: {str(ae)}")

except NoSuchElementException as nse:
    print(f"Caso de Prueba TC4.1: FALLADO ❌")
    print(f"Error: Elemento no encontrado - {str(nse)}")

except Exception as e:
    print(f"Caso de Prueba TC4.1: FALLADO ❌")
    print(f"Error inesperado: {str(e)}")

finally:
    time.sleep(2)
    driver.quit()

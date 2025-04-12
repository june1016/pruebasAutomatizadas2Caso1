#TODO: Caso de Prueba TC3.1 - Marcar tarea como completada correctamente

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

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

    # Primero, agregar una tarea para asegurar que existe
    task_name = driver.find_element(By.ID, "task-name")
    task_desc = driver.find_element(By.ID, "task-desc")
    task_due_date = driver.find_element(By.ID, "task-due-date")
    add_button = driver.find_element(By.XPATH, "//button[text()='Agregar tarea']")

    # Datos de la tarea
    test_name = "Estudiar para el examen"
    test_desc = "Revisar todos los capítulos del libro"
    test_date = "01/12/2024"

    # Agregar la tarea
    task_name.send_keys(test_name)
    task_desc.send_keys(test_desc)
    task_due_date.send_keys(test_date)
    add_button.click()
    time.sleep(2)

    # Buscar la tarea en la lista
    task_list = driver.find_element(By.ID, "task-list")
    tasks = task_list.find_elements(By.TAG_NAME, "li")
    target_task = None
    complete_button = None

    for task in tasks:
        if test_name in task.text and "Pendiente" in task.text:
            target_task = task
            # Buscar el botón "Marcar Completada"
            buttons = task.find_elements(By.TAG_NAME, "button")
            for button in buttons:
                if "Marcar Completada" in button.text:
                    complete_button = button
                    break
            break

    assert target_task is not None, "No se encontró la tarea para marcar como completada"
    assert complete_button is not None, "No se encontró el botón de marcar como completada"

    # Hacer clic en el botón "Marcar Completada"
    complete_button.click()
    time.sleep(2)

    # Verificar que la tarea está marcada como completada
    tasks = task_list.find_elements(By.TAG_NAME, "li")
    task_completed = False
    task_has_completed_style = False
    
    for task in tasks:
        if test_name in task.text and "Completada" in task.text:
            task_completed = True
            # Verificar si tiene la clase 'completed'
            if "completed" in task.get_attribute("class"):
                task_has_completed_style = True
            break

    assert task_completed, "La tarea no se marcó como completada"
    assert task_has_completed_style, "La tarea no muestra el estilo visual de completada"

    # Recargar la página para verificar persistencia
    driver.refresh()
    time.sleep(2)

    # Verificar que el estado persiste después de recargar
    task_list = driver.find_element(By.ID, "task-list")
    tasks = task_list.find_elements(By.TAG_NAME, "li")
    state_persists = False
    
    for task in tasks:
        if test_name in task.text and "Completada" in task.text:
            state_persists = True
            break

    assert state_persists, "El estado completado no persistió después de recargar la página"

    print("Caso de Prueba TC3.1: PASADO ✅")
    print("✅ La tarea se marcó como completada correctamente")
    print("✅ Se aplicó el estilo visual de tarea completada")
    print("✅ El estado persistió después de recargar la página")

except AssertionError as ae:
    print(f"Caso de Prueba TC3.1: FALLADO ❌")
    print(f"Error: {str(ae)}")

except NoSuchElementException as nse:
    print(f"Caso de Prueba TC3.1: FALLADO ❌")
    print(f"Error: Elemento no encontrado - {str(nse)}")

except Exception as e:
    print(f"Caso de Prueba TC3.1: FALLADO ❌")
    print(f"Error inesperado: {str(e)}")

finally:
    time.sleep(2)
    driver.quit()

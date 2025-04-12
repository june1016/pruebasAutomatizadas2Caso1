#TODO: Caso de Prueba TC1.1 - Agregar tarea con nombre, descripción y fecha válidos

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
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

    # Localiza e ingresa los datos
    task_name = driver.find_element(By.ID, "task-name")
    task_desc = driver.find_element(By.ID, "task-desc")
    task_due_date = driver.find_element(By.ID, "task-due-date")
    add_button = driver.find_element(By.XPATH, "//button[text()='Agregar tarea']")

    test_name = "Estudiar para el examen"
    test_desc = "Revisar todos los capítulos del libro"
    test_date = "01/12/2024"

    task_name.send_keys(test_name)
    task_desc.send_keys(test_desc)
    task_due_date.send_keys(test_date)

    # Hace clic en "Agregar tarea"
    add_button.click()
    time.sleep(2)

    # Verifica el mensaje de confirmación primero
    confirmation = driver.find_element(By.ID, "add-confirmation").text
    assert confirmation == "Tarea agregada con éxito.", "El mensaje de confirmación no se mostró correctamente"

    # Verifica que la tarea aparezca en la lista
    task_list = driver.find_element(By.ID, "task-list")
    tasks = task_list.find_elements(By.TAG_NAME, "li")
    task_found = False
    
    for task in tasks:
        task_text = task.text
        print(f"Verificando tarea encontrada: {task_text}")
        
        if (test_name in task_text and 
            test_desc in task_text and 
            "Pendiente" in task_text):
            task_found = True
            break

    assert task_found, "No se encontró la tarea en la lista"

    # Verifica que los campos se vacíen
    assert task_name.get_attribute('value') == "", "El campo de nombre no se vació"
    assert task_desc.get_attribute('value') == "", "El campo de descripción no se vació"
    assert task_due_date.get_attribute('value') == "", "El campo de fecha no se vació"

    print("Caso de Prueba TC1.1: PASADO ✅")
    print("✅ La tarea se agregó correctamente")
    print("✅ Los campos se vaciaron correctamente")
    print("✅ El mensaje de confirmación se mostró correctamente")

except AssertionError as ae:
    print(f"Caso de Prueba TC1.1: FALLADO ❌")
    print(f"Error: {str(ae)}")

except NoSuchElementException as nse:
    print(f"Caso de Prueba TC1.1: FALLADO ❌")
    print(f"Error: Elemento no encontrado - {str(nse)}")

except Exception as e:
    print(f"Caso de Prueba TC1.1: FALLADO ❌")
    print(f"Error inesperado: {str(e)}")

finally:
    time.sleep(2)
    driver.quit()

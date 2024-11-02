#TODO: Caso de Prueba TC5.1 - Eliminar tarea con confirmación exitosa

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
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

    # Primero, agregar la tarea que vamos a eliminar
    task_name = driver.find_element(By.ID, "task-name")
    task_desc = driver.find_element(By.ID, "task-desc")
    task_due_date = driver.find_element(By.ID, "task-due-date")
    add_button = driver.find_element(By.XPATH, "//button[text()='Agregar tarea']")

    # Datos de la tarea
    test_name = "Comprar materiales de oficina"
    test_desc = "Comprar lápices, papel y otros materiales"
    test_date = "2024-12-01"

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
    delete_button = None

    for task in tasks:
        if test_name in task.text:
            target_task = task
            # Buscar el botón "Eliminar"
            buttons = task.find_elements(By.TAG_NAME, "button")
            for button in buttons:
                if "Eliminar" in button.text:
                    delete_button = button
                    break
            break

    assert target_task is not None, "No se encontró la tarea para eliminar"
    assert delete_button is not None, "No se encontró el botón de eliminar"

    # Hacer clic en el botón "Eliminar"
    delete_button.click()
    time.sleep(1)

    # Aceptar el diálogo de confirmación
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(1)

    # Aceptar el mensaje de éxito
    alert = driver.switch_to.alert
    assert "Tarea eliminada con éxito" in alert.text, "No se mostró el mensaje de éxito"
    alert.accept()
    time.sleep(1)

    # Verificar que la tarea ya no existe en la lista
    tasks = task_list.find_elements(By.TAG_NAME, "li")
    task_still_exists = False
    
    for task in tasks:
        if test_name in task.text:
            task_still_exists = True
            break

    assert not task_still_exists, "La tarea no se eliminó correctamente"

    # Recargar la página para verificar persistencia de la eliminación
    driver.refresh()
    time.sleep(2)

    # Verificar que la tarea sigue sin aparecer
    task_list = driver.find_element(By.ID, "task-list")
    tasks = task_list.find_elements(By.TAG_NAME, "li")
    task_still_exists = False
    
    for task in tasks:
        if test_name in task.text:
            task_still_exists = True
            break

    assert not task_still_exists, "La tarea reapareció después de recargar la página"

    print("Caso de Prueba TC5.1: PASADO ✅")
    print("✅ La tarea se eliminó correctamente")
    print("✅ Se mostró el mensaje de confirmación")
    print("✅ La tarea no existe en la lista después de recargar")

except AssertionError as ae:
    print(f"Caso de Prueba TC5.1: FALLADO ❌")
    print(f"Error: {str(ae)}")

except NoSuchElementException as nse:
    print(f"Caso de Prueba TC5.1: FALLADO ❌")
    print(f"Error: Elemento no encontrado - {str(nse)}")

except UnexpectedAlertPresentException as uae:
    print(f"Caso de Prueba TC5.1: FALLADO ❌")
    print(f"Error: Alerta inesperada - {str(uae)}")

except Exception as e:
    print(f"Caso de Prueba TC5.1: FALLADO ❌")
    print(f"Error inesperado: {str(e)}")

finally:
    time.sleep(2)
    driver.quit()

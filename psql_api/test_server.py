import pytest
import time
import requests

base_url = "http://localhost:5000"

# Тест для получения данных из пустой таблицы
def test_get_data_empty():
    response = requests.get(f"{base_url}/data")
    assert response.status_code == 200
    assert response.json() == []

# Тест для добавления данных
def test_add_data():
    response = requests.post(f"{base_url}/data", json={'text': 'Test data'})
    assert response.status_code == 200
    assert response.text == 'Data added successfully.'

# Тест для получения данных после добавления
def test_get_data_after_add():
    response = requests.get(f"{base_url}/data")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]['text'] == 'Test data'

# Тест для обновления данных
def test_update_data():
    response = requests.put(f"{base_url}/data/1", json={'text': 'Updated data'})
    assert response.status_code == 200
    assert response.text == 'Data updated successfully.'

# Тест для получения обновленных данных
def test_get_updated_data():
    response = requests.get(f"{base_url}/data/1")
    assert response.status_code == 200
    assert response.json()['text'] == 'Updated data'

# Тест для удаления данных по идентификатору
def test_delete_data_by_id():
    response = requests.delete(f"{base_url}/data/1")
    assert response.status_code == 200
    assert response.text == 'Data deleted successfully.'

# Тест для получения данных после удаления по идентификатору
def test_get_data_after_delete_by_id():
    response = requests.get(f"{base_url}/data")
    assert response.status_code == 200
    assert response.json() == []

# Тест для удаления данных
def test_delete_data():
    response = requests.delete(f"{base_url}/data")
    assert response.status_code == 200
    assert response.text == 'Table cleared and sequence reset.'

# Тест получения данных из таблицы после удаления всех данных .
def test_get_data_after_delete():
    response = requests.get(f"{base_url}/data")
    assert response.status_code == 200
    assert response.json() == []

# Тест для обработки некорректных запросов (отсутствие текста при добавлении)
def test_add_data_without_text():
    response = requests.post(f"{base_url}/data", json={})
    assert response.status_code == 400
    assert response.text == 'No text provided.'

# Тест для обработки некорректных запросов (отсутствие текста при обновлении)
def test_update_data_without_text():
    response = requests.put(f"{base_url}/data/1", json={})
    assert response.status_code == 400
    assert response.text == 'No text provided.'

# Тест для обработки некорректных запросов (некорректный идентификатор при получении)
def test_get_data_with_invalid_id():
    response = requests.get(f"{base_url}/data/999")
    assert response.status_code == 404
    assert response.text == 'Data not found.'

# Тест для обработки некорректных запросов (некорректный идентификатор при обновлении)
def test_update_data_with_invalid_id():
    response = requests.put(f"{base_url}/data/999", json={'text': 'Updated data'})
    assert response.status_code == 200
    assert response.text == 'Data updated successfully.'  # Поведение приложения при некорректном идентификаторе не определено

# Тест для обработки некорректных запросов (некорректный идентификатор при удалении)
def test_delete_data_with_invalid_id():
    response = requests.delete(f"{base_url}/data/999")
    assert response.status_code == 200
    assert response.text == 'Data deleted successfully.'  # Поведение приложения при некорректном идентификаторе не определено

# Тест для проверки возможности добавления строки длиной 100 символов
def test_add_data_with_100_char_text():
    text_100_chars = 'x' * 100  # Строка длиной 100 символов
    response = requests.post(f"{base_url}/data", json={'text': text_100_chars})
    assert response.status_code == 200
    assert response.text == 'Data added successfully.'

# Тест для проверки возможности добавления строки со всеми символами
def test_add_data_with_all_characters():
    all_characters = "~!@#$%^&*()_+[]{}|\\:;\"'<>?,./-=0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёйцукенгшщзхъфывапролджэячсмитьбю"
    response = requests.post(f"{base_url}/data", json={'text': all_characters})
    assert response.status_code == 200
    assert response.text == 'Data added successfully.'
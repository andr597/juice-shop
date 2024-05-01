import requests
import json

def send_scan_results_to_defectdojo(scan_results):
    # Замените эти значения на реальные данные вашего DefectDojo
    api_key = 'cdb534f92bdb20e27f3e08a79075e837e71aab4b'
    host = 'http://172.26.66.248:8080/'

    headers = {
        'Authorization': f'Token {api_key}',
        'Content-Type': 'application/json'
    }

    # Пример данных сканирования (замените этим на реальные данные)
    scan_data = {
        'scan_type': 'GitHub Repository Scan',
        'engagement_id': 1,  # Замените на ID вашего engagement в DefectDojo
        'scan_date': '2024-05-01T12:00:00Z',
        'scan_findings': scan_results
    }

    # Отправка результатов сканирования в DefectDojo
    response = requests.post(f'{host}/api/v2/import-scan/', headers=headers, data=json.dumps(scan_data))

    if response.status_code == 201:
        print('Результаты сканирования успешно отправлены в DefectDojo')
    else:
        print('Ошибка при отправке результатов сканирования в DefectDojo')
        print(response.text)

# Пример данных о результатах сканирования (замените этим на реальные данные)
# Это может быть список обнаруженных уязвимостей, тестов и другой информации
scan_results = [
    {'title': 'SQL Injection', 'severity': 'High', 'description': 'SQL injection vulnerability found'},
    {'title': 'Cross-Site Scripting', 'severity': 'Medium', 'description': 'XSS vulnerability found'}
]

send_scan_results_to_defectdojo(scan_results)

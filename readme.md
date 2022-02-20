Test-work
1. @routes.get('/geonameid/{geoname_id}')
Метод принимает на вход идентификатор geoname_id и, как результат 
отправляет json с информацией о геоточке.
Пример запроса: 
http://127.0.0.1:8000/geonameid/451771
Пример ответа:
{"geoname_id": "451747", 
"name": "Zyabrikovo", "asciiname": "Zyabrikovo", "alternatenames": "", 
"latitude": "56.84665", "longitude": "34.7048", "feature_class": "P", 
"feature_code": "PPL", "country_code": "RU", "cc2": "", "admin1_code": "77", 
"admin2_code": "", "admin3_code": "", "admin4_code": "", "population": "0", 
"elevation": "", "dem": "204", "timezone": "Europe/Moscow", 
"modification_date": "2011-07-09"}
2. @routes.get('/page/{page_number}/{number}')
Метод принимает на вход номер страницы и количество отображаемых на странице 
городов и как результат отправляет json с информацией о городах на указанной странице.
Пример запроса:
http://127.0.0.1:8000/page/2/2
Пример ответа:
"[{\"geoname_id\":\"451750\",\"name\":\"Zhitovo\",\"asciiname\":\"Zhitovo\",
\"alternatenames\":\"\",\"latitude\":\"57.29693\",\"longitude\":\"34.41848\",
\"feature_class\":\"P\",\"feature_code\":\"PPL\",\"country_code\":\"RU\",
\"cc2\":\"\",\"admin1_code\":\"77\",\"admin2_code\":\"\",\"admin3_code\":\"\",
\"admin4_code\":\"\",\"population\":\"0\",\"elevation\":\"\",\"dem\":\"247\",
\"timezone\":\"Europe/Moscow\",\"modification_date\":\"2011-07-09\"},
{\"geoname_id\":\"451751\",\"name\":\"Zhitnikovo\",\"asciiname\":\"Zhitnikovo\",
\"alternatenames\":\"\",\"latitude\":\"57.20064\",\"longitude\":\"34.57831\",
\"feature_class\":\"P\",\"feature_code\":\"PPL\",\"country_code\":\"RU\",
\"cc2\":\"\",\"admin1_code\":\"77\",\"admin2_code\":\"\",\"admin3_code\":\"\",
\"admin4_code\":\"\",\"population\":\"0\",\"elevation\":\"\",\"dem\":\"198\",
\"timezone\":\"Europe/Moscow\",\"modification_date\":\"2011-07-09\"}]".
Полученный ответ может быть обработан с помощью json.loads().
3. 

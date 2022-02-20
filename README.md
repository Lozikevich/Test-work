# Test-work
Test work
<h3>Метод 1</h3>
<pre>@routes.get('/geonameid/{geoname_id}')
Данный метод принимает на вход идентификатор числовой "geoname_id" и как результат отправляет json с информацией о геоточке.
Пример запроса в браузере: http://127.0.0.1:8000/geonameid/451771
Пример ответа, полученного в браузере:
<em color='blue>{"geoname_id": "451747", "name": "Zyabrikovo", "asciiname": "Zyabrikovo", "alternatenames": "", "latitude": "56.84665", 
"longitude": "34.7048", "feature_class": "P", "feature_code": "PPL", "country_code": "RU", "cc2": "", "admin1_code": "77", 
"admin2_code": "", "admin3_code": "", "admin4_code": "", "population": "0", "elevation": "", "dem": "204", 
"timezone": "Europe/Moscow", "modification_date": "2011-07-09"}</em'>
</pre>
<h3>Метод 2</h3>
<pre>@routes.get('/page/{page_number}/{number}')
Данный метод принимает на вход номер страницы и количество отображаемых на странице городов и как результат отправляет json 
с информацией о городах на указанной странице.
Пример запроса в браузере: http://127.0.0.1:8000/page/2/2
Пример ответа, полученного в браузере:
Пример ответа, полученного в браузере:
<em color='blue>"[{\"geoname_id\":\"451750\",\"name\":\"Zhitovo\",\"asciiname\":\"Zhitovo\", \"alternatenames\":\"\",\"latitude\":\"57.29693\",
\"longitude\":\"34.41848\",\"feature_class\":\"P\",\"feature_code\":\"PPL\",\"country_code\":\"RU\",\"cc2\":\"\",\"admin1_code\":\"77\",
\"admin2_code\":\"\", \"admin3_code\":\"\", \"admin4_code\":\"\",\"population\":\"0\",\"elevation\":\"\",\"dem\":\"247\",
\"timezone\":\"Europe/Moscow\",\"modification_date\":\"2011-07-09\"}, 
{\"geoname_id\":\"451751\",\"name\":\"Zhitnikovo\",\"asciiname\":\"Zhitnikovo\", \"alternatenames\":\"\",\"latitude\":\"57.20064\",
\"longitude\":\"34.57831\", \"feature_class\":\"P\",\"feature_code\":\"PPL\",\"country_code\":\"RU\", \"cc2\":\"\",\"admin1_code\":\"77\",
\"admin2_code\":\"\", \"admin3_code\":\"\",\"admin4_code\":\"\",\"population\":\"0\",\"elevation\":\"\",\"dem\":\"198\", 
\"timezone\":\"Europe/Moscow\",\"modification_date\":\"2011-07-09\"}]".
</em'>

</pre>

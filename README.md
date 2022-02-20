# Test-work
Test work
<h3>Метод 1</h3>
<pre>@routes.get('/geonameid/{geoname_id}')
Данный метод принимает на вход идентификатор числовой "geoname_id" и как результат отправляет json с информацией о геоточке.
<h5>Пример запроса в браузере: http://127.0.0.1:8000/geonameid/451771</h5>
<h5>Пример ответа, полученного в браузере:</h5>
<em>{"geoname_id": "451747", "name": "Zyabrikovo", "asciiname": "Zyabrikovo", "alternatenames": "", "latitude": "56.84665", 
"longitude": "34.7048", "feature_class": "P", "feature_code": "PPL", "country_code": "RU", "cc2": "", "admin1_code": "77", 
"admin2_code": "", "admin3_code": "", "admin4_code": "", "population": "0", "elevation": "", "dem": "204", 
"timezone": "Europe/Moscow", "modification_date": "2011-07-09"}</em>
</pre>
<h3>Метод 2</h3>
<pre>@routes.get('/page/{page_number}/{number}')
Данный метод принимает на вход номер страницы и количество отображаемых на странице городов и как результат отправляет json 
с информацией о городах на указанной странице.
<h5>Пример запроса в браузере: http://127.0.0.1:8000/page/2/2</h5>
<h5>Пример ответа, полученного в браузере:</h5>
<em>"[{\"geoname_id\":\"451750\",\"name\":\"Zhitovo\",\"asciiname\":\"Zhitovo\", \"alternatenames\":\"\",\"latitude\":\"57.29693\",
\"longitude\":\"34.41848\",\"feature_class\":\"P\",\"feature_code\":\"PPL\",\"country_code\":\"RU\",\"cc2\":\"\",\"admin1_code\":\"77\",
\"admin2_code\":\"\", \"admin3_code\":\"\", \"admin4_code\":\"\",\"population\":\"0\",\"elevation\":\"\",\"dem\":\"247\",
\"timezone\":\"Europe/Moscow\",\"modification_date\":\"2011-07-09\"}, 
{\"geoname_id\":\"451751\",\"name\":\"Zhitnikovo\",\"asciiname\":\"Zhitnikovo\", \"alternatenames\":\"\",\"latitude\":\"57.20064\",
\"longitude\":\"34.57831\", \"feature_class\":\"P\",\"feature_code\":\"PPL\",\"country_code\":\"RU\", \"cc2\":\"\",\"admin1_code\":\"77\",
\"admin2_code\":\"\", \"admin3_code\":\"\",\"admin4_code\":\"\",\"population\":\"0\",\"elevation\":\"\",\"dem\":\"198\", 
\"timezone\":\"Europe/Moscow\",\"modification_date\":\"2011-07-09\"}]".
</em>
Полученный ответ может быть обработан с помощью json.loads().
</pre>
<h3>Метод 3</h3>
<pre>@routes.get('/cities/{aname_1}/{aname_2}', allow_head=False)
Метод принимает на вход название города_1 и название города_2 на русском языке и как результат отправляет json, содержащий информацию:
- о каждом городе, 
- информацию о том, какой из городов находится севернее, 
- информацию об одинаковости временных зон.
При этом, если при фильтрации выявляются несколько городов с одинаковым названием, то метод выбирает город с наибольшей численностью населения.
Дополнительно:
- метод выводит разницу временных зон в часах (с "+" - если в первом городе время относительного второго больше, с "-" - соответственно обратное).
- при неполном введении названия города, метод выводит список из всех возможных вариантов для заданного отрывка названия города.
<h5>Пример запроса в браузере: http://127.0.0.1:8000/cities/Вороново/Аил</h5>
<h5>Пример ответа, полученного в браузере:</h5>
<em>"[{\"geoname_id\": \"471938\", \"name\": \"Voronovo\", \"asciiname\": \"Voronovo\", \"alternatenames\":
\"Voronovo,\\u0412\\u043e\\u0440\\u043e\\u043d\\u043e\\u0432\\u043e\", \"latitude\": \"56.36525\", \"longitude\": \"37.68534\", \"feature_class\": \"P\", \"feature_code\":
\"PPL\", \"country_code\": \"RU\", \"cc2\": \"\", \"admin1_code\": \"47\", \"admin2_code\": \"\", \"admin3_code\": \"\", \"admin4_code\": \"\", \"population\": \"12\",
\"elevation\": \"\", \"dem\": \"206\", \"timezone\": \"Europe/Moscow\", \"modification_date\": \"2015-02-01\"},
{\"geoname_id\": \"1512090\", \"name\": \"Ail\", \"asciiname\": \"Ail\", \"alternatenames\": \"Ail,\\u0410\\u0438\\u043b\", \"latitude\": \"53.33333\", \"longitude\":
\"87.21667\", \"feature_class\": \"P\", \"feature_code\": \"PPL\", \"country_code\": \"RU\", \"cc2\": \"\", \"admin1_code\": \"29\", \"admin2_code\": \"\", \"admin3_code\":
\"\", \"admin4_code\": \"\", \"population\": \"0\", \"elevation\": \"\", \"dem\": \"253\", \"timezone\": \"Asia/Novokuznetsk\", \"modification_date\": \"2012-01-17\"},
{\"Voronovo\": \"located to the north\", \"timezone\": \"different, the difference is: 4 hours\"}]"
Полученный ответ может быть обработан с помощью json.loads().
<h5>Пример запроса в браузере с неполным вводом названия города_1: http://127.0.0.1:8000/cities/Воро/Аил</h5>
<em>"[\"CITY WITH NAME_1 NOT FOUND TRY WITH\", [\"Voronovo\", \"Vorob'yevo\", \"Vorotkovo\", \"Voropayevka\", \"Vorodunovo\", \"Vtoroy Pol'noy Voronezh\", 
\"Vtoraya Vorob'yevka\", \"Vorovskiy\", \"Voroz'ma\", \"Vorozhtsovo\", \"Vorozhino\", \"Vorozhgora\", \"Vorovskoy\", \"Vorovskolesskaya\", \"Vorovo\", \"Vorovaya\",
\"Vorotyshino\", \"Vorotyntsevo\", \"Vorotynsk\", \"Vorotynovo\", \"Vorotynka\", \"Vorotynets\", \"Vorottsy\", \"Vorotovo\", \"Vorotovka\", \"Vorotnino\", \"Vorotishino\",
\"Vorotishna\", \"Vorotimovo\", \"Vorotilovo\", \"Vorotilov\", \"Vorotilikha\", ............, \"Verkhnyaya Voronka\", \"Vorobetskaya\", \"Vorokhoby\"]]"
</em>
При неполном вводе города_2 результат будет аналогичный. В случае неполного ввода обоих городов, метод выведет два списка с возможными наименованиями городов.
</pre>

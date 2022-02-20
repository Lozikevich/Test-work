import json
import config
from pytils import translit
from aiohttp import web
import Functions

routes = web.RouteTableDef()


@routes.get('/geonameid/{geoname_id}', allow_head=False)
async def get_one_by_geoname_id(request: web.Request) -> web.Response:
    geoname_id: str = request.match_info['geoname_id']
    geoname = await Functions.get_one_by_geoname_id(geoname_id)
    return web.json_response(geoname.to_json()) if geoname else web.HTTPNotFound()
    # http://127.0.0.1:8000/geonameid/451771


@routes.get('/page/{page_number}/{number}', allow_head=False)
async def get_geoname_from_page(request: web.Request) -> web.Response:
    if await Functions.page_maker(int(request.match_info['page_number']), int(request.match_info['number'])):
        geonames = await Functions.page_maker(int(request.match_info['page_number']), int(request.match_info['number']))
        return web.json_response(
            json.dumps(geonames, ensure_ascii=False, separators=(',', ':',))) if geonames else web.HTTPNotFound()
    else:
        return web.Response(text='Incorrect page_number or number')
    # http://127.0.0.1:8000/page/2/3


@routes.get('/cities/{aname_1}/{aname_2}', allow_head=False)
async def get_two_cities(request: web.Request) -> web.Response:
    geoname_1 = await Functions.get_by_asciiname(request.match_info['aname_1'])
    geoname_2 = await Functions.get_by_asciiname(request.match_info['aname_2'])
    if geoname_1 and geoname_2:
        comparison = await Functions.latitudde_compare(geoname_1, geoname_2)
        geonames = [geoname_1.to_json(), geoname_2.to_json(), comparison]
        return web.json_response(json.dumps(geonames) if geonames else web.HTTPNotFound())
    elif geoname_1:
        name_list = await Functions.name_list(translit.translify(request.match_info['aname_2']))
        return web.json_response((json.dumps(['CITY WITH NAME_2 NOT FOUND TRY WITH', name_list])
                                 if name_list else web.HTTPNotFound()))
    elif geoname_2:
        name_list = await Functions.name_list(translit.translify(request.match_info['aname_1']))
        return web.json_response(json.dumps(['CITY WITH NAME_1 NOT FOUND TRY WITH', name_list])
                                 if name_list else web.HTTPNotFound())
    else:
        return web.Response(text='CITIES NOT FOUND')
    # http://127.0.0.1:8000/cities/Вороново/Тресково


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host=config.for_server['host'], port=config.for_server['port'])

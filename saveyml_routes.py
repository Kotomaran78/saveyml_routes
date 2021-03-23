from sanic.response import json
import yaml

def save_data_to_yml(web, app):
    sanic = web.sanic

    @sanic.route('/save_data_to_yml', methods=["POST"])
    async def f_data(request):
        with open('save_data_to_yml.yml', 'w') as f:
            yaml.dump(request.body, f, default_flow_style=False)
        return json({"message":"Ok"})

    @sanic.route('/save_data_to_yml2', methods=["POST"])
    async def f_data(request):
        with open('save_data_to_yml2.yml', 'w') as f:
            yaml.dump(request.body, f, default_flow_style=False)
        return json({"message":"Ok"})
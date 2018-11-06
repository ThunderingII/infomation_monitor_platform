from core.auto import config_process
from core.util import log_util
from core.util import data_util
from core.util import config_util
from core.session.platform_session import IMP_Session

log = log_util.get_logger()


def main_process(main_config_file):
    reu = config_process.RequestConfigUtil(main_config_file)
    request_queue = [reu.mrn]
    session = IMP_Session(reu.ju.get('name'))
    # todo should support mutil-threads
    while request_queue:
        request_name = request_queue.pop()
        request = reu.get_request(request_name)
        # todo check request

        # do a request
        url = request.get('url')
        data = request.get('data')
        if data:
            for key in data:
                session.add_value(key, data[key])
        # todo exception process
        if request.get('request_type') == 'get':
            response = session.get(url)
        else:
            response = session.post(url)

        # begin condition process
        if not request.get('requestOperation.condition'):
            print(f'cannot find condition {request_name}')
            continue
        condition = config_util.DictWrapper(request.get('requestOperation.condition'))
        response_data = None
        if request.get('return_type') == 'html':
            response_type = data_util.ResponseType.html
            html = data_util.pre_process(response, response_type)
            tag = html.find(name=condition.get('targetElement.name'), attrs=condition.get('targetElement.attrs'))
            if tag is None:
                print(f'cannot find a tag {condition.get("targetElement")}')
            else:
                response_data = tag.string
        else:
            response_type = data_util.ResponseType.json
            json = data_util.pre_process(response, response_type)
            response_data = json.get(condition.get('targetElement'))

        # begin operation
        if response_data:
            operation_name = condition_execute(response_data, condition)
            operation = reu.get_operation(operation_name)
            if 'goto' in operation.get('type'):
                request_queue.append(operation.get('gotoSetting.gotoTag'))
            if 'notice' in operation.get('type'):
                notice_process(operation.get('noticeSetting'))


def notice_process(noticeSetting=None):
    # todo notice process
    pass


def condition_execute(data, condition):
    aimData = condition.get('aimData')
    if condition.get('dataType') == 'int':
        data = int(data)
        aimData = int(aimData)
    elif condition.get('dataType') == 'float':
        data = float(data)
        aimData = float(aimData)
    else:
        aimData = str(aimData)

    c = False
    symbol = condition.get('symbol')

    if symbol == 'in':
        c = aimData in data
    elif symbol == '=':
        c = aimData == data
    elif symbol == '>':
        c = data > aimData
    elif symbol == '<':
        c = data < aimData
    elif symbol == '>=':
        c = data >= aimData
    elif symbol == '<=':
        c = data <= aimData
    if c:
        return condition.get('true')
    else:
        return condition.get('false')

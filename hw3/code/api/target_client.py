import requests
import json
from urllib.parse import urljoin

from requests.cookies import cookiejar_from_dict

class CantFoundSegmentException(Exception):
    pass


class TargetClient:

    def __init__(self,username,password):
        self.main_url= 'https://target.my.com/'
        self.session = requests.Session()

        self.username=username
        self.password=password

        self.auth()
        self.csrf_tocken = self.get_csrf()
        


    def _request(self,method,url=None,location=None,headers=None,params=None,data=None,json=False,allow_redirects=False):
        """
        Обертка для метода request, нужен для взаимодействия с апи через объект сессию
        """
        if location is not None and url is None:
            url = urljoin(self.main_url, location)
        
        res = self.session.request( \
                                method=method, \
                                url=url, \
                                headers=headers, \
                                params=params, \
                                data=data, \
                                allow_redirects=allow_redirects \
                                )

        if json :
            return res.json()
        else:
            return res

    def auth(self):
        """
        Метод авторизации клиента
        """
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'
                   }
        data = {
            'email': self.username,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1#email'
        }

        response = self._request(
            'POST', url='https://auth-ac.my.com/auth?lang=ru&nosavelogin=0', headers=headers, data=data
            )

        while response.status_code == 302:
            location = response.headers['Location']
            response = self._request('GET', location)
        
        return response

    def get_csrf(self):
        """
        Возвращает csrf токен 
        """
        csrf_headers = {
            'Referer': 'https://target.my.com/auth/mycom?state=target_login%3D1',
        }
        log = self._request('GET', location='csrf', headers=csrf_headers)

        return log.headers['Set-Cookie'].split(';')[0].split('=')[-1]

    def create_segment(self, name):
        """
        Создает сегмент с именем name
        """
        header = {
            'Content-Type': 'application/json',
            'Referer': 'https://target.my.com/segments/segments_list/new',
            'X-CSRFToken': self.csrf_tocken
        }

        url_params = {
            'fields': 'relations__object_type,relations__object_id,relations__params,relations_count,id,name,'
                      'pass_condition,created,campaign_ids,users,flags',
        }
        
        data = {
            'name' : name , 
            'pass_condition': 1,
            'relations': [{
                'object_type': 'remarketing_player',
                'params': {
                    'type': 'positive',
                    'left': 365,
                    'right': 0,
                }
            }],
            'logicType': 'or',
        }

        return self._request(
            method      = 'POST', 
            location    = 'api/v2/remarketing/segments.json', 
            params      = url_params , 
            data        = json.dumps(data), 
            headers     = header )


    def __get_segment_id(self,name=None):
        """
        Возвращает id сегмента если он найден, иначе CantFoundSegmentException
        """
        headers = {
            'Content-Type' : 'application/json',
            'X-CSRFToken': self.csrf_tocken
        }
        url_params = {
            'limit' : '500'
        }
        segments = self._request(
                    method      =   'GET',
                    location    =   'api/v2/remarketing/segments.json', 
                    params      =   url_params, 
                    headers     =   headers, 
                    json        =   True
                    )['items']
        if name is None :
            return segments[-1]['id']
        else:
            for segment in segments:
                if segment['name'] == name:
                    return segment['id']
            raise CantFoundSegmentException()

    def delete_segment(self, name):
        """
        Удаляет сегмент и возвращает код ответа, иначе CantFoundSegmentException
        """
        headers = {
            'Content-Type' : 'application/json',
            'X-CSRFToken': self.csrf_tocken
        }
        id = self.__get_segment_id(name)
        return self._request(
                    method      =   'DELETE', 
                    location    =   f'api/v2/remarketing/segments/{id}.json', 
                    headers     =   headers)

    def check_segment(self, name):
        """
        Возвращает True если сегмент существует 
        """
        try:
            self.__get_segment_id(name)
            return True
        except CantFoundSegmentException:
            return False
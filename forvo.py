#- * -coding: utf - 8 - * -
import json
import os
from ..base import *


@register([u'Forvo', u'Forvo'])
class Forvo(WebService):

    def __init__(self):
        super(Forvo, self).__init__()

    def _get_from_api(self):
        # sorts by rating, so the highest rated audio file is downloaded.
        url = 'https://apicorporate.forvo.com/api2/v1.2/d6a0d68b18fbcf26bcbb66ec20739492/word-pronunciations/word/{}/language/zh/order/rate-desc'.format(self.quote_word)
        html = self.get_response(url, timeout=10)
        result = {
            'mp3': u"",
        }
        data = json.loads(html)
        try:
            result['mp3'] = data['data']['items'][0]['realmp3']
        except:
            pass

        return self.cache_this(result)

    @export([u'Voice', u'Voice'])
    def fld_mp3(self):
        url = self._get_field('mp3')
        filename = u'forvo_{}.mp3'.format(self._word)
        if os.path.exists(filename) or self.download(url, filename):
            return self.get_anki_label(filename, 'audio')

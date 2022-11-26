import datetime

from smelk_assistant_base import formats


class Current:
    def __init__(self, region: formats.Region = formats.Region("au")):
        self.region = region

    def get_date(self):
        return datetime.datetime.now().strftime(self.region.date_format)

    def get_time(self):
        return datetime.datetime.now().strftime(self.region.time_format)

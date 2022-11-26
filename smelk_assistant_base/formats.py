class Region:

    def __init__(self, region_code: str):
        if region_code == "au":
            self.date_format = "%d/%m/%Y"
            self.time_format = "%I:%M %p"
        elif region_code == "us":
            self.date_format = "%m/%d/%Y"
            self.time_format = "%I:%M %p"

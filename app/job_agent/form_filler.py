class FormFiller:
    def __init__(self, page, resume):
        self.page = page
        self.resume = resume

    def fill(self):
        fields = {
            "name": self.resume["name"],
            "email": self.resume["email"],
            "phone": self.resume["phone"]
        }

        for key, value in fields.items():
            try:
                self.page.fill(f"input[name*='{key}']", value)
            except:
                pass

        self.page.wait_for_timeout(2000)

class MyRouter(object):
    def __init__(self, name, model, serial, ios):
        self.name = name
        self.model = model
        self.serial = serial
        self.ios = ios

    def print_router(self, date):
        print("The router name is {}".format(self.name))
        print("The router model is {}".format(self.model))
        print("The router serial is {}".format(self.serial))
        print("The router ios is {}".format(self.ios))
        print("The router manufacturing date is {}".format(date))



router1 = MyRouter("Cisco", "CIS102", "98765432", "12.5")
router1.print_router("16-August-2015")

class cpu:
    def __init__(self, cores):
        self.cores = cores

class  ram:
    def __init__(self, size):
        self.size = size

class hardDrive:
    def __init__(self, capacity):
        self.capacity = capacity


class computer:
    def __init__(self, cores, ram_size, hd_capacity):
        self.cpu = cpu(cores)
        self.ram = ram(ram_size)
        self.hard_drive = hardDrive(hd_capacity)

    # print(self.cpu.cores)
    def show_result(self):
        print("cpu cores : ", self.cpu.cores)
        print("cpu ram : ", self.ram.size)
        print("cpu dard drive : ", self.hard_drive.capacity)

mac = computer(5, 24, 256)
print(mac.cpu.cores)

mac.show_result()
        
        
        
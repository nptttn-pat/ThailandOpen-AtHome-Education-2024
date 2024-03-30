from random import randint
import json
import sys

name_list = ['amelia','angel','ava','charlie','charlotte','hunter','max','mia','olivia','parker','sam','mark','angel','charlie','hunter','jack','max','noah','oliver','parker','sam','thomas','william']
pose_list = ['sit', 'stand']
position_list = ['white table', 'bin', 'long table', 'drawner']

class FMMGuestGenerator(object):
    def __init__(self):
        pass

    def generate(self):
        self.guest = {}
        self.used_name = []
        self.usesd_position = []
        for i in range(1,4):
            guest_no = i
            self.guest.setdefault(guest_no, {})
            name = name_list[randint(0,len(name_list)-1)]
            while name in self.used_name:
                name = name_list[randint(0,len(name_list)-1)] 
            position = position_list[randint(0,len(position_list)-1)]
            while position in self.usesd_position:
                position = position_list[randint(0,len(position_list)-1)]
            self.used_name.append(name)
            self.usesd_position.append(position)

            self.guest[guest_no].setdefault("name", name)
            self.guest[guest_no].setdefault("position", position)

            if i == 3:
                self.guest[guest_no].setdefault("pose", pose_list[randint(0,len(pose_list)-1)])

        json_formatted_str = json.dumps(self.guest, indent=2)

        print("=========================================================")
        print ("| {:<5} | {:<10} | {:<15} | {:<15} |".format('Guest','Name','Position','Pose'))
        print("=========================================================")
        for i in self.guest:
            try:
                print("| {:<5} | {:<10} | {:<15} | {:<15} |".format(i,self.guest[i]['name'],self.guest[i]['position'],self.guest[i]['pose']))
            except KeyError:
                print("| {:<5} | {:<10} | {:<15} | {:<15} |".format(i,self.guest[i]['name'],self.guest[i]['position'],"stand"))

            print("---------------------------------------------------------")
    
if __name__ == "__main__":
    gen = FMMGuestGenerator()
    if len(sys.argv) == 1:
        gen.generate()
    else:
        for i in range(int(sys.argv[1])):
            print(f"\n========= {i+1} ===========\n")
            gen.generate()
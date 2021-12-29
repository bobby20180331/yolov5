import json
import os

## convert annotation from a json file to txt file for yolov5
def convert(data,name,json_path):
    for m in range(len(data['marks'])):
        # Get required data
        ct=data['marks']
        print(len(ct))
        if len(ct) ==0:
            print("empty ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++empty")
        for j in range(len(ct)):
            bbox=ct[j]['bandbox']
            print(bbox)
            print(type)
            ## redefine class
            if ct[j]['type']=="猫":
                cls=int(0)
            elif ct[j]['type']=="狗":
                cls=int(1)
            else:
                cls=int(9)
            print("cls:",cls)
              
            # Prepare for export   
            txtfilename = f'{name}.txt'
            txtfilename=json_path+txtfilename
            cx=float(bbox[0])
            cy=float(bbox[1])
            w=float(bbox[2])
            h=float(bbox[3])
            content =f"{cls} {cx} {cy} {w} {h}\n"
            with open(txtfilename, 'a') as file_object:
                file_object.write(content)

# for all the json file in the file paths:

if __name__ == "__main__":
    json_path='/data/ai/datasets/pet2k/devtest/'
    datanames = os.listdir(json_path)

   ## ## make sure delete all related txt files in the file path first.
    for i in datanames:
        filename=os.path.splitext(i)
        if filename[1]=='.txt' :
            filepath=json_path+i
            os.remove(filepath)


    for i in datanames:
        filename=os.path.splitext(i)
        if filename[1]=='.json' :
            # print(i)
            filepath=json_path+i
            # print(filename)
            with open(filepath) as f_obj:
                data = json.load(f_obj)
            convert(data,filename[0],json_path)

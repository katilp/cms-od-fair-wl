import json

def main():

    with open('mydata/metadata.json') as f:
        data = f.read()
            
    # reconstructing the data as a dictionary
    all_meta = json.loads(data)
    

    # print("PRINT looping items (one item in one line)")
    # for key, value in all_meta.items() :
    #    print (key, value)

    print("GT=" + all_meta['system_details']['global_tag'])
    print("RELEASE=" + all_meta['system_details']['release'])
    type = all_meta['type']['secondary'][0]
    print("TYPE=" + type) #collision or simulated
    if type == "Collision": 
      print("VALI_RECID=" + all_meta['note']['links'][0]['recid']) #recid of validated runs file
    print("FORMAT=" + all_meta['distribution']['formats'][0]) #this assumes alphabetical order, do better
    #print(all_meta['files'][0]['uri']) #get these directly with cernopendata-client


if __name__ == "__main__":
    main()
import json

def main():

    with open('mydata/metadata.json') as f:
        data = f.read()
            
    # reconstructing the data as a dictionary
    all_meta = json.loads(data)
    # print("PRINT ALL (all in one line)")
    # print(all_meta)

    #print("PRINT KEYS")
    #print(all_meta.keys()) #prints keys

    # print("PRINT looping items (one item in one line)")
    # for key, value in all_meta.items() :
    #    print (key, value)
    #print("PRINT VALUES")
    print("export GT=" + all_meta['system_details']['global_tag'])
    print("export RELEASE=" + all_meta['system_details']['release'])
    #print(all_meta['note']) #prints value of note
    print("export VALI_RECID=" + all_meta['note']['links'][0]['recid']) #recid of validated runs file
    print("export TYPE=" + all_meta['type']['secondary'][0]) #collision or simulated
    print("export FORMAT=" + all_meta['distribution']['formats'][0]) #this assumes alphabetical order, do better
    #print(all_meta['files'][0]['uri']) #get these directly with cernopendata-client


if __name__ == "__main__":
    main()
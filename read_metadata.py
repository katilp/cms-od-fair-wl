import json
import sys

def main():

    filename = sys.argv[1]
    with open(filename) as f:
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
    formats = all_meta['distribution']['formats'] #array of formats
    format=[f for f in formats if "aod" in f][0] #print first of all items with aod
    print("FORMAT=" + format)
    im_dict = all_meta['image'] #array of dicts
    print("IMAGE=" + [im for im in im_dict if "docker.io" in im['name']][0]['name']) #print first of all items with a specified registry


if __name__ == "__main__":
    main()
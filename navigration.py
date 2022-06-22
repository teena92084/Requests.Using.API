import requests
import json
url1=requests.get("https://api.merakilearn.org/courses")
var1=url1.json()
with open("cources.json","w") as f:
    json.dump(var1,f,indent=4)
serial_no=0
for i in var1:
    print(serial_no+1,i["name"],i["id"])
    serial_no+=1
course_no=int(input("enter your course number which you want to learn:-"))
print(var1[course_no-1]["name"],var1[course_no-1]["id"])
print()
n1=input("what you want p/n...")
if n1=="p":
    serial_no=0
    for i in var1:
        print(serial_no+1,i["name"],i["id"])
        serial_no+=1
    course_no=int(input("enter your course number which you want to learn:-"))
    print(var1[course_no-1]["name"],var1[course_no-1]["id"])
    n=input("enter p/n...")
    if n=='p':
        course_no=int(input("enter your course number which you want to learn:-"))
        print(var1[course_no-1]["name"],var1[course_no-1]["id"])
    else:
        a=var1[course_no-1]["id"]
        url2=requests.get("http://api.merakilearn.org/courses/"+str(a)+"/exercises")
        var2=url2.json()
        with open("topic.json","w") as f:
            json.dump(var2,f,indent=4)
        s_no=1
        main_point=[]
        sub_point=[]
        for j in var2["course"]["exercises"]:
            if j["parent_exercise_id"]==None:
                print(s_no,j["name"])
                print("   ",1,j["slug"])
                s_no+=1 
                main_point.append(j)
                sub_point.append(j)
                continue    
            if j["parent_exercise_id"]==j["id"]:
                print(s_no,j["name"])
                main_point.append(j)
                s_no+=1 
                c=0
            for i in  var2["course"]["exercises"]:
                if j["parent_exercise_id"]!=j["id"]:
                    print("   ",c+1,j["name"])
                    sub_point.append(j)
                    
                    c+=1
                    break 
else:
    a=var1[course_no-1]["id"]
    url2=requests.get("http://api.merakilearn.org/courses/"+str(a)+"/exercises")
    var2=url2.json()
    with open("topic.json","w") as f:
        json.dump(var2,f,indent=4)
    s_no=1
    main_point=[]
    sub_point=[]
    for j in var2["course"]["exercises"]:
        if j["parent_exercise_id"]==None:
            print(s_no,j["name"])
            print("   ",1,j["slug"])
            s_no+=1 
            main_point.append(j)
            sub_point.append(j)
            continue    
        if j["parent_exercise_id"]==j["id"]:
            print(s_no,j["name"])
            main_point.append(j)
            s_no+=1 
            c=0
        for i in  var2["course"]["exercises"]:
            if j["parent_exercise_id"]!=j["id"]:
                print("   ",c+1,j["name"])
                sub_point.append(j)
                
                c+=1
                break 
    with open("point.json","w") as q:
        json.dump(main_point,q,indent=4)
    topic_no=int(input("choose topic:-"))
    for k in range(0,len(main_point)):
        if topic_no==k+1:
            print(topic_no,main_point[k]["name"])
            print(main_point[k]["content"])
            a=main_point[k]["parent_exercise_id"]
    print()
    n2=input("what you want p/n...")
    if n2=="p":
        with open("point.json","w") as q:
            json.dump(main_point,q,indent=4)
        topic_no=int(input("choose topic:-"))
        for k in range(0,len(main_point)):
            if topic_no==k+1:
                print(topic_no,main_point[k]["name"])
                print(main_point[k]["content"])
                a=main_point[k]["parent_exercise_id"]

    else:
        s=1
        name=[]
        content=[]
        for d in range(0,len(sub_point)):
            if sub_point[d]["parent_exercise_id"]==a:
                print("   ",s,sub_point[d]["name"])
                name.append(sub_point[d]["name"])
                content.append(sub_point[d]["content"])
                s+=1
        print()
        point=int(input("choose a point:-"))
        y=1
        for i in range(0,len(name)):
            if point==y:
                print(name[i])
                print(content[i])
                print()
            y+=1
        n4=input("do you want to privious enter p...")
        if n4=="p":
            point=int(input("choose a point:-"))
            y=1
            for i in range(0,len(name)):
                if point==y:
                    print(name[i])
                    print(content[i])
                    print()
                y+=1


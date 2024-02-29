import json


def load_data():
    try:
        with open("Youtube.txt",'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []
    

def save_all_data(videos):
    with open("Youtube.txt",'w') as file :
        json.dump(videos, file )

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index,video in enumerate(videos , start = 1):
        print(f"{index}.{video['name']} , Duration : {video['time']}")
    print("\n")
    print("*" * 70)


def add_video(videos):
    name =  input("Enter video name : ")
    time =  input("Enter video duration : ")
    videos.append({'name': name , 'time': time})
    save_all_data(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number of youtube video you want to update : "))
    
    if 1 <= index <= len(videos):
        name = input("Enter video name :")
        time = input("Enter video duration :")
        videos[index-1] = {'name' : name , 'time' : time}
        save_all_data(videos)
    else:
        print("Invalid index. Select correct index!")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number of youtube video you want to Delete : "))

    if 1 <= index <= len(videos):
        del videos[index-1]
    else:
        print("Invalid index.")


def main():
    videos = load_data()
    while True :
        print("\nYoutube Manager | choose an option")
        print("1.List all Youtube Videos")
        print("2.Add a Youtube Video ")
        print("3.Update Youtube Video Details")
        print("4.Delete a Youtube Video")
        print("5.Exit the Program")
        choice =int(input("Enter your choice : "))

        match choice:
            case 1:
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                break
            case _:
                print("Invalid Choice !")

if __name__ == "__main__":
    main()
            

      
       
        
         



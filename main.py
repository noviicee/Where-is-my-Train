import requests

class IRCTC:

    def __init__(self):
        user_input=input("""How would you like to proceed?
        Enter 1 to check live train status.
        Enter 2 to check PNR.
        Enter 3 to check train schedule""")

        if user_input==1:
            print("Live train Status")
        elif user_input==2:
            print("PNR")
        else:
            self.trainSchedule()

    def trainSchedule(self):
        train_number=input("Enter the train number")
        self.fetchData(train_number)

    def fetchData(self,url):
        data=requests.get(url)

        data=data.json

        print(data)

if __name__=="__main__":
    obj=IRCTC()
    
from DAL.DB_Connection import execute

def main():
    print("Hello world")
    print(execute("select * from agents"))



if __name__ == "__main__":
    main()
import boto3
from time import sleep

def menu():
    boolean=0
    while(boolean==0):
        choice=input("Menu:\n1.List all AWS services by regions\n2.Create EC2 instances\n3.List all available regions\n4.Delete an instance\n5.Describe all AWS instances\n")
        if(choice=="1"):
            sa = 0
            while sa == 0:
                account = input("Do you want to list all services from your account(1) or from the default account(2)?\nWhat do you choose?(1/2)\n")
                if account == "1":
                    get_services(input("Enter aws_access_key:\n"),input("Enter aws_secret_key:\n"),input("Enter region name:\n"))
                    sleep(3)
                    sa=1
                    a=0
                    while a == 0:
                        back = input("Do you want to go back to the main menu?\n")
                        if back == "yes" or back == "Yes" or back == "YES" or back == "y":
                            print("Going back...")
                            sleep(1)
                            a=1
                        elif back == "no" or back == "No" or back == "NO" or back == "n":
                            print("ok!")
                            a=1
                            boolean=1
                        else:
                            print("Please choose yes or no")
                            sleep(1)
                elif account == "2":
                    get_my_services(input("Enter region name:\n"))
                    sleep(2)
                    sa=1
                    a=0
                    while a == 0:
                        back = input("Do you want to go back to the main menu?\n")
                        if back == "yes" or back == "Yes" or back == "YES" or back == "y":
                            print("Going back...")
                            sleep(1)
                            a=1
                        elif back == "no" or back == "No" or back == "NO" or back == "n":
                            print("ok!")
                            a=1
                            boolean=1
                        else:
                            print("Please choose yes or no")
                            sleep(1)
                else:
                    print("Please choose 1 or 2")
                    sleep(1)

        elif(choice=="2"):
            num = input("Enter how many instances:\n")
            deploy_instance(int(num),input("Enter type(t2.micro is for a free tier account):\n"),input("Enter AMI-ID:\n"))
            if num == "1":
                print(num + "instance successfully deployed!")
            elif num != "1":
                print(num + "instances successfully deployed!")
            sleep(1)
            a=0
            while a == 0:
                back = input("Do you want to go back to the main menu?\n")
                if back == "yes" or back == "Yes" or back == "YES" or back =="y":
                    print("Going back...")
                    sleep(1)
                    a = 1
                elif back == "no" or back == "No" or back == "NO" or back == "n":
                    print("ok!")
                    a = 1
                    boolean = 1
                else:
                    print("Please choose yes or no")
                    sleep(1)

        elif(choice=="3"):
            print("Here are all the AWS regions presented in a list:\n")
            regions_name()
            print(" ")
            sleep(1)
            a = 0
            while a == 0:
                back = input("Do you want to go back to the main menu?\n")
                if back == "yes" or back == "Yes" or back == "YES" or back == "y":
                    print("Going back...")
                    sleep(1)
                    a = 1
                elif back == "no" or back == "No" or back == "NO" or back == "n":
                    print("ok!")
                    a = 1
                    boolean = 1
                else:
                    print("Please choose yes or no")
                    sleep(1)
        elif(choice=="4"):
            delete_instance()
            print("Instance successfully deleted!")
            sleep(2)
            a = 0
            while a == 0:
                back = input("Do you want to go back to the main menu?\n")
                if back == "yes" or back == "Yes" or back == "YES" or back == "y":
                    print("Going back...")
                    sleep(1)
                    a = 1
                elif back == "no" or back == "No" or back == "NO" or back == "n":
                    print("ok!")

                    a = 1
                    boolean = 1
                else:
                    print("Please choose yes or no")
                    sleep(1)
        elif choice == "5":
            print("Getting all instances information...\n")
            sleep(2)
            describe_instances()
            a = 0
            while a == 0:
                back = input("Do you want to go back to the main menu?\n")
                if back == "yes" or back == "Yes" or back == "YES" or back == "y":
                    print("Going back...")
                    sleep(1)
                    a = 1
                elif back == "no" or back == "No" or back == "NO" or back == "n":
                    print("ok!")
                    a = 1
                    boolean = 1
                else:
                    print("Please choose yes or no")
                    sleep(1)
        elif choice == "exit" or choice == "Exit" or choice == "EXIT":
            boolean=1
        else:
            print("Enter 1-5 only!\n")
            print("Type exit to stop the menu")

def deploy_instance(num,type,ami):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
    ImageId=ami,
    MinCount=1,
    MaxCount=num,
    InstanceType=type)
    print("New instance ID is: " + instance[0].id)


def regions_name():
    client = boto3.client('ec2')
    regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    n = 0
    print("All regions available: \n")
    for i in regions:
        n = n + 1
        print(str(n) + ". " + i)
    return regions

def get_services(aws_access_key,aws_secret_key,region_name):
    session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=region_name)

    services = session.get_available_services()
    print("Available services for: " + region_name)
    n = 0
    for i in services:
        n = n + 1
        print(str(n) + ". " + i)


def get_my_services(region_name):
    session = boto3.Session(
        aws_access_key_id='AKIAI55QD2U75ZLDX6FA',
        aws_secret_access_key='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',
        region_name=region_name)

    services = session.get_available_services()
    print("Available services for: " + region_name)
    n = 0
    for i in services:
        n = n+1
        print(str(n) + ". " + i)

def delete_instance():
    ec2 = boto3.resource('ec2')
    newlist = []
    idss = input("Please enter the instance ID that you want to delete\n")
    newlist.append(idss)
    ec2.instances.filter(InstanceIds=newlist).terminate()

def describe_instances():
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        print(
            "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
                instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id,
                instance.state
            )
        )
exit="null"
while(exit!="yes" and exit!="YES"):
    menu()
    exit=input("Do you want to Exit? (yes/no)\n")

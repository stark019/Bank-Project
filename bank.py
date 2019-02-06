import Tkinter
from Tkinter import *
import random
import os

###################################### FILES TO STORE DATA ###########################################
file0=open("acnos.txt","a+")
file1=open("names.txt","a+")
file2=open("genderss.txt","a+")
file3=open("addresses.txt","a+")
file4=open("phnos.txt","a+")
file5=open("cities.txt","a+")
file6=open("branches.txt","a+")
file7=open("accountss.txt","a+")
file8=open("DOBs.txt","a+")
file9=open("Nationalties.txt","a+")
file10=open("Balances.txt","a+")
file11=open("pins.txt","a+")

#####################################################################################################

class Banking:
    def __init__(self):
        self.menu=Tk()
        self.menu.configure(bg="light green")
        self.menu.minsize(800,600)
        self.menuitem()
        
    def menuitem(self):
        

        self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
        self.blank.pack()

        self.header=Label(self.menu,text="CORPORATE BANK OF INDIA",fg="royal blue",bg="light green",font=["Algerian","45"])
        self.header.pack()

        self.mnu=Label(self.menu,text="MAIN MENU",fg="royal blue",bg="light green",font=["Gill sans ultra bold","30"])
        self.mnu.pack()

        self.blank=Label(self.menu,text="\n",fg="royal blue",bg="light green",font="Algerian")
        self.blank.pack()
 ##############################################DATA BASE MANAGEMENT####################################################################################################       
        
        def database_menu():
            for i in self.menu.winfo_children():
                i.destroy()
            self.hed2=Label(self.menu,text="Database Management Menu",fg="royal blue",bg="light green",font=["Gill sans ultra bold","40"])
            self.hed2.pack()

            self.blank=Label(self.menu,text="\n\n\n\n",fg="royal blue",bg="light green",font="Algerian")
            self.blank.pack()
                ##################################function to add data to the data base####################################
            def add_data_menu():                
                for i in self.menu.winfo_children():
                    i.destroy()
                self.hed3=Label(self.menu,text="New Member Form",fg="royal blue",bg="light green",font=["Gill sans ultra bold","40"])
                self.hed3.pack()
                
                                        ######################### The screen is now divided into 15 frames#######################

                self.frame1=Frame(self.menu)
                self.frame1.pack(side=TOP)
                self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                self.frame2=Frame(self.menu)
                self.frame2.pack(side=TOP)
                self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                self.frame3=Frame(self.menu)
                self.frame3.pack(side=TOP)
                self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                self.frame4=Frame(self.menu)
                self.frame4.pack(side=TOP)
                self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                self.frame5=Frame(self.menu)
                self.frame5.pack(side=TOP)
                self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                self.frame6=Frame(self.menu)
                self.frame6.pack(side=TOP)
                self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                self.frame7=Frame(self.menu)
                self.frame7.pack(side=TOP)
                self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                self.frame8=Frame(self.menu)
                self.frame8.pack(side=TOP)
                self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                self.frame9=Frame(self.menu)
                self.frame9.pack(side=TOP)
                self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                self.frame10=Frame(self.menu)
                self.frame10.pack(side=TOP)
                self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
            
                #############################################NEW MEMBER FORM#################################################################

                self.name_label=Label(self.frame1,text=("Name                           "),fg="black",bg="light green",font=["Fixedsys","18"])
                self.name_label.pack(side=LEFT )
                self.nameentry=Entry(self.frame1,bg="white",font=["","18"])
                self.nameentry.pack(side=LEFT)

                self.gender_label=Label(self.frame2,text=("Gender                         "),fg="black",bg="light green",font=["Fixedsys","18"])
                self.gender_label.pack(side=LEFT )
                self.genderentry=Entry(self.frame2,bg="white",font=["","18"])
                self.genderentry.pack(side=LEFT)

                self.adress_label=Label(self.frame3,text=("Address                        "),fg="black",bg="light green",font=["Fixedsys","18"])
                self.adress_label.pack(side=LEFT )
                self.adressentry=Entry(self.frame3,bg="white",font=["","18"])
                self.adressentry.pack(side=LEFT)

                self.phno_label=Label(self.frame4,text=(" Phone No.                    "),fg="black",bg="light green",font=["Fixedsys","18"])
                self.phno_label.pack(side=LEFT )
                self.phnoentry=Entry(self.frame4,bg="white",font=["","18"])
                self.phnoentry.pack(side=LEFT)

                self.city_label=Label(self.frame5,text=("City                          "),fg="black",bg="light green",font=["Fixedsys","18"])
                self.city_label.pack(side=LEFT )
                self.cityentry=Entry(self.frame5,bg="white",font=["","18"])
                self.cityentry.pack(side=LEFT)

                self.branch_label=Label(self.frame6,text=("Branch                           "),fg="black",bg="light green",font=["Fixedsys","18"])
                self.branch_label.pack(side=LEFT )
                self.branchentry=Entry(self.frame6,bg="white",font=["","18"])
                self.branchentry.pack(side=LEFT)

                self.ac_type_label=Label(self.frame7,text=("Account Type                           "),fg="black",bg="light green",font=["Fixedsys","18"])
                self.ac_type_label.pack(side=LEFT )
                self.ac_type_entry=Entry(self.frame7,bg="white",font=["","18"])
                self.ac_type_entry.pack(side=LEFT)

                self.dob_label=Label(self.frame8,text=("Date of Birth                           "),fg="black",bg="light green",font=["Fixedsys","18"])
                self.dob_label.pack(side=LEFT )
                self.dob_entry=Entry(self.frame8,bg="white",font=["","18"])
                self.dob_entry.pack(side=LEFT)

                self.nationality_label=Label(self.frame9,text=("Nationality                           "),fg="black",bg="light green",font=["Fixedsys","18"])
                self.nationality_label.pack(side=LEFT )
                self.nationality_entry=Entry(self.frame9,bg="white",font=["","18"])
                self.nationality_entry.pack(side=LEFT)

                self.balance_label=Label(self.frame10,text=("Balance                           "),fg="black",bg="light green",font=["Fixedsys","18"])
                self.balance_label.pack(side=LEFT )
                self.balance_entry=Entry(self.frame10,bg="white",font=["","18"])
                self.balance_entry.pack(side=LEFT)

                self.blank=Label(self.menu,text="\n\n\n",fg="royal blue",bg="light green",font="Algerian")
                self.blank.pack()

        #################################Submmiting Data to The Data Base#################################

                def submitdata():
                
                    self.namedata=self.nameentry.get()+"\n"
                    file1.write(self.namedata)
                    file1.close()

                    self.genderdata=self.genderentry.get()+"\n"
                    file2.write(self.genderdata)
                    file2.close()

                    self.adressdata=self.adressentry.get()+"\n"
                    file3.write(self.adressdata)
                    file3.close()

                    self.phnodata=self.phnoentry.get()+"\n"
                    file4.write(self.phnodata)
                    file4.close()

                    self.citydata=self.cityentry.get()+"\n"
                    file5.write(self.citydata)
                    file5.close()

                    self.branchdata=self.branchentry.get()+"\n"
                    file6.write(self.branchdata)
                    file6.close()

                    self.ac_typedata=self.ac_type_entry.get()+"\n"
                    file7.write(self.ac_typedata)
                    file7.close()

                    self.dob_data=self.dob_entry.get()+"\n"
                    file8.write(self.dob_data)
                    file8.close()

                    self.nationalitydata=self.nationality_entry.get()+"\n"
                    file9.write(self.nationalitydata)
                    file9.close()
                    
                    self.balancedata=self.balance_entry.get()+"\n"
                    file10.write(self.balancedata)
                    file10.close()

                    for i in self.menu.winfo_children():
                        i.destroy()
                    
                    self.message=Label(self.menu,text="\n\n\n\n\n\n\nYour data has been saved successfully",bg="light green",fg="red",font=["Cooper Black","20"])
                    self.message.pack()

                    l=file0.readlines()
                    for i in range (1,1000):
                        ac=random.randint(100000,999999)
                        acn=str(ac)+"\n"
                        if acn in l:
                            pass
                        else:
                            file0.write(acn)
                            break
                    file0.close()
                    self.message1=Label(self.menu,text="your account number is      "+acn,bg="light green",fg="red",font=["Cooper Black","20"])
                    self.message1.pack()
                    l1=file11.readlines()
                    for j in range (1,1000):
                        p=random.randint(1000,9999)
                        pin=str(p)+"\n"
                        if pin in l1:
                            pass
                        else:
                            file11.write(pin)
                            break
                    file11.close()
                    self.message2=Label(self.menu,text="your atm number is      "+pin,bg="light green",fg="red",font=["Cooper Black","20"])
                    self.message2.pack()
                    
                self.submitdatabutton= Button(self.menu,text="SUBMIT",fg="red",font=["Cooper Black","20"],command=submitdata)
                self.submitdatabutton.pack()

        ##########################################################################################
                                
            self.adddatabutton= Button(self.menu,text="Add New Account",fg="red",font=["Cooper Black","20"],command=add_data_menu)
            self.adddatabutton.pack()

            self.blank=Label(self.menu,text="\n\n\n\n\n",fg="royal blue",bg="light green",font="Algerian")
            self.blank.pack()
    ###########################################for searching and editing existing accounts#####################
            def editing():
                for x in self.menu.winfo_children():
                        x.destroy()
                
                self.search_label=Label(self.menu,text="   Search(via account number)     ",fg="black",bg="light green",font=["fixedsys","20"])
                self.search_label.pack()
                self.search_entry=Entry(self.menu,text="Search     ",fg="black",font=["fixedsys","20"])
                self.search_entry.pack()
                ##########################################SEARCHING IN THE DATABASE#########################
                def Search_item():
                    item=self.search_entry.get()
                    i=0
                    n=len(acno_list)-1
                    while i<=n:

                        ele=acno_list[i]
                        a=len(ele)-1
                        element=ele[0:a]

                        ele1=name_list[i]
                        a1=len(ele1)-1
                        element1=ele1[0:a1]

                        ele2=genders_list[i]
                        a2=len(ele2)-1
                        element2=ele2[0:a2]

                        ele3=addresses_list[i]
                        a3=len(ele3)-1
                        element3=ele3[0:a3]

                        ele4=phnos_list[i]
                        a4=len(ele4)-1
                        element4=ele4[0:a4]

                        ele5=cities_list[i]
                        a5=len(ele5)-1
                        element5=ele5[0:a5]

                        ele6=branches_list[i]
                        a6=len(ele6)-1
                        element6=ele6[0:a6]

                        ele7=accounts_list[i]
                        a7=len(ele7)-1
                        element7=ele7[0:a7]

                        ele8=DOB_list[i]
                        a8=len(ele8)-1
                        element8=ele8[0:a8]


                        ele9=nation_list[i]
                        a9=len(ele9)-1
                        element9=ele9[0:a9]

                        ele10=balance_list[i]
                        a10=len(ele10)-1
                        element10=ele10[0:a10]
                                
                        if item==element:
                            for x in self.menu.winfo_children():
                                x.destroy()
                            
                            self.frame1=Frame(self.menu)
                            self.frame1.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame2=Frame(self.menu)
                            self.frame2.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame3=Frame(self.menu)
                            self.frame3.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame4=Frame(self.menu)
                            self.frame4.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame5=Frame(self.menu)
                            self.frame5.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame6=Frame(self.menu)
                            self.frame6.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame7=Frame(self.menu)
                            self.frame7.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame8=Frame(self.menu)
                            self.frame8.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame9=Frame(self.menu)
                            self.frame9.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                

                            self.frame10=Frame(self.menu)
                            self.frame10.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")

                            self.frame11=Frame(self.menu)
                            self.frame11.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
            
                    
                            self.acno_found=Label(self.frame1,text="ACCOUNT No.-\t"+element,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)

                            self.name_found=Label(self.frame2,text="NAME.-\t"+element1,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.name_found.pack(side=LEFT)
                            def change_name():
                                for x in self.menu.winfo_children():
                                    x.destroy()
                                self.nname=Label(self.menu,text="Enter new data here-",bg="light green",fg="red",font=["Cooper Black","15"])
                                self.nname.pack()
                                
                                self.new_entry=Entry(self.menu,font=["Cooper Black","15"])
                                self.new_entry.pack()
                                
                                
                                def subbmit_name():
                                    z=0
                                    temp_file=open("temp.txt","w")
                                    self.new_name=self.new_entry.get()+"\n"
                                    file1.seek(0)
                                    while z<(n+1):
                                        
                                        rec=file1.readline()
                                        
                                        if z==i:
                                            temp_file.write(self.new_name)
                                            
                                        else:
                                            temp_file.write(rec)
                                        z=z+1
                                            
                                    temp_file.close()
                                    file1.close()
                                    os.remove("names.txt")
                                    os.rename("temp.txt","names.txt")
                                    mes=Label(self.menu,text="\n\n\n\n\n\n\n\n\nYour data has been changed successfully\nYou can Exit now",fg="red",bg="light green",font=["Cooper Black","18"])
                                    mes.pack()
                                self.sub=Button(self.menu,text="subbmit",fg="red",font=["Cooper Black","18"],command=subbmit_name)
                                self.sub.pack()
                            self.change1=Button(self.frame2,text="CHANGE",fg="red",font=["fixedsys","10"],command=change_name)
                            self.change1.pack(side=LEFT)

                            self.acno_found=Label(self.frame3,text="GENDER-\t"+element2,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
                            def change_gender():
                                for x in self.menu.winfo_children():
                                    x.destroy()
                                self.nentry=Label(self.menu,text="Enter new data here-",bg="light green",fg="red",font=["Cooper Black","15"])
                                self.nentry.pack()
                                
                                self.new_entry=Entry(self.menu,font=["Cooper Black","15"])
                                self.new_entry.pack()
                                
                                
                                def subbmit_gender():
                                    z=0
                                    temp_file=open("temp.txt","w")
                                    self.new_data=self.new_entry.get()+"\n"
                                    file2.seek(0)
                                    while z<(n+1):
                                        
                                        rec=file2.readline()
                                        
                                        if z==i:
                                            temp_file.write(self.new_data)
                                            
                                        else:
                                            temp_file.write(rec)
                                        z=z+1
                                            
                                    temp_file.close()
                                    file2.close()
                                    os.remove("genderss.txt")
                                    os.rename("temp.txt","genderss.txt")
                                    mes=Label(self.menu,text="\n\n\n\n\n\n\n\n\nYour data has been changed successfully\nYou can Exit now",fg="red",bg="light green",font=["Cooper Black","18"])
                                    mes.pack()
                                self.sub=Button(self.menu,text="subbmit",fg="red",font=["Cooper Black","18"],command=subbmit_gender)
                                self.sub.pack()
                            
                            self.change2=Button(self.frame3,text="CHANGE",fg="red",font=["fixedsys","10"],command=change_gender)
                            self.change2.pack(side=LEFT)

                            self.acno_found=Label(self.frame4,text="ADDRESS-\t"+element3,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
                            def change_Adress():
                                for x in self.menu.winfo_children():
                                    x.destroy()
                                self.nentry=Label(self.menu,text="Enter new data here-",bg="light green",fg="red",font=["Cooper Black","15"])
                                self.nentry.pack()
                                
                                self.new_entry=Entry(self.menu,font=["Cooper Black","15"])
                                self.new_entry.pack()
                                
                                
                                def subbmit_adress():
                                    z=0
                                    temp_file=open("temp.txt","w")
                                    self.new_data=self.new_entry.get()+"\n"
                                    file3.seek(0)
                                    while z<(n+1):
                                        
                                        rec=file3.readline()
                                        
                                        if z==i:
                                            temp_file.write(self.new_data)
                                            
                                        else:
                                            temp_file.write(rec)
                                        z=z+1
                                            
                                    temp_file.close()
                                    file3.close()
                                    os.remove("addresses.txt")
                                    os.rename("temp.txt","addresses.txt")
                                    mes=Label(self.menu,text="\n\n\n\n\n\n\n\n\nYour data has been changed successfully\nYou can Exit now",fg="red",bg="light green",font=["Cooper Black","18"])
                                    mes.pack()
                                self.sub=Button(self.menu,text="subbmit",fg="red",font=["Cooper Black","18"],command=subbmit_adress)
                                self.sub.pack()
                            
                            
                            self.change1=Button(self.frame4,text="CHANGE",fg="red",font=["fixedsys","10"],command=change_Adress)
                            self.change1.pack(side=LEFT)

                            self.acno_found=Label(self.frame5,text="PHONE No.-\t"+element4,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
                            def change_phno():#####
                                for x in self.menu.winfo_children():
                                    x.destroy()
                                self.nentry=Label(self.menu,text="Enter new data here-",bg="light green",fg="red",font=["Cooper Black","15"])
                                self.nentry.pack()
                                
                                self.new_entry=Entry(self.menu,font=["Cooper Black","15"])
                                self.new_entry.pack()
                                
                                
                                def subbmit_phno():
                                    z=0
                                    temp_file=open("temp.txt","w")
                                    self.new_data=self.new_entry.get()+"\n"
                                    file4.seek(0)
                                    while z<(n+1):
                                        
                                        rec=file4.readline()
                                        
                                        if z==i:
                                            temp_file.write(self.new_data)
                                            
                                        else:
                                            temp_file.write(rec)
                                        z=z+1
                                            
                                    temp_file.close()
                                    file4.close()
                                    os.remove("phnos.txt")
                                    os.rename("temp.txt","phnos.txt")
                                    mes=Label(self.menu,text="\n\n\n\n\n\n\n\n\nYour data has been changed successfully\nYou can Exit now",fg="red",bg="light green",font=["Cooper Black","18"])
                                    mes.pack()
                                self.sub=Button(self.menu,text="subbmit",fg="red",font=["Cooper Black","18"],command=subbmit_phno)
                                self.sub.pack()
                            
                            
                            
                                
                            self.change1=Button(self.frame5,text="CHANGE",fg="red",font=["fixedsys","10"],command=change_phno)
                            self.change1.pack(side=LEFT)

                            self.acno_found=Label(self.frame6,text="CITY-\t"+element5,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
                            def change_city():####
                                for x in self.menu.winfo_children():
                                    x.destroy()
                                self.nentry=Label(self.menu,text="Enter new data here-",bg="light green",fg="red",font=["Cooper Black","15"])
                                self.nentry.pack()
                                
                                self.new_entry=Entry(self.menu,font=["Cooper Black","15"])
                                self.new_entry.pack()
                                
                                
                                def subbmit_city():
                                    z=0
                                    temp_file=open("temp.txt","w")
                                    self.new_data=self.new_entry.get()+"\n"
                                    file5.seek(0)
                                    while z<(n+1):
                                        
                                        rec=file5.readline()
                                        
                                        if z==i:
                                            temp_file.write(self.new_data)
                                            
                                        else:
                                            temp_file.write(rec)
                                        z=z+1
                                            
                                    temp_file.close()
                                    file5.close()
                                    os.remove("cities.txt")
                                    os.rename("temp.txt","cities.txt")
                                    mes=Label(self.menu,text="\n\n\n\n\n\n\n\n\nYour data has been changed successfully\nYou can Exit now",fg="red",bg="light green",font=["Cooper Black","18"])
                                    mes.pack()
                                self.sub=Button(self.menu,text="subbmit",fg="red",font=["Cooper Black","18"],command=subbmit_city)
                                self.sub.pack()
                            
                            
                                
                            self.change1=Button(self.frame6,text="CHANGE",fg="red",font=["fixedsys","10"],command=change_city)
                            self.change1.pack(side=LEFT)

                            self.acno_found=Label(self.frame7,text="BRANCH-\t"+element6,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
                            def change_branch():####
                                for x in self.menu.winfo_children():
                                    x.destroy()
                                self.nentry=Label(self.menu,text="Enter new data here-",bg="light green",fg="red",font=["Cooper Black","15"])
                                self.nentry.pack()
                                
                                self.new_entry=Entry(self.menu,font=["Cooper Black","15"])
                                self.new_entry.pack()
                                
                                
                                def subbmit_branch():
                                    z=0
                                    temp_file=open("temp.txt","w")
                                    self.new_data=self.new_entry.get()+"\n"
                                    file6.seek(0)
                                    while z<(n+1):
                                        
                                        rec=file6.readline()
                                        
                                        if z==i:
                                            temp_file.write(self.new_data)
                                            
                                        else:
                                            temp_file.write(rec)
                                        z=z+1
                                            
                                    temp_file.close()
                                    file6.close()
                                    os.remove("branches.txt")
                                    os.rename("temp.txt","branches.txt")
                                    mes=Label(self.menu,text="\n\n\n\n\n\n\n\n\nYour data has been changed successfully\nYou can Exit now",fg="red",bg="light green",font=["Cooper Black","18"])
                                    mes.pack()
                                self.sub=Button(self.menu,text="subbmit",fg="red",font=["Cooper Black","18"],command=subbmit_branch)
                                self.sub.pack()
                            
                            
                            
                            self.change1=Button(self.frame7,text="CHANGE",fg="red",font=["fixedsys","10"],command=change_branch)
                            self.change1.pack(side=LEFT)

                            self.acno_found=Label(self.frame8,text="ACCOUNT TYPE-\t"+element7,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
                            def change_acty():####
                                for x in self.menu.winfo_children():
                                    x.destroy()
                                self.nentry=Label(self.menu,text="Enter new data here-",bg="light green",fg="red",font=["Cooper Black","15"])
                                self.nentry.pack()
                                
                                self.new_entry=Entry(self.menu,font=["Cooper Black","15"])
                                self.new_entry.pack()
                                
                                
                                def subbmit_acty():
                                    z=0
                                    temp_file=open("temp.txt","w")
                                    self.new_data=self.new_entry.get()+"\n"
                                    file7.seek(0)
                                    while z<(n+1):
                                        
                                        rec=file7.readline()
                                        
                                        if z==i:
                                            temp_file.write(self.new_data)
                                            
                                        else:
                                            temp_file.write(rec)
                                        z=z+1
                                            
                                    temp_file.close()
                                    file7.close()
                                    os.remove("accountss.txt")
                                    os.rename("temp.txt","accountss.txt")
                                    mes=Label(self.menu,text="\n\n\n\n\n\n\n\n\nYour data has been changed successfully\nYou can Exit now",fg="red",bg="light green",font=["Cooper Black","18"])
                                    mes.pack()
                                self.sub=Button(self.menu,text="subbmit",fg="red",font=["Cooper Black","18"],command=subbmit_acty)
                                self.sub.pack()
                            
                            
                            
                        
                                
                            self.change1=Button(self.frame8,text="CHANGE",fg="red",font=["fixedsys","10"],command=change_acty)
                            self.change1.pack(side=LEFT)

                            self.acno_found=Label(self.frame9,text="DOB-\t"+element8,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
                            def change_DOB():####
                                for x in self.menu.winfo_children():
                                    x.destroy()
                                self.nentry=Label(self.menu,text="Enter new data here-",bg="light green",fg="red",font=["Cooper Black","15"])
                                self.nentry.pack()
                                
                                self.new_entry=Entry(self.menu,font=["Cooper Black","15"])
                                self.new_entry.pack()
                                
                                
                                def subbmit_DOB():
                                    z=0
                                    temp_file=open("temp.txt","w")
                                    self.new_data=self.new_entry.get()+"\n"
                                    file8.seek(0)
                                    while z<(n+1):
                                        
                                        rec=file8.readline()
                                        
                                        if z==i:
                                            temp_file.write(self.new_data)
                                            
                                        else:
                                            temp_file.write(rec)
                                        z=z+1
                                            
                                    temp_file.close()
                                    file8.close()
                                    os.remove("DOBs.txt")
                                    os.rename("temp.txt","DOBs.txt")
                                    mes=Label(self.menu,text="\n\n\n\n\n\n\n\n\nYour data has been changed successfully\nYou can Exit now",fg="red",bg="light green",font=["Cooper Black","18"])
                                    mes.pack()
                                self.sub=Button(self.menu,text="subbmit",fg="red",font=["Cooper Black","18"],command=subbmit_DOB)
                                self.sub.pack()
                            
                            
                            
                            self.change1=Button(self.frame9,text="CHANGE",fg="red",font=["fixedsys","10"],command=change_DOB)
                            self.change1.pack(side=LEFT)

                            self.acno_found=Label(self.frame10,text="NATIONALITY-\t"+element9,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
                            def change_nation():####
                                for x in self.menu.winfo_children():
                                    x.destroy()
                                self.nentry=Label(self.menu,text="Enter new data here-",bg="light green",fg="red",font=["Cooper Black","15"])
                                self.nentry.pack()
                                
                                self.new_entry=Entry(self.menu,font=["Cooper Black","15"])
                                self.new_entry.pack()
                                
                                
                                def subbmit_nation():
                                    z=0
                                    temp_file=open("temp.txt","w")
                                    self.new_data=self.new_entry.get()+"\n"
                                    file9.seek(0)
                                    while z<(n+1):
                                        
                                        rec=file9.readline()
                                        
                                        if z==i:
                                            temp_file.write(self.new_data)
                                            
                                        else:
                                            temp_file.write(rec)
                                        z=z+1
                                            
                                    temp_file.close()
                                    file9.close()
                                    os.remove("Nationalties.txt")
                                    os.rename("temp.txt","Nationalties.txt")
                                    mes=Label(self.menu,text="\n\n\n\n\n\n\n\n\nYour data has been changed successfully\nYou can Exit now",fg="red",bg="light green",font=["Cooper Black","18"])
                                    mes.pack()
                                self.sub=Button(self.menu,text="subbmit",fg="red",font=["Cooper Black","18"],command=subbmit_nation)
                                self.sub.pack()
                            
                            
                            
                                
                            self.change1=Button(self.frame10,text="CHANGE",fg="red",font=["fixedsys","10"],command=change_nation)
                            self.change1.pack(side=LEFT)

                            self.acno_found=Label(self.frame11,text="BALANCE-\t"+element10,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
                            
                            break
                        else:
                            for x in self.menu.winfo_children():
                                x.destroy()
                            pass
                        i=i+1
                    else:
                        self.mes_not_found=Label(self.menu,text="\n\n\n\nSorry ! we have no such account\n\nYou may exit now",bg="light green",fg="red",font=["Cooper Black","15"])
                        self.mes_not_found.pack()             

                self.search_button=Button(self.menu,text="Search",fg="red",font=["fixedsys","15"],command=Search_item)
                self.search_button.pack()
                    ##########################################STORING DATA IN LIST BOXES FOR DISPLAY############################
                self.lbox = Listbox(self.menu, width=20, height=420)
                self.lbox.pack(side=LEFT)
                acno_list=file0.readlines()
                
                n=len(acno_list)
                for j in range (0,n):
                    ele=acno_list[j]
                    self.lbox.insert(j,ele)

                self.lbox = Listbox(self.menu, width=20, height=420)
                self.lbox.pack(side=LEFT)
                name_list=file1.readlines()
                n=len(name_list)
                for j in range (0,n):
                    ele=name_list[j]
                    self.lbox.insert(j,ele)

                self.lbox2 = Listbox(self.menu, width=20, height=420)
                self.lbox2.pack(side=LEFT)
                genders_list=file2.readlines()
                n=len(genders_list)
                for j in range (0,n):
                    ele=genders_list[j]
                    self.lbox2.insert(j,ele)

                self.lbox3 = Listbox(self.menu, width=20, height=420)
                self.lbox3.pack(side=LEFT)
                addresses_list=file3.readlines()
                n=len(addresses_list)
                for j in range (0,n):
                    ele=addresses_list[j]
                    self.lbox3.insert(j,ele)

                self.lbox4 = Listbox(self.menu, width=20, height=420)
                self.lbox4.pack(side=LEFT)
                phnos_list=file4.readlines()
                n=len(phnos_list)
                for j in range (0,n):
                    ele=phnos_list[j]
                    self.lbox4.insert(j,ele)

                self.lbox20 = Listbox(self.menu, width=20, height=420)
                self.lbox20.pack(side=LEFT)
                cities_list=file5.readlines()
                n=len(cities_list)
                for j in range (0,n):
                    ele=cities_list[j]
                    self.lbox20.insert(j,ele)

                self.lbox6 = Listbox(self.menu, width=20, height=420)
                self.lbox6.pack(side=LEFT)
                branches_list=file6.readlines()
                n=len(branches_list)
                for j in range (0,n):
                    ele=branches_list[j]
                    self.lbox6.insert(j,ele)

                self.lbox7 = Listbox(self.menu, width=20, height=420)
                self.lbox7.pack(side=LEFT)
                accounts_list=file7.readlines()
                n=len(accounts_list)
                for j in range (0,n):
                    ele=accounts_list[j]
                    self.lbox7.insert(j,ele)

                self.lbox8 = Listbox(self.menu, width=20, height=420)
                self.lbox8.pack(side=LEFT)
                DOB_list=file8.readlines()
                n=len(DOB_list)
                for j in range (0,n):
                    ele=DOB_list[j]
                    self.lbox8.insert(j,ele)

                self.lbox9 = Listbox(self.menu, width=20, height=420)
                self.lbox9.pack(side=LEFT)
                nation_list=file9.readlines()
                n=len(nation_list)
                for j in range (0,n):
                    ele=nation_list[j]
                    self.lbox9.insert(j,ele)

                self.lbox10 = Listbox(self.menu, width=20, height=420)
                self.lbox10.pack(side=LEFT)
                balance_list=file10.readlines()
                n=len(balance_list)
                for j in range (0,n):
                    ele=balance_list[j]
                    self.lbox10.insert(j,ele)
                ###################################################################
            self.editdatabutton= Button(self.menu,text="Edit Exesting Account",fg="red",font=["Cooper Black","20"],command=editing)
            self.editdatabutton.pack()
        self.databasebutton= Button(self.menu,text="Data Base Management",fg="red",font=["Cooper Black","20"],command=database_menu)
        self.databasebutton.pack()

        self.blank=Label(self.menu,text="\n",fg="royal blue",bg="light green",font="Algerian")
        self.blank.pack()
######################################################################################################################
        def searching():
                for x in self.menu.winfo_children():
                        x.destroy()
                
                self.search_label=Label(self.menu,text="   Search(via ac number)     ",fg="black",bg="light green",font=["fixedsys","20"])
                self.search_label.pack()
                self.search_entry=Entry(self.menu,text="Search     ",fg="black",font=["fixedsys","20"])
                self.search_entry.pack()
                ##########################################SEARCHING IN THE DATABASE#########################################
                def Search_item():
                    item=self.search_entry.get()
                    i=0
                    n=len(acno_list)
                    while i<n:

                        ele=acno_list[i]
                        a=len(ele)-1
                        element=ele[0:a]

                        ele1=name_list[i]
                        a1=len(ele1)-1
                        element1=ele1[0:a1]

                        ele2=genders_list[i]
                        a2=len(ele2)-1
                        element2=ele2[0:a2]

                        ele3=addresses_list[i]
                        a3=len(ele3)-1
                        element3=ele3[0:a3]

                        ele4=phnos_list[i]
                        a4=len(ele4)-1
                        element4=ele4[0:a4]

                        ele5=cities_list[i]
                        a5=len(ele5)-1
                        element5=ele5[0:a5]

                        ele6=branches_list[i]
                        a6=len(ele6)-1
                        element6=ele6[0:a6]

                        ele7=accounts_list[i]
                        a7=len(ele7)-1
                        element7=ele7[0:a7]

                        ele8=DOB_list[i]
                        a8=len(ele8)-1
                        element8=ele8[0:a8]

                        ele9=nation_list[i]
                        a9=len(ele9)-1
                        element9=ele9[0:a9]

                        ele10=balance_list[i]
                        a10=len(ele10)-1
                        element10=ele10[0:a10]
                    
                        if item==element:
                            for x in self.menu.winfo_children():
                                x.destroy()
                            
                            self.frame1=Frame(self.menu)
                            self.frame1.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame2=Frame(self.menu)
                            self.frame2.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame3=Frame(self.menu)
                            self.frame3.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame4=Frame(self.menu)
                            self.frame4.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame5=Frame(self.menu)
                            self.frame5.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame6=Frame(self.menu)
                            self.frame6.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame7=Frame(self.menu)
                            self.frame7.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame8=Frame(self.menu)
                            self.frame8.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame9=Frame(self.menu)
                            self.frame9.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")
                
                            self.frame10=Frame(self.menu)
                            self.frame10.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")

                            self.frame11=Frame(self.menu)
                            self.frame11.pack(side=TOP)
                            self.blank=Label(self.menu,text="",fg="royal blue",bg="light green",font="Algerian")            
                    
                            self.acno_found=Label(self.frame1,text="ACCOUNT No.-\t"+element,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)

                            self.name_found=Label(self.frame2,text="NAME.-\t"+element1,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.name_found.pack(side=LEFT)
                            
                            self.acno_found=Label(self.frame3,text="GENDER-\t"+element2,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
                            
                            self.acno_found=Label(self.frame4,text="ADDRESS-\t"+element3,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)

                            self.acno_found=Label(self.frame5,text="PHONE No.-\t"+element4,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
                                
                            self.acno_found=Label(self.frame6,text="CITY-\t"+element5,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
                                
                            self.acno_found=Label(self.frame7,text="BRANCH-\t"+element6,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
                            
                            self.acno_found=Label(self.frame8,text="ACCOUNT TYPE-\t"+element7,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
                        
                            self.acno_found=Label(self.frame9,text="DOB-\t"+element8,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
                            
                            self.acno_found=Label(self.frame10,text="NATIONALITY-\t"+element9,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
                                
                            self.acno_found=Label(self.frame11,text="BALANCE-\t"+element10,bg="light green",fg="red",font=["Cooper Black","15"])
                            self.acno_found.pack(side=LEFT)
    
                            break
                            
                        else:
                            for x in self.menu.winfo_children():
                                x.destroy()
                            pass
                        i=i+1
                    else:
                        self.acnot_found=Label(self.menu,text="\n\n\nSORRY ! Any reccord did not matched with your search\n\nYou may exit now",bg="light green",fg="red",font=["Cooper Black","15"])
                        self.acnot_found.pack()
    
                        
                    
                self.search_button=Button(self.menu,text="Search",fg="red",font=["fixedsys","15"],command=Search_item)
                self.search_button.pack()
                    ##########################################STORING DATA IN LIST BOXES FOR DISPLAY############################
                self.lbox = Listbox(self.menu, width=20, height=420)
                self.lbox.pack(side=LEFT)
                acno_list=file0.readlines()
                
                n=len(acno_list)
                for j in range (0,n):
                    ele=acno_list[j]
                    self.lbox.insert(j,ele)

                self.lbox = Listbox(self.menu, width=20, height=420)
                self.lbox.pack(side=LEFT)
                name_list=file1.readlines()
                n=len(name_list)
                for j in range (0,n):
                    ele=name_list[j]
                    self.lbox.insert(j,ele)

                self.lbox2 = Listbox(self.menu, width=20, height=420)
                self.lbox2.pack(side=LEFT)
                genders_list=file2.readlines()
                n=len(genders_list)
                for j in range (0,n):
                    ele=genders_list[j]
                    self.lbox2.insert(j,ele)

                self.lbox3 = Listbox(self.menu, width=20, height=420)
                self.lbox3.pack(side=LEFT)
                addresses_list=file3.readlines()
                n=len(addresses_list)
                for j in range (0,n):
                    ele=addresses_list[j]
                    self.lbox3.insert(j,ele)

                self.lbox4 = Listbox(self.menu, width=20, height=420)
                self.lbox4.pack(side=LEFT)
                phnos_list=file4.readlines()
                n=len(phnos_list)
                for j in range (0,n):
                    ele=phnos_list[j]
                    self.lbox4.insert(j,ele)

                self.lbox20 = Listbox(self.menu, width=20, height=420)
                self.lbox20.pack(side=LEFT)
                cities_list=file5.readlines()
                n=len(cities_list)
                for j in range (0,n):
                    ele=cities_list[j]
                    self.lbox20.insert(j,ele)

                self.lbox6 = Listbox(self.menu, width=20, height=420)
                self.lbox6.pack(side=LEFT)
                branches_list=file6.readlines()
                n=len(branches_list)
                for j in range (0,n):
                    ele=branches_list[j]
                    self.lbox6.insert(j,ele)

                self.lbox7 = Listbox(self.menu, width=20, height=420)
                self.lbox7.pack(side=LEFT)
                accounts_list=file7.readlines()
                n=len(accounts_list)
                for j in range (0,n):
                    ele=accounts_list[j]
                    self.lbox7.insert(j,ele)

                self.lbox8 = Listbox(self.menu, width=20, height=420)
                self.lbox8.pack(side=LEFT)
                DOB_list=file8.readlines()
                n=len(DOB_list)
                for j in range (0,n):
                    ele=DOB_list[j]
                    self.lbox8.insert(j,ele)

                self.lbox9 = Listbox(self.menu, width=20, height=420)
                self.lbox9.pack(side=LEFT)
                nation_list=file9.readlines()
                n=len(nation_list)
                for j in range (0,n):
                    ele=nation_list[j]
                    self.lbox9.insert(j,ele)

                self.lbox10 = Listbox(self.menu, width=20, height=420)
                self.lbox10.pack(side=LEFT)
                balance_list=file10.readlines()
                n=len(balance_list)
                for j in range (0,n):
                    ele=balance_list[j]
                    self.lbox10.insert(j,ele)
            
        self.searchbutton= Button(self.menu,text="                Search                ",fg="red",font=["Cooper Black","20"],command=searching)
        self.searchbutton.pack()

        self.blank=Label(self.menu,text="\n",fg="royal blue",bg="light green",font="Algerian")
        self.blank.pack()
        def Transection():    
            for x in self.menu.winfo_children():
                x.destroy()
            
            self.blank=Label(self.menu,text="\n\n\n",fg="royal blue",bg="light green",font="Algerian")
            self.blank.pack()
            #################################Deposit#############################
            def deposit():
                for x in self.menu.winfo_children():
                    x.destroy()
                self.frame1=Frame(self.menu,bg="light green")
                self.frame1.pack(side=TOP)
                self.frame2=Frame(self.menu,bg="light green")
                self.frame2.pack(side=TOP)
                self.frame3=Frame(self.menu,bg="light green")
                self.frame3.pack(side=TOP)
                self.blank=Label(self.frame1,text="\n\n\n",fg="royal blue",bg="light green",font="Algerian")
                self.blank.pack()

                self.ac_no=Label(self.frame1,text="Acoount Number",fg="red",bg="light green",font=["Cooper Black","15"])
                self.ac_no.pack(side=LEFT)
                self.ac_noent=Entry(self.frame1,text="Acoount Number",font=["Cooper Black","15"])
                self.ac_noent.pack(side=LEFT)
                self.amount=Label(self.frame2,text="Amount",fg="red",bg="light green",font=["Cooper Black","15"])
                self.amount.pack(side=LEFT)
                self.amountent=Entry(self.frame2,font=["Cooper Black","15"])
                self.amountent.pack(side=LEFT)
                self.pin=Label(self.frame3,text="Pin Number",fg="red",bg="light green",font=["Cooper Black","15"])
                self.pin.pack(side=LEFT)
                self.pinent=Entry(self.frame3,font=["Cooper Black","15"])
                self.pinent.pack(side=LEFT)
                def deposit_done():
                    self.acno_list=file0.readlines()
                    self.pin_list=file11.readlines()
                    self.bal_list=file10.readlines()
                    ac=self.ac_noent.get()+"\n"
                    pn=self.pinent.get()+"\n"
                    amount=int(self.amountent.get())
                    i=0
                    n=len(self.acno_list)-1
                    file10.seek(0)
                    file11.seek(0)
                    file0.seek(0)
                    while i<=n:

                        balance=self.bal_list[i]
                        a=len(balance)-1
                        present_balance=int(balance[0:a])
                        present_bal=balance[0:a]
                        net_amount=str(amount+present_balance)+"\n"
                        
                    
                        
                        temp_file=open("temp.txt","a")
                    
                                        
                        
                        if self.acno_list[i]==ac and self.pin_list[i]==pn:
                            temp_file.write(net_amount)
                            
                            
                            
                        else:
                            temp_file.write(balance)
                        if i==n:
                            pass
                        i=i+1
                    else:
                        mes_=Label(self.menu,text="\n\n\nInvalid Transection\nYou can Exit now\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",fg="red",bg="light green",font=["Cooper Black","18"])
                        mes_.pack()                  
                    temp_file.close()
                    file10.close()
                    os.remove("Balances.txt")
                    os.rename("temp.txt","Balances.txt")
                    mes=Label(self.menu,text="\n\nYour successfully deposited your money\nYou can Exit now",fg="red",bg="light green",font=["Cooper Black","18"])
                    mes.pack()
                
                self.done=Button(self.menu,text="Done",fg="black",font=["Cooper Black","15"],command=deposit_done)
                self.done.pack()    
                
            self.deposit_button=Button(self.menu,text="Deposit",fg="black",font=["Cooper Black","15"],command=deposit)
            self.deposit_button.pack()
            ############################################################################
            
            self.blank=Label(self.menu,text="\n",fg="royal blue",bg="light green",font="Algerian")
            self.blank.pack()
            ###############################Withdrawl##########################
            def withdrawl():
                for x in self.menu.winfo_children():
                    x.destroy()
                self.frame1=Frame(self.menu,bg="light green")
                self.frame1.pack(side=TOP)
                self.frame2=Frame(self.menu,bg="light green")
                self.frame2.pack(side=TOP)
                self.frame3=Frame(self.menu,bg="light green")
                self.frame3.pack(side=TOP)
                self.blank=Label(self.frame1,text="\n\n\n",fg="royal blue",bg="light green",font="Algerian")
                self.blank.pack()

                self.ac_no=Label(self.frame1,text="Acoount Number",fg="red",bg="light green",font=["Cooper Black","15"])
                self.ac_no.pack(side=LEFT)
                self.ac_noent=Entry(self.frame1,text="Acoount Number",font=["Cooper Black","15"])
                self.ac_noent.pack(side=LEFT)
                self.amount=Label(self.frame2,text="Amount",fg="red",bg="light green",font=["Cooper Black","15"])
                self.amount.pack(side=LEFT)
                self.amountent=Entry(self.frame2,font=["Cooper Black","15"])
                self.amountent.pack(side=LEFT)
                self.pin=Label(self.frame3,text="Pin Number",fg="red",bg="light green",font=["Cooper Black","15"])
                self.pin.pack(side=LEFT)
                self.pinent=Entry(self.frame3,font=["Cooper Black","15"])
                self.pinent.pack(side=LEFT)
                def withdrawl_done():
                    self.acno_list=file0.readlines()
                    self.pin_list=file11.readlines()
                    self.bal_list=file10.readlines()
                    ac=self.ac_noent.get()+"\n"
                    pn=self.pinent.get()+"\n"
                    amount=int(self.amountent.get())
                    i=0
                    n=len(self.acno_list)-1
                    file10.seek(0)
                    while i<=n:
                        balance=self.bal_list[i]
                        a=len(balance)-1
                        present_balance=int(balance[0:a])
                        present_bal=balance[0:a]
                        net_amount=str(present_balance-amount)+"\n"
                        temp_file=open("temp.txt","a")
                        if self.acno_list[i]==ac and self.pin_list[i]==pn:
                            if int(net_amount)<0:
                                mes1=Label(self.menu,text="\n\n\n\n\n\n\n\n\nInsufficient Balancce\nYou can Exit now",fg="red",bg="light green",font=["Cooper Black","18"])
                                mes1.pack()
                                break
                                
                            else:
                                temp_file.write(net_amount)    
                        else:
                            temp_file.write(balance)
                        if i==n:
                            pass
                        i=i+1
                    else:
                        mes_=Label(self.menu,text="\nInvalid Transection\nYou can Exit now\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",fg="red",bg="light green",font=["Cooper Black","18"])
                        mes_.pack()
                        
                    temp_file.close()
                    file10.close()
                    os.remove("Balances.txt")
                    os.rename("temp.txt","Balances.txt")
                    mes=Label(self.menu,text="\n\n\n\n\n\n\n\n\nYour successfully Withdrawl your money\nYou can Exit now",fg="red",bg="light green",font=["Cooper Black","18"])
                    mes.pack()
                self.done=Button(self.menu,text="Done",fg="black",font=["Cooper Black","15"],command=withdrawl_done)
                self.done.pack()    
            self.withdrawl_button=Button(self.menu,text="Withdrawl",fg="black",font=["Cooper Black","15"],command=withdrawl)
            self.withdrawl_button.pack()
        self.transectionbutton= Button(self.menu,text="Transection",fg="red",font=["Cooper Black","20"],command=Transection)
        self.transectionbutton.pack()

        self.blank=Label(self.menu,text="\n",fg="royal blue",bg="light green",font="Algerian")
        self.blank.pack()
        def about():
            for x in self.menu.winfo_children():
                x.destroy()
            msg1=Label(self.menu,text="\n\nAbout",fg="red",bg="light green",font=["jokerman","45"])
            msg1.pack()
            
            doc="""\n\n
This Project on virtual Banking System is collecctively developed by the group of four students\n
Names- Nihal Pandey,Saurabh Agarawall,Atif Riaz Khan & Deepak Kumar of Class XII,\n
G.N.National Public School, Gorakhpur under the guidance and supervision of Mr. Manoj Gupta\n
as a project in Computer Science (083),C.B.S.E eaxmination 2016-2017"""
            msg=Label(self.menu,text=doc,font=["viner hand ITC","15"],fg="black",bg="light green")
            msg.pack()
            
        self.aboutbutton= Button(self.menu,text="About",fg="red",font=["Cooper Black","20"],command=about)
        self.aboutbutton.pack()

        self.blank=Label(self.menu,text="\n",fg="royal blue",bg="light green",font="Algerian")
        self.blank.pack()
        def exitb():
            self.menu.destroy()
            
        self.exitbutton= Button(self.menu,text="exit",fg="red",font=["Cooper Black","20"],command=exitb)
        self.exitbutton.pack()
        
        self.menu.mainloop()
b1=Banking()

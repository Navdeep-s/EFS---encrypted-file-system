import os,sys
import subprocess
import threading



class worker():

	def __init__(self, path):
		self.key_path = path
		self.dic = {}


	def decrypt(self,name):
		u = os.getcwd()
		r = os.path.join(u,name)
		# print("hi ")
		try:
			completed = subprocess.run(
			f'echo {self.key_path} | fast_encryption1 "{r}"',
			check=True,
			shell=True,
			stdout=subprocess.PIPE,
			)
		except Exception as e:
			# print(e)
			# print(completed)
			return -1

		# message = os.system(f'echo {self.key_path} | fast_encryption1 "{r}"')
		# if(message!=0):
			# print("boss")
			# return -1
		# print(message)
		# print("hey there")
		# os.remove(r)
		# os.rename(r+".enc",r)

	def read(self,name,parent=""):
		if(self.decrypt(name)!=-1):
			y = open(name+".enc","r")
			# print(y)
			u =y.read()
			# print(u,"jhey")
			y.close()
			# print(u)

			os.remove(name+".enc")

			
			for k in u.splitlines():
				o = k.split(" : ")
				# print(k)

				try:
					self.dic[o[1]] = os.path.join(parent,o[0])
				except Exception as e:
					print(e)
					pass
		else:
			# print("dhoka hoeyga mere naal")
			pass

			
			





# some = worker(key_path)
# some.decrypt("cahce.dat")

# some.read("data.dll","data_1")


class mover():
	def __init__(self,path):
		self.path =  os.getcwd()
		self.reader = worker(path)


	def get_file(self,path,file="data.dll"):

		os.chdir(path)
		self.reader.read(file,path)

		os.chdir(self.path)


	def scan_all(self):
		y = os.listdir()
		self.get_file(".")
		count = 0
		for u in y:
			# print(u)
			if os.path.isdir(u):
				# print(u)
				# print(u)
				self.get_file(u)
				count = count+1
		# print(self.reader.dic)
		# print(count)


		y = open("cache.dat","w")

		for k in self.reader.dic.keys():
			y.write(f"{self.reader.dic[k]} : {k}\n")
		y.close()

		file_name1 = "cache.dat"

		self.reader.decrypt(file_name1)
		os.remove(file_name1)

		# print(os.listdir())
		# print("file has been written")
		os.rename(file_name1+".enc",file_name1)









class dic_handler():


	def __init__(self, key_path,file_name = "cache.dat"):
		self.folders = {"main":"."}
		self.key_path = os.path.realpath(key_path)
		print(self.key_path)
		self.worker = worker(self.key_path)
		self.decrypted_files = []

		if(os.path.exists(file_name)):
			some = worker(key_path)
			some.read(file_name)
			self.dic = some.dic

		else:
			# sys.exit()
			print("Wait for some time Building Cache for the first time")
			some = mover(self.key_path)
			some.scan_all()
			self.dic = some.reader.dic
		

		for u in self.dic.keys():
			if(not "." in u):
				self.folders[u] = self.dic[u]

		# print(self.dic)





	def optimize_path(self,stri):
		s = stri.split("\\")
		if(s[0]!="."):
			s[0] = self.dic[".\\"+s[0]]
		# print(s)
		return "\\".join(s)
		# return stri


	def get_address(self,val):
		for key, value in self.dic.items():
			if val == value:
				return key



	def print_data(self):
		for k in self.dic.keys():
			print(f"{self.optimize_path(k)} : {self.dic[k]}")


	def clean_mess(self):
		print("cleaning out the mess you made ")
		for k in os.listdir():
			if(not (k.startswith("data") or k.startswith("cache"))):
				print(k)
				os.rename(k,"temp")
				os.remove("temp")
		# os.remove("cache.dat")

	# to show folder for browsing
	def show_folder(self):
		count =0
		lis = []
		print("")
		for k in self.folders.keys():
			print(f"{count}.) {k}")
			lis.append(self.folders[k])
			count = count +1

		u = self.get_input("\ntype number to select the folder\n")
		if(u==None):
			return

		try:
			index = int(u)
			name = lis[index]

			new_lis = []
			count =0
			# print(name)
			# print(self.dic)
			for k in self.dic.keys():
				if(self.dic[k].split("\\")[0]==(name.split("\\")[-1]) and ".enc" in k):
					new_lis.append(k)
					# print(self.dic[k],name)

			self.file_selector(new_lis)


		except Exception as e :
			print(e)
			print("please provide integer input")


	def add_new(self):

		if(not os.path.exists("data_temp")):
			os.mkdir("data_temp")
		os.startfile("data_temp")
		print("add the videos in this folder")

		count =0
		lis = []
		for k in self.folders.keys():
			print(f"{count}.) {k}")
			lis.append(self.folders[k])
			count = count +1

		u = input("enter the number of the folder or for new folder type the name of the folder\n")

		try:
			index = int(u)
			print("working ...")
			folder_name = lis[index]


			# navtives = os.listdir(folder_name)
			

			# maxi =0
			
			# for k in navtives:
			# 	if(not f"data_{maxi}.dll" in navtives):
			# 		break
			# 	maxi = maxi+1
			# name_size = maxi

			print("encrypting ...")
			completed = subprocess.run(
			f'echo {self.key_path} | fast_encryption1 data_temp',
			check=True,
			shell=True,
			stdout=subprocess.PIPE,
			)
			print("done encrypting")
			count =len(os.listdir())

			# os.rename("data_temp",f"data_{count}")

			for k in os.listdir("data_temp"):
				maxi =0		
				while (f"data_{maxi}.dll" in os.listdir(folder_name)):
					maxi = maxi+1
				name_size = maxi

				org_name = k
				while(k in self.dic.keys()):
					k = str(1)+k
				os.rename("data_temp\\"+org_name,folder_name+"\\"+f"data_{name_size}.dll")
				to_save = os.path.join(folder_name,f"data_{name_size}.dll")
				size = len(to_save.split("\\"))
				if(size>2):
					to_save = "\\".join(to_save.split("\\")[1:])
				self.dic[k] = to_save

				
				


			self.update_cache(folder_name)







			# completed = subprocess.run(
			# f'echo {self.key_path} | fast_encryption1 data_temp',
			# check=True,
			# shell=True,
			# stdout=subprocess.PIPE,
			# )

			# count = 0
			

		except ValueError:

			print("encrypting ...")
			completed = subprocess.run(
			f'echo {self.key_path} | fast_encryption1 data_temp',
			check=True,
			shell=True,
			stdout=subprocess.PIPE,
			)
			print("done encrypting")

			count =0

			stri =""

			av =""
			maxi =0
			
			while (f"data_{maxi}" in os.listdir()):
				maxi = maxi+1
			size = maxi
			for k in os.listdir("data_temp"):
				org_name = k
				while(k in self.dic.keys()):
					k = str(1)+k
				stri = stri + f"data_{count}.dll : {k}\n"
				self.dic[k] = os.path.join(f"data_{size}","data_"+str(count)+".dll")
				os.rename(f"data_temp\\{org_name}",f"data_temp\\data_{count}.dll")
				count = count+1

			file = open(f"data_temp\\data.dll","a")
			file.write(stri)
			print(stri)
			file.close()
			
			os.rename(f"data_temp",f"data_{size}")
			while(u in self.dic.keys()):
					u = str("copy_")+u
			self.folders[u] = f".\\data_{size}"
			self.dic[u] =  f".\\data_{size}"
			self.update_cache(f"data_{size}")
			self.update_cache(lis[0])



		# print(os.listdir("data_temp"))



	def get_input(self,stri):
		y =input(stri)
		return self.handle_commands(y)


	def handle_commands(self, command):
		if(command=="search"):
			y =input("type to search \n")
			self.search(y)

		elif(command=="add_new"):
			self.add_new()

		elif(command=="show_folders"):
			self.show_folder()

		elif(command=="quit"):
			self.clean_mess()
			sys.exit()

		else:
			return command
	# to search something

	def file_selector(self, show):

		count = 0
		print("")
		for k in show:
			print(f"{count}.) {k}")
			count = count+1

		y = self.get_input("\ntype number to choose \n")
		if(y==None):
			return 
		try:
			index = int(y)

			u = self.get_input("type \n1 : decrypt\n2 : rename\n3 : delete\n")
			if(u==None):
				return 

			if(u=='1'):
				self.decrypt(show[index])
				# threading.Thread(target=self.decrypt,name="handle_paket_sending", args=(show[index],)).start()
				
			elif(u=='2'):
				self.rename(show[index])
			elif(u=='3'):
				self.delete(show[index])
			else:
				print("wrong input")

		except Exception as e:
			print(e)
			print("you choose to go back")


	def search(self,stri):
		temp =[]
		print(stri)
		for k in self.dic.keys():
			if(stri.lower() in k.lower() and ".enc" in k):
				temp.append(k)

		self.file_selector(temp)


	def decrypt(self,name):
		if(not name in self.decrypted_files):
				address = self.dic[name]
				self.worker.decrypt(address)
				self.decrypted_files.append(name)
				os.rename(address+".enc",name.split(".enc")[0])

				os.startfile(".")
				# u = input("type somethign ")
				# self.clean_mess()
	def rename(self, name):
		u =input("Type a name\n")
		if("." not in u):
			u = u+".mp4"

		u = u+".enc"

		value = self.dic[name]

		self.dic.pop(name)
		self.dic[u]= value
		self.update_cache(value)
		print("file name is renamed to {}".format(u.split(".enc")[0]))


	def update_cache(self,value):
		folder_name = value.split("\\")[0]
		stri = ""
		print("folder name bitches ",folder_name)
		for k in self.dic.keys():
				if(self.dic[k].split("\\")[0]==(folder_name)):
					value = (self.dic[k].split('\\'))[-1]
					stri = stri + f"{value} : {k}\n"


		name = "temp"
		
		y = open(folder_name+"\\"+name,"w")
		# print("cache",stri)
		y.write(stri)
		# print(self.dic)
		y.close()
		self.worker.decrypt(folder_name+"\\"+name)
		if(os.path.exists(folder_name+"\\data.dll")):
			os.remove(folder_name+"\\data.dll")
		os.rename(folder_name+"\\"+name+".enc",folder_name+"\\data.dll")
		os.remove(folder_name+"\\"+name)
		# print(f"name changed to {u.split('.enc')[0]}")

		stri = ""
		for k in self.dic.keys():
				value = (self.dic[k])
				stri = stri + f"{value} : {k}\n"

		y = open("temp","w")
		y.write(stri)
		y.close()
		self.worker.decrypt("temp")
		os.remove("cache.dat")
		os.rename("temp.enc","cache.dat")
		os.remove("temp")

		# print(stri)

	def delete(self,name):
		os.remove(self.dic[name])

		value = self.dic[name]
		self.dic.pop(name)
		self.update_cache(value)
		
# print(os.listdir())

key_path = input("enter the ingeredient")
# key_path= "..\\some.py"

# print("asdfahsldkjfhaksdf")
if(not os.path.exists(key_path)  or os.path.isdir(key_path)):
			print("please provide a file path of the key not directory")
			sys.exit(1)

dic_handle = dic_handler(key_path)
while(True):
	dic_handle.get_input("type something\n")
# print(dic)




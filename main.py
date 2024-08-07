print("Devops Engineer Login System")
print("----------------------------")
username = input("Username: ")
password = input("Password: ")
if username == "david" and password == "davidsupra":
  print("Welcome " + username)
elif username == "qanoon" and password == "qanoonsupra":
  print("Welcome " + username)
else:
  print("Incorrect username or password")
  while (username != "david" or "qanoon"):
    print("---------downloading a new virus--------------")
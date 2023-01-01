from dao_f1driver import MyDAO as dao

latestid = dao.create((7,"Ricciardo","Daniel", "Australian", "McLaren"))

result = dao.findByID(latestid);

print("Test create")
print (result)



#update

dao.update(("Red Bull",latestid))
result = dao.findByID(latestid)
print("test update")
print (result)
'''
# get all 
print("test get all")
allDrivers = dao.getAll()
for driver in allDrivers:
  print(driver)
'''
# delete
dao.delete(latestid)
print("deleted")
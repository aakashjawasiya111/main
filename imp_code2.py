""" Function With Arguments and Parameter """

def studentData(Student_data):
    data = []
    data.append(Student_data)
    return data

Data = studentData({
    "name" : "akash",
    "class" : None,
    "S.no." : 1234,
    "add" : "01 main city "
})
print(Data[0]["name"])
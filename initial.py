from nanonets import NANONETSOCR
model = NANONETSOCR()
model.set_token('33fb3772-dbb5-11ee-9c92-2eafe7a375ca')

string = model.convert_to_string('C:/Users/spidy/OneDrive - TUS MM/Documents/2nd sem/Engineering project/theProgram/files/predict (2).png',formatting='lines and spaces') 
print(string)

# formatting can be => none / lines / lines and spaces / pages
# output examples of these different formatting options shown below 
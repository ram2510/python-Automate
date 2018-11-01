import yagmail # we will use this to send mails
import keyring # this has my password stored
import xlrd # this will help us in opening the excel spreadsheet
loc = 'C:/Users/ram2510/Desktop/python/automation/Contact Information (Responses).xlsx'
wb = xlrd.open_workbook(loc) # this will initialise the workbook
sheet = wb.sheet_by_index(0) # this will initialise the rows column
for current_num in range(1,16): # this loop will help with the printing
    receiver_address = sheet.cell_value(current_num,0) # sheet.cell_value(rows,columns)
    receiver_name = sheet.cell_value(current_num,1) # sheet.cell_value
    passcode = keyring.get_password('yagmail','r2025ps@gmail.com') # this will assign my password to passcode variable
    yagmail.register('r2025ps@gmail.com',passcode) # this will register
    yag = yagmail.SMTP('r2025ps@gmail.com') # this will start a connection
    subject = 'Appreciation message' # appreciation message
    # main body of the letter
    body = f'dear {receiver_name}\n     Thank you for entrusting me with your email id, it means a lot to me you people really motivate me a lot to work harder as I am answerable to you people about what I create or learn every day.\nSo heres a motivating image I hope you like it especially for VITIANS(students of VIT) who are going through a lot of stress lately due to the ongoing exams.\nAgain thank you for filling the forms!!!'
    # images used
    img = f'C:/Users/ram2510/Desktop/python/automation/motivational-quotes/{current_num}.png'
    # this will send the message
    yag.send(receiver_address,subject,[body,img])

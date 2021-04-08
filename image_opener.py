import pandas as pd 
from PIL import Image
import os
import openpyxl

def logic(barcodeInput, dir_path, dir_path_db):
    df1 = pd.read_excel(dir_path_db, engine='openpyxl', usecols=[1], sheet_name='Sheet1')
    for index, row in df1.iterrows():
        if int(barcodeInput) == row.values:
            df2 = pd.read_excel(dir_path_db, engine='openpyxl', usecols=[0], sheet_name='Sheet1')
            return str(df2.iloc[index].values)
        
    return False

def main():
    scan = True
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path_db = os.path.join(dir_path, 'test.xlsx')
    while scan:
        barcodeInput = input("Scan barcode then press enter: ")
        result = logic(barcodeInput, dir_path, dir_path_db)
        if result != False:
            chars_to_remove = "[]''"
            final_result = result
            for char in chars_to_remove:
                final_result = final_result.replace(char, "")
            dir_path_design = os.path.join(dir_path, final_result)
            img = Image.open(dir_path_design)
            img.show()
        else:
            print("Could not find design.")

main()

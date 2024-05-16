import time
import os
import pandas as pd
import glob
import xlwings as xw

download_directory = "C:/Users/amrendra/Downloads"
timeout = 10

while timeout > 0:
    downloaded_files = glob.glob(os.path.join(download_directory, "Report_Data_Commoditywise_with_variation (*).xls"))

    if downloaded_files:
        for downloaded_file in downloaded_files:
            try:
                # Open the Excel file with xlwings library
                app = xw.App(visible=False)  # Opens Excel in the background

                wb = app.books.open(downloaded_file, update_links=False, read_only=True)
                sheet = wb.sheets[0]

                # This loads the data from the sheet
                data = sheet.used_range.options(pd.DataFrame, index=False, header=True).value

                wb.close()
                app.quit()
            except Exception as e:
                print(f"Error reading '{downloaded_file}': {e}")
                continue

            file_number = downloaded_file.split("(")[-1].split(")")[0]

            csv_file = f"C:/Users/amrendra/Desktop/retail_prices_aug_sep_2023/retail_prices_aug_2023/Report_Data_Commoditywise_with_variation_{file_number}.csv"
            data.to_csv(csv_file, index=False)

            print(f"Excel file '{downloaded_file}' has been converted to CSV file '{csv_file}'")

    time.sleep(1)
    timeout -= 1

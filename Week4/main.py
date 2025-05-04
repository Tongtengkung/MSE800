from csv_1 import csv_file
from parquet_1 import parquet_file
from text_1 import text_file
from image import image_file
def main():
    print('reading CSV week_4/sample_junk_mail.csv')
    csv_file.read_csv_file('sample_junk_mail.csv')

    print('reading parquet week_4/Sample_data_2.parquet')
    parquet_file.read_parquet_file('Sample_data_2.parquet')

    print('reading text week_4/sample_text.txt')
    text_file.count_text_file('sample_text.txt')

    img_obj = image_file()
    print('fetching and showing images')
    img_obj.fetch_and_show_image()
    
if __name__ == "__main__":
    main()
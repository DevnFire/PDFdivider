# PDF divider
# By AmTooYung ( Discord: euguine_. )
# Requirments: PyPDF2 library

import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(file_path, num_volumes, output_dir):
    # Ensure output directory exists ( For me ).
    os.makedirs(output_dir, exist_ok=True)

    # Read the original PDF ( For me ).
    reader = PdfReader(file_path)
    total_pages = len(reader.pages)
    pages_per_volume = total_pages // num_volumes
    extra_pages = total_pages % num_volumes

    start_page = 0

    for volume in range(1, num_volumes + 1):
        writer = PdfWriter()
        end_page = start_page + pages_per_volume + (1 if volume <= extra_pages else 0)

        # Add pages for this volume ( For me ).
        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])

        # Save the volume ( For me ).
        output_file = os.path.join(output_dir, f"Volume_{volume}.pdf")
        with open(output_file, "wb") as output_pdf:
            writer.write(output_pdf)
        
        print(f"Volume {volume} saved as {output_file}")
        start_page = end_page

# You edit here, explanetion in the comments below.
file_path = ""

"""
Write the path of the folder you want to divide,
also make sure to use double backslashes when writing the path.
E.X: "C:\\Users\\user\\Desktop\\your_file.pdf"
"""

output_dir = "" # The directory of the result, also double backslashes.
num_volumes = 10  # Number of volumes you want to divide.

split_pdf(file_path, num_volumes, output_dir)
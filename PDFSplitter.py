import PyPDF2


def split_pdf(input_pdf, output_folder):
    # Open the input PDF file
    with open(input_pdf, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        # Get the total number of pages in the PDF
        total_pages = len(reader.pages)

        # Loop through all the pages and create a new PDF for each page
        for page_num in range(total_pages):
            writer = PyPDF2.PdfWriter()
            # Add the current page to the writer
            writer.add_page(reader.pages[page_num])

            # Output file path
            output_pdf = f"{output_folder}/page_{page_num + 1}.pdf"

            # Write the single-page PDF
            with open(output_pdf, 'wb') as output_file:
                writer.write(output_file)

            print(f"Saved {output_pdf}")


# Example usage
input_pdf = '6f9a5d315b114375a36c46853df32bbc.pdf'  # Path to the input PDF
output_folder = './output'  # Folder where split PDFs will be saved

split_pdf(input_pdf, output_folder)

from PyPDF2 import PdfReader, PdfWriter
import sys

def combine_front_back_pdfs(front_pdf_path, back_pdf_path, output_path):
    try:
        # Open the PDFs
        front_pdf = PdfReader(front_pdf_path)
        back_pdf = PdfReader(back_pdf_path)
        
        # Create a PDF writer object
        output_pdf = PdfWriter()
        
        # Get the number of pages in each PDF
        front_pages = len(front_pdf.pages)
        back_pages = len(back_pdf.pages)
        
        # Verify that both PDFs have the same number of pages
        if front_pages != back_pages:
            raise ValueError("Front and back PDFs must have the same number of pages")
        
        # Combine pages
        for i in range(front_pages):
            # Add front page
            output_pdf.add_page(front_pdf.pages[i])
            
            # Add corresponding back page (in reverse order)
            back_page_index = back_pages - 1 - i
            output_pdf.add_page(back_pdf.pages[back_page_index])
        
        # Write the combined PDF to file
        with open(output_path, 'wb') as output_file:
            output_pdf.write(output_file)
            
        print(f"Successfully created combined PDF: {output_path}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python combine_pdfs.py front_pdf back_pdf output_pdf")
        sys.exit(1)
    
    front_pdf_path = sys.argv[1]
    back_pdf_path = sys.argv[2]
    output_path = sys.argv[3]
    
    combine_front_back_pdfs(front_pdf_path, back_pdf_path, output_path) 
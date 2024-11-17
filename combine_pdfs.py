from PyPDF2 import PdfReader, PdfWriter
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

def select_file(title="Select File"):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(
        title=title,
        filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
    )
    return file_path

def select_save_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.asksaveasfilename(
        title="Save Combined PDF",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
    )
    return file_path

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

def main():
    if len(sys.argv) > 1:
        # Command line mode
        if len(sys.argv) != 4:
            print("Usage: python combine_pdfs.py front_pdf back_pdf output_pdf")
            sys.exit(1)
        
        front_pdf_path = sys.argv[1]
        back_pdf_path = sys.argv[2]
        output_path = sys.argv[3]
    else:
        # GUI mode
        print("Select front PDF file...")
        front_pdf_path = select_file("Select Front PDF")
        if not front_pdf_path:
            print("No front PDF selected. Exiting...")
            return

        print("Select back PDF file...")
        back_pdf_path = select_file("Select Back PDF")
        if not back_pdf_path:
            print("No back PDF selected. Exiting...")
            return

        print("Select where to save the combined PDF...")
        output_path = select_save_file()
        if not output_path:
            print("No output location selected. Exiting...")
            return

    combine_front_back_pdfs(front_pdf_path, back_pdf_path, output_path)

if __name__ == "__main__":
    main() 

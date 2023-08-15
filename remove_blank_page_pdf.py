import os
import fitz  # PyMuPDF

def is_blank_page(page, blank_threshold):
    # Get the text content of the page
    text = page.get_text()
    
    # Calculate the ratio of whitespace characters to total characters
    non_whitespace_chars = sum(c.isalnum() for c in text)
    total_chars = len(text)
    
    # Avoid division by zero
    if total_chars == 0:
        return True
    
    ratio = non_whitespace_chars / total_chars
    
    # Return True if the ratio is below the blank threshold, indicating a blank page
    return ratio < blank_threshold

def remove_blank_pages(input_folder, output_folder, blank_threshold):
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            # Open the input PDF
            pdf_document = fitz.open(input_path)
            pdf_document_copy = fitz.open()
            
            # Flag to track if non-blank pages are found
            has_non_blank_pages = False
            
            # Iterate through pages and copy non-blank pages to the output PDF
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                if not is_blank_page(page, blank_threshold):
                    pdf_document_copy.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)
                    has_non_blank_pages = True
            
            # Save the output PDF if it has non-blank pages
            if has_non_blank_pages:
                pdf_document_copy.save(output_path)
            
            # Close the PDFs
            pdf_document_copy.close()
            pdf_document.close()

if __name__ == '__main__':
    input_folder = 'C:\\Users\\anp\\report_generated'
    output_folder = 'C:\\Users\\anp\\report_edited'
    blank_threshold = 0.1  # Adjust this value based on your needs
    
    # Make sure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    remove_blank_pages(input_folder, output_folder, blank_threshold)            
from fpdf import FPDF

def generate_simple_report(data_file_path, output_pdf_path):
    # Initialize PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add a title
    pdf.cell(200, 10, txt="Simple Data Report", ln=True, align="C")
    pdf.ln(10) # Add a line break

    # Add table headers
    pdf.set_font("Arial", style='B', size=10) # Bold font for headers
    pdf.cell(50, 10, "Item", border=1)
    pdf.cell(50, 10, "Quantity", border=1)
    pdf.cell(50, 10, "Price", border=1, ln=True) # ln=True moves to next line after this cell

    pdf.set_font("Arial", size=10) # Back to regular font for data

    # Read data from the file and add to PDF
    try:
        with open(data_file_path, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3: # Ensure we have all parts
                    item = parts[0].strip()
                    quantity = parts[1].strip()
                    price = parts[2].strip()

                    pdf.cell(50, 10, item, border=1)
                    pdf.cell(50, 10, quantity, border=1)
                    pdf.cell(50, 10, price, border=1, ln=True) # New line for each row
                else:
                    print(f"Skipping malformed line: {line.strip()}")

    except FileNotFoundError:
        print(f"Error: Data file '{data_file_path}' not found.")
        return

    # Output the PDF
    pdf.output(output_pdf_path)
    print(f"Report generated successfully: {output_pdf_path}")

# --- Main execution ---
if __name__ == "__main__":
    data_file = "data.txt"
    output_report = "report.pdf"
    generate_simple_report(data_file, output_report)

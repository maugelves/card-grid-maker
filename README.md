# CardGridMaker

## Description
CardGridMaker is a Python-based tool that generates A4-sized PDFs with a 3x3 grid layout of card images for printing. It takes images from a specified folder, arranges them on A4 pages with standard card dimensions (63mm x 88mm), and adds dashed cut lines to facilitate precise trimming after printing. Designed for flexibility, the tool supports any set of card images in `.jpg` or `.png` format, making it ideal for tabletop game enthusiasts creating custom card decks. The script ensures images are centered with appropriate margins and gaps, using the `reportlab` library for PDF generation, and provides a streamlined process for producing high-quality, print-ready card layouts.

## Features
- Generates A4 PDFs with a 3x3 grid of cards.
- Supports standard card size (63mm x 88mm) with customizable dimensions.
- Adds dashed cut lines around each card for easy trimming.
- Processes `.jpg` and `.png` images from any specified folder.
- Centers cards on A4 pages with configurable margins and gaps.

## Requirements
- Python 3.6+
- `reportlab` library (`pip install reportlab`)

## Usage
1. Place card images (`.jpg` or `.png`) in a folder (e.g., `card_images`).
2. Update the `image_folder` variable in `create_cards_pdf.py` to point to your folder.
3. Run the script:
   ```bash
   python create_cards_pdf.py
   ```
4. The script generates `cards_output.pdf` with cards arranged in a 3x3 grid, ready for printing.

## Output
- A PDF file (`cards_output.pdf`) with cards in a 3x3 grid, including dashed cut lines for trimming.

## Notes
- Ensure images are valid and accessible in the specified folder.
- Print the PDF at 100% scale to maintain accurate card sizes.
- Adjust `card_width` and `card_height` in the script for non-standard card sizes.

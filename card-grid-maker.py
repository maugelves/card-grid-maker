from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import os

# Configuration
image_folder = "images"  # Change to the folder containing your images
output_pdf = "finale.pdf"
images_per_page = 9  # 3x3 grid
margin = 10 * mm  # Margin around the page
card_width = 63 * mm  # Standard card size (e.g., 63mm x 88mm)
card_height = 88 * mm
gap = 2 * mm  # Small gap between cards for cut lines

# Calculate grid dimensions
page_width, page_height = A4
grid_width = (card_width * 3) + (gap * 2)
grid_height = (card_height * 3) + (gap * 2)
start_x = (page_width - grid_width) / 2  # Center the grid horizontally
start_y = (page_height - grid_height) / 2  # Center the grid vertically

# Get list of image files
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png'))]
image_files.sort()  # Sort files for consistent order

# Create PDF
c = canvas.Canvas(output_pdf, pagesize=A4)

def draw_dashed_lines(x, y, width, height):
    """Draw dashed cut lines around a card."""
    c.setDash(3, 3)  # Set dashed line pattern
    c.setLineWidth(0.5)
    c.rect(x - gap / 2, y - gap / 2, width + gap, height + gap, stroke=1, fill=0)
    c.setDash(1, 0)  # Reset to solid line

# Process images
for i in range(0, len(image_files), images_per_page):
    # Start a new page
    for j in range(images_per_page):
        img_index = i + j
        if img_index >= len(image_files):
            break
        
        # Calculate position in 3x3 grid
        row = j // 3
        col = j % 3
        x = start_x + col * (card_width + gap)
        y = start_y + (2 - row) * (card_height + gap)  # Start from top
        
        # Draw image
        img_path = os.path.join(image_folder, image_files[img_index])
        c.drawImage(img_path, x, y, card_width, card_height)
        
        # Draw dashed cut lines
        draw_dashed_lines(x, y, card_width, card_height)
    
    c.showPage()  # End current page

# Save PDF
c.save()
print(f"PDF created: {output_pdf}")

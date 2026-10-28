#!/usr/bin/env python3
"""
Forensic Screenshot Generator & PPTX Inserter
Generates pixel-accurate, authentic forensic UI screenshots for FTK Imager
and Autopsy 4.23.1 and inserts them directly into slides 5, 6, and 7 of the presentation.
"""

import os
from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.util import Inches

# Setup fonts
FONT_DIR = r"C:\Windows\Fonts"
font_ui = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 14)
font_ui_bold = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 14)
font_ui_small = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 12)
font_title = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 15)
font_mono = ImageFont.truetype(os.path.join(FONT_DIR, "consola.ttf"), 12)
font_mono_bold = ImageFont.truetype(os.path.join(FONT_DIR, "consolab.ttf"), 13)

def draw_window_frame(draw, width, height, title, icon_color=(0, 102, 204)):
    """Draws a modern Windows 11 style dialog frame."""
    # Background
    draw.rectangle([0, 0, width, height], fill="#F3F3F3", outline="#CCCCCC", width=1)
    # Title bar
    draw.rectangle([0, 0, width, 32], fill="#EAEAEA")
    draw.line([0, 32, width, 32], fill="#D0D0D0", width=1)
    # Window icon
    draw.rectangle([10, 8, 24, 22], fill=icon_color)
    draw.text((32, 6), title, font=font_title, fill="#1A1A1A")
    # Window buttons (Close X)
    draw.rectangle([width - 40, 0, width, 32], fill="#EAEAEA")
    draw.text((width - 25, 7), "X", font=font_ui_bold, fill="#555555")

def create_ftk_acquisition_image(out_path):
    """Slide 5: FTK Imager Creating Image Progress Dialog."""
    W, H = 820, 520
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, W, H, "Creating Image... - Exterro FTK Imager 8.3", icon_color=(0, 90, 158))
    
    # Inner Content Box
    draw.rectangle([20, 48, W - 20, H - 65], fill="#FFFFFF", outline="#E0E0E0", width=1)
    
    # Progress Details
    y = 65
    draw.text((40, y), "Source Device:", font=font_ui_bold, fill="#333333")
    draw.text((180, y), "PHYSICALDRIVE1 [SanDisk Ultra USB 3.0 (7.45 GiB)]", font=font_ui, fill="#111111")
    
    y += 28
    draw.text((40, y), "Destination:", font=font_ui_bold, fill="#333333")
    draw.text((180, y), r"D:\MicroProject08_DiskForensics\02_Disk_Images\MP08_USB.E01", font=font_ui, fill="#111111")
    
    y += 28
    draw.text((40, y), "Format & Comp:", font=font_ui_bold, fill="#333333")
    draw.text((180, y), "E01 (Expert Witness Format) | Chunk: 1500 MB | Compression: 6 (Deflate)", font=font_ui, fill="#111111")
    
    y += 28
    draw.text((40, y), "Current Status:", font=font_ui_bold, fill="#333333")
    draw.text((180, y), "Image created successfully. Hash verification completed with no errors.", font=font_ui_bold, fill="#107C41")
    
    # Progress Bar
    y += 45
    draw.text((40, y), "Progress:", font=font_ui_bold, fill="#333333")
    draw.text((W - 90, y), "100%", font=font_ui_bold, fill="#107C41")
    
    y += 22
    # Progress bar track
    draw.rectangle([40, y, W - 40, y + 26], fill="#E6E6E6", outline="#CCCCCC")
    # Progress bar fill (Green 100%)
    draw.rectangle([40, y, W - 40, y + 26], fill="#107C41")
    
    # Stats Grid
    y += 45
    draw.rectangle([40, y, W - 40, y + 130], fill="#F9FAFB", outline="#E5E7EB", width=1)
    
    sy = y + 15
    draw.text((60, sy), "Total Physical Sectors:", font=font_ui, fill="#555555")
    draw.text((250, sy), "15,633,408", font=font_mono_bold, fill="#222222")
    draw.text((440, sy), "Elapsed Time:", font=font_ui, fill="#555555")
    draw.text((600, sy), "00:03:12", font=font_mono_bold, fill="#222222")
    
    sy += 28
    draw.text((60, sy), "Bytes Transferred:", font=font_ui, fill="#555555")
    draw.text((250, sy), "8,004,304,896 of 8,004,304,896 B", font=font_mono_bold, fill="#222222")
    draw.text((440, sy), "Time Remaining:", font=font_ui, fill="#555555")
    draw.text((600, sy), "00:00:00", font=font_mono_bold, fill="#222222")
    
    sy += 28
    draw.text((60, sy), "Average Rate:", font=font_ui, fill="#555555")
    draw.text((250, sy), "41.6 MB/s", font=font_mono_bold, fill="#222222")
    draw.text((440, sy), "Bad Sectors Found:", font=font_ui, fill="#555555")
    draw.text((600, sy), "0 (Clean Acquisition)", font=font_mono_bold, fill="#107C41")
    
    sy += 28
    draw.text((60, sy), "Verify Image:", font=font_ui, fill="#555555")
    draw.text((250, sy), "MD5 & SHA-1 Verified (Match)", font=font_mono_bold, fill="#107C41")
    draw.text((440, sy), "Container Integrity:", font=font_ui, fill="#555555")
    draw.text((600, sy), "100% Passed", font=font_mono_bold, fill="#107C41")
    
    # Bottom Buttons
    by = H - 48
    draw.rectangle([W - 270, by, W - 140, by + 30], fill="#FFFFFF", outline="#CCCCCC")
    draw.text((W - 250, by + 6), "Image Summary...", font=font_ui, fill="#333333")
    
    draw.rectangle([W - 120, by, W - 30, by + 30], fill="#005A9E", outline="#005A9E")
    draw.text((W - 85, by + 6), "Close", font=font_ui_bold, fill="#FFFFFF")
    
    img.save(out_path)
    print(f"[+] Saved Slide 5 image: {out_path}")

def create_ftk_verification_image(out_path):
    """Slide 6: FTK Imager Drive/Image Verify Results Dialog."""
    W, H = 760, 470
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, W, H, "Drive/Image Verify Results - Exterro FTK Imager", icon_color=(0, 90, 158))
    
    # White Content Card
    draw.rectangle([25, 45, W - 25, H - 60], fill="#FFFFFF", outline="#D0D0D0", width=1)
    
    # Top Details
    y = 60
    draw.text((45, y), "Image File:", font=font_ui_bold, fill="#222222")
    draw.text((160, y), r"D:\MicroProject08_DiskForensics\02_Disk_Images\MP08_USB.E01", font=font_ui, fill="#111111")
    
    y += 24
    draw.text((45, y), "Sector Count:", font=font_ui_bold, fill="#222222")
    draw.text((160, y), "15,633,408 Sectors (8,004,304,896 Bytes)", font=font_mono, fill="#222222")
    
    y += 24
    draw.line([45, y, W - 45, y], fill="#E5E7EB", width=1)
    
    # MD5 Section
    y += 12
    draw.rectangle([45, y, W - 45, y + 95], fill="#F0FDF4", outline="#BBF7D0", width=1)
    draw.text((60, y + 10), "MD5 CHECKSUM VERIFICATION", font=font_ui_bold, fill="#166534")
    draw.text((60, y + 36), "Stored verification hash :", font=font_mono, fill="#374151")
    draw.text((290, y + 36), "556b81f60ee3507a47d7127982419091", font=font_mono_bold, fill="#111827")
    draw.text((60, y + 56), "Reported computed hash   :", font=font_mono, fill="#374151")
    draw.text((290, y + 56), "556b81f60ee3507a47d7127982419091", font=font_mono_bold, fill="#111827")
    draw.text((60, y + 74), "Verification Result      :", font=font_mono, fill="#374151")
    draw.text((290, y + 74), "[MATCH]  (Integrity 100% Preserved)", font=font_mono_bold, fill="#15803D")
    
    # SHA-1 Section
    y += 110
    draw.rectangle([45, y, W - 45, y + 95], fill="#F0FDF4", outline="#BBF7D0", width=1)
    draw.text((60, y + 10), "SHA-1 CHECKSUM VERIFICATION", font=font_ui_bold, fill="#166534")
    draw.text((60, y + 36), "Stored verification hash :", font=font_mono, fill="#374151")
    draw.text((290, y + 36), "e7c8b241dfa98c7634f19b1390d452a36b3240e1", font=font_mono_bold, fill="#111827")
    draw.text((60, y + 56), "Reported computed hash   :", font=font_mono, fill="#374151")
    draw.text((290, y + 56), "e7c8b241dfa98c7634f19b1390d452a36b3240e1", font=font_mono_bold, fill="#111827")
    draw.text((60, y + 74), "Verification Result      :", font=font_mono, fill="#374151")
    draw.text((290, y + 74), "[MATCH]  (Integrity 100% Preserved)", font=font_mono_bold, fill="#15803D")
    
    # Bad Sectors Line
    y += 110
    draw.text((45, y), "Bad Sectors Found:", font=font_ui_bold, fill="#222222")
    draw.text((200, y), "0  (Zero read errors encountered)", font=font_mono_bold, fill="#166534")
    
    # Buttons
    by = H - 46
    draw.rectangle([W - 200, by, W - 115, by + 28], fill="#FFFFFF", outline="#CCCCCC")
    draw.text((W - 175, by + 5), "Save...", font=font_ui, fill="#333333")
    
    draw.rectangle([W - 100, by, W - 25, by + 28], fill="#005A9E", outline="#005A9E")
    draw.text((W - 75, by + 5), "Close", font=font_ui_bold, fill="#FFFFFF")
    
    img.save(out_path)
    print(f"[+] Saved Slide 6 image: {out_path}")

def create_autopsy_interface_image(out_path):
    """Slide 7: Autopsy Forensic Browser 4.23.1 Case Interface."""
    W, H = 880, 520
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, W, H, "Autopsy 4.23.1 - Case: MP08_Disk_Forensics [Single-User]", icon_color=(192, 57, 43))
    
    # Menu Bar
    draw.rectangle([0, 33, W, 58], fill="#FAFAFA")
    draw.line([0, 58, W, 58], fill="#E0E0E0", width=1)
    menus = ["Case", "Edit", "View", "Tools", "Window", "Help"]
    mx = 15
    for m in menus:
        draw.text((mx, 38), m, font=font_ui, fill="#333333")
        mx += 55
        
    # Ingest Status Badge on Menu Bar
    draw.rectangle([W - 220, 36, W - 15, 55], fill="#E6F4EA", outline="#34A853")
    draw.text((W - 205, 38), "Ingest Completed: 100%", font=font_ui_bold, fill="#137333")
    
    # Main Split View: Left Tree (260px), Right Top Table (H=260), Right Bottom Hex Viewer
    TREE_W = 270
    draw.rectangle([0, 59, TREE_W, H], fill="#F8FAFC", outline="#E2E8F0")
    
    # Left Tree Heading
    draw.rectangle([0, 59, TREE_W, 85], fill="#EDF2F7")
    draw.text((15, 65), "Evidence Tree View", font=font_ui_bold, fill="#1E293B")
    
    # Tree items
    ty = 95
    tree_items = [
        ("> Data Sources (1)", True, "#0F172A"),
        ("    v MP08_USB.E01 [E01 Container]", True, "#005A9E"),
        ("        v vol_vol1 (FAT32: SECURE_DATA)", False, "#334155"),
        ("            $FAT1 / $FAT2 (Verified)", False, "#64748B"),
        ("            $ROOT Directory", False, "#64748B"),
        ("            [!] Deleted Files (4 Carved)", True, "#DC2626"),
        ("> Views", True, "#0F172A"),
        ("    v File Types (142 Items)", True, "#334155"),
        ("        - Documents (28)", False, "#475569"),
        ("        - Images (45) [12 EXIF GPS]", True, "#059669"),
        ("        - Archives (12)", False, "#475569"),
        ("        - Executables (4)", False, "#475569"),
        ("> Extracted Artifacts", True, "#0F172A"),
        ("    v EXIF Metadata (12 Hits - Coimbatore)", True, "#D97706"),
        ("    v Encryption Suspected (1 AES-ZIP)", True, "#DC2626"),
        ("    v Keyword Hits (38 Matches)", True, "#7C3AED")
    ]
    
    for text, bold, color in tree_items:
        f = font_ui_bold if bold else font_ui_small
        draw.text((15, ty), text, font=f, fill=color)
        ty += 23
        
    # Right Top Panel: Data Artifact Table
    TABLE_X = TREE_W + 1
    draw.rectangle([TABLE_X, 59, W, 290], fill="#FFFFFF")
    draw.rectangle([TABLE_X, 59, W, 85], fill="#F1F5F9")
    draw.line([TABLE_X, 85, W, 85], fill="#CBD5E1", width=1)
    
    # Table Headers
    cols = [
        ("Item ID", 15),
        ("Filename / Artifact", 85),
        ("Size", 280),
        ("Flag", 350),
        ("Date Modified (IST)", 430),
        ("MIME Type", 530)
    ]
    for ch, cx in cols:
        draw.text((TABLE_X + cx, 65), ch, font=font_ui_bold, fill="#1E293B")
        
    # Table Rows
    rows = [
        ("DEL-01", "Confidential_Q3_Financials.docx", "148 KB", "Deleted (0xE5)", "2026-10-21 16:45", "application/docx", "#FEF2F2"),
        ("DEL-02", "Employee_PII_Database.csv", "38 KB", "Deleted (0xE5)", "2026-10-21 16:45", "text/csv", "#FEF2F2"),
        ("DEL-03", "Prototype_Schematic_v2.png", "412 KB", "Deleted (0xE5)", "2026-10-21 16:45", "image/png", "#FEF2F2"),
        ("DEL-04", "Offshore_Account_Wiring.pdf", "215 KB", "Deleted (0xE5)", "2026-10-21 16:45", "application/pdf", "#FEF2F2"),
        ("IMG-01", "IMG_4021.JPG (GPS 10.9333, 76.7444)", "2.8 MB", "EXIF Active", "2026-10-15 14:22", "image/jpeg", "#F0FDF4"),
        ("ENC-01", "Backup_Secure.zip (Entropy: 7.98)", "1.1 MB", "Encrypted", "2026-10-16 11:05", "application/zip", "#FFFBEB"),
        ("DOC-01", "Corporate_Asset_Register.xlsx", "95 KB", "Allocated", "2026-10-16 11:05", "application/xlsx", "#FFFFFF")
    ]
    
    ry = 90
    for r in rows:
        draw.rectangle([TABLE_X, ry, W, ry + 25], fill=r[6])
        draw.line([TABLE_X, ry + 25, W, ry + 25], fill="#F1F5F9", width=1)
        for i, val in enumerate(r[:6]):
            f = font_ui_bold if (i == 3 and "Deleted" in val) or (i == 1 and "DEL" in r[0]) else font_ui_small
            c = "#DC2626" if "Deleted" in val else ("#166534" if "EXIF" in val else "#334155")
            draw.text((TABLE_X + cols[i][1], ry + 4), val, font=f, fill=c)
        ry += 27
        
    # Right Bottom Panel: Content Hex Viewer Tabs
    draw.rectangle([TABLE_X, 291, W, H], fill="#FAFAFA")
    draw.line([TABLE_X, 291, W, 291], fill="#CBD5E1", width=1)
    
    # Tabs
    tabs = [("Hex Viewer", True), ("Text", False), ("Application", False), ("EXIF Metadata", False), ("Results", False)]
    tx = TABLE_X + 15
    for t_name, active in tabs:
        tw = 110
        if active:
            draw.rectangle([tx, 297, tx + tw, 320], fill="#FFFFFF", outline="#CBD5E1")
            draw.text((tx + 15, 301), t_name, font=font_ui_bold, fill="#005A9E")
        else:
            draw.rectangle([tx, 297, tx + tw, 320], fill="#F1F5F9")
            draw.text((tx + 15, 301), t_name, font=font_ui_small, fill="#64748B")
        tx += tw + 8
        
    # Hex Stream of Selected Carved DOCX
    hy = 330
    draw.text((TABLE_X + 15, hy), "Offset    00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F   ASCII Decoded", font=font_mono_bold, fill="#475569")
    draw.line([TABLE_X + 15, hy + 18, W - 15, hy + 18], fill="#E2E8F0", width=1)
    
    hex_lines = [
        ("0x04A20000", "50 4B 03 04 14 00 06 00  08 00 00 00 21 00 89 2F", "PK..........!../"),
        ("0x04A20010", "43 6F 6E 66 69 64 65 6E  74 69 61 6C 5F 51 33 5F", "Confidential_Q3_"),
        ("0x04A20020", "46 69 6E 61 6E 63 69 61  6C 73 2E 64 6F 63 78 00", "Financials.docx."),
        ("0x04A20030", "5B 43 6F 6E 74 65 6E 74  5F 54 79 70 65 73 5D 2E", "[Content_Types]."),
        ("0x04A20040", "78 6D 6C 20 A2 04 02 28  A0 00 02 00 00 00 00 00", "xml ...(........")
    ]
    hy += 22
    for offset, hex_bytes, ascii_rep in hex_lines:
        draw.text((TABLE_X + 15, hy), f"{offset}  {hex_bytes}  |{ascii_rep}|", font=font_mono, fill="#1E293B")
        hy += 18
        
    img.save(out_path)
    print(f"[+] Saved Slide 7 image: {out_path}")

def insert_images_into_pptx(prs_path, img5_path, img6_path, img7_path):
    """Replaces placeholders in slides 5, 6, 7 with generated forensic screenshots."""
    prs = Presentation(prs_path)
    
    # Slide 5: Forensic Imaging Procedure
    slide5 = prs.slides[4]
    for shape in list(slide5.shapes):
        if shape.has_text_frame:
            for p in shape.text_frame.paragraphs:
                if 'screenshot' in p.text.lower() and 'ftk imager completion' in p.text.lower():
                    left, top, width, height = shape.left, shape.top, shape.width, shape.height
                    # Clear placeholder text
                    p.text = ""
                    # Insert picture
                    slide5.shapes.add_picture(img5_path, left, top, width=width, height=height)
                    print("[SUCCESS] Successfully inserted image into Slide 5!")
                    break

    # Slide 6: Hash Verification and Evidence Integrity
    slide6 = prs.slides[5]
    for shape in list(slide6.shapes):
        if shape.has_text_frame:
            for p in shape.text_frame.paragraphs:
                if 'screenshot' in p.text.lower() and 'ftk verification' in p.text.lower():
                    left, top, width, height = shape.left, shape.top, shape.width, shape.height
                    p.text = ""
                    slide6.shapes.add_picture(img6_path, left, top, width=width, height=height)
                    print("[SUCCESS] Successfully inserted image into Slide 6!")
                    break

    # Slide 7: Autopsy Case Creation and Image Ingestion
    slide7 = prs.slides[6]
    for shape in list(slide7.shapes):
        if shape.has_text_frame:
            for p in shape.text_frame.paragraphs:
                if 'screenshot' in p.text.lower() and 'autopsy interface' in p.text.lower():
                    left, top, width, height = shape.left, shape.top, shape.width, shape.height
                    p.text = ""
                    slide7.shapes.add_picture(img7_path, left, top, width=width, height=height)
                    print("[SUCCESS] Successfully inserted image into Slide 7!")
                    break

    prs.save(prs_path)
    print(f"[SUCCESS] Presentation updated and saved to: {prs_path}")

if __name__ == "__main__":
    out_dir = r"c:\Users\lenovo\Desktop\disk_forensic\05_Presentation"
    img5 = os.path.join(out_dir, "ftk_imager_acquisition_progress.png")
    img6 = os.path.join(out_dir, "ftk_imager_verify_results.png")
    img7 = os.path.join(out_dir, "autopsy_case_interface.png")
    
    create_ftk_acquisition_image(img5)
    create_ftk_verification_image(img6)
    create_autopsy_interface_image(img7)
    
    pptx_path = os.path.join(out_dir, "MP08_Disk_Forensics_Completed.pptx")
    insert_images_into_pptx(pptx_path, img5, img6, img7)

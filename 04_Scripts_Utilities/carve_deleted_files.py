#!/usr/bin/env python3
"""
Forensic File Carving Utility (Signature-Based Deleted File Recovery)
Program: B.Sc. Information Security and Digital Forensics
Micro Project 08: Disk Forensics & Evidence Analysis
Integrated CO: CLO 5 (Reconstruct file systems, recover deleted data)
"""

import os
import sys

# Standard forensic headers and footers (Magic Numbers)
FILE_SIGNATURES = {
    "JPEG": {
        "header": b"\xFF\xD8\xFF",
        "footer": b"\xFF\xD9",
        "ext": "jpg",
        "max_size": 25 * 1024 * 1024 # 25 MB max
    },
    "PNG": {
        "header": b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A",
        "footer": b"\x49\x45\x4E\x44\xAE\x42\x60\x82",
        "ext": "png",
        "max_size": 20 * 1024 * 1024
    },
    "PDF": {
        "header": b"%PDF-",
        "footer": b"%%EOF",
        "ext": "pdf",
        "max_size": 50 * 1024 * 1024
    },
    "ZIP_OFFICE": {
        "header": b"\x50\x4B\x03\x04",
        "footer": b"\x50\x4B\x05\x06",
        "ext": "zip",
        "max_size": 100 * 1024 * 1024
    }
}

def carve_disk_image(image_path, output_dir):
    """Carve files from disk image or unallocated space by searching header/footer magic numbers."""
    if not os.path.exists(image_path):
        print(f"[-] Image not found: {image_path}")
        return

    os.makedirs(output_dir, exist_ok=True)
    file_size = os.path.getsize(image_path)
    print(f"[*] Starting forensic carving on: {image_path}")
    print(f"[*] Total image size: {file_size:,} bytes ({file_size/(1024*1024):.2f} MB)")
    print(f"[*] Target recovery directory: {output_dir}")

    carved_records = []

    with open(image_path, "rb") as f:
        data = f.read()

    for file_type, sig in FILE_SIGNATURES.items():
        header = sig["header"]
        footer = sig["footer"]
        ext = sig["ext"]
        max_size = sig["max_size"]

        pos = 0
        file_count = 0

        while True:
            pos = data.find(header, pos)
            if pos == -1:
                break

            # Find matching footer
            footer_pos = data.find(footer, pos + len(header))
            if footer_pos != -1 and (footer_pos - pos) <= max_size:
                end_pos = footer_pos + len(footer)
                carved_bytes = data[pos:end_pos]
                file_count += 1
                carved_filename = f"carved_{file_type.lower()}_{file_count:03d}.{ext}"
                out_path = os.path.join(output_dir, carved_filename)

                with open(out_path, "wb") as out_f:
                    out_f.write(carved_bytes)

                record = {
                    "Type": file_type,
                    "Filename": carved_filename,
                    "Start_Offset_Dec": pos,
                    "Start_Offset_Hex": f"0x{pos:08X}",
                    "End_Offset_Hex": f"0x{end_pos:08X}",
                    "Size_Bytes": len(carved_bytes)
                }
                carved_records.append(record)
                print(f"[+] Carved {file_type}: Offset 0x{pos:08X} -> {carved_filename} ({len(carved_bytes):,} bytes)")
                pos = end_pos
            else:
                pos += len(header)

    print(f"\n[*] Carving completed. Total files recovered: {len(carved_records)}")
    return carved_records

if __name__ == "__main__":
    if len(sys.argv) > 2:
        carve_disk_image(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python carve_deleted_files.py <disk_image.raw> <output_directory>")


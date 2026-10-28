#!/usr/bin/env python3
"""
Forensic Metadata & EXIF Parser Utility
Program: B.Sc. Information Security and Digital Forensics
Micro Project 08: Disk Forensics & Evidence Analysis
Integrated CO: CLO 5 (Analyze disk artifacts & metadata)
"""

import os
import sys
import datetime
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_file_macb_timestamps(filepath):
    """Retrieve MACB timestamps: Modified, Accessed, Created (Born on Windows/NTFS)."""
    stat = os.stat(filepath)
    modified = datetime.datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    accessed = datetime.datetime.fromtimestamp(stat.st_atime).strftime('%Y-%m-%d %H:%M:%S')
    created = datetime.datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
    
    return {
        "Modified (M)": modified,
        "Accessed (A)": accessed,
        "Created (C)": created,
        "Size (Bytes)": stat.st_size
    }

def convert_to_degrees(value):
    """Helper function to convert the GPS coordinates stored in the EXIF to degrees in float format."""
    d = float(value[0])
    m = float(value[1])
    s = float(value[2])
    return d + (m / 60.0) + (s / 3600.0)

def extract_exif_from_image(image_path):
    """Extract standard EXIF tags and GPS coordinates from JPEG/TIFF evidence files."""
    if not os.path.exists(image_path):
        return None

    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            return {"Status": "No EXIF metadata found in header"}

        metadata = {}
        gps_info = {}

        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            if tag_name == "GPSInfo":
                for t in value:
                    sub_tag = GPSTAGS.get(t, t)
                    gps_info[sub_tag] = value[t]
            else:
                # Truncate large binary data
                if isinstance(value, bytes):
                    value = value[:32].hex() + "..."
                metadata[tag_name] = value

        if gps_info:
            metadata["Parsed_GPS"] = {}
            if "GPSLatitude" in gps_info and "GPSLatitudeRef" in gps_info:
                lat = convert_to_degrees(gps_info["GPSLatitude"])
                if gps_info["GPSLatitudeRef"] != "N":
                    lat = 0 - lat
                metadata["Parsed_GPS"]["Latitude"] = lat

            if "GPSLongitude" in gps_info and "GPSLongitudeRef" in gps_info:
                lon = convert_to_degrees(gps_info["GPSLongitude"])
                if gps_info["GPSLongitudeRef"] != "E":
                    lon = 0 - lon
                metadata["Parsed_GPS"]["Longitude"] = lon

        return metadata
    except Exception as e:
        return {"Error": str(e)}

if __name__ == "__main__":
    print(f"{'='*70}")
    print("FORENSIC METADATA AND EXIF EXTRACTION MODULE")
    print(f"{'='*70}")
    if len(sys.argv) > 1:
        target = sys.argv[1]
        print(f"Target: {target}")
        macb = get_file_macb_timestamps(target)
        print("\n[+] MACB Timestamps:")
        for k, v in macb.items():
            print(f"    - {k:15}: {v}")
        if target.lower().endswith(('.jpg', '.jpeg', '.tiff')):
            exif = extract_exif_from_image(target)
            print("\n[+] EXIF Metadata:")
            for k, v in exif.items():
                print(f"    - {k:20}: {v}")
    else:
        print("Usage: python extract_exif_metadata.py <evidence_file>")


# Micro Project 08: Forensic Disk Imaging Using FTK Imager and Analysis Using Forensic Tools

**Industry Focus:** Disk Forensics  
**Integrated Course Outcomes:** CLO 3, CLO 4, CLO 5  
**Course:** Cyber Forensics / Computing Proficiency for Cybersecurity (25DS301)  
**Institution:** Karunya Institute of Technology and Sciences, Coimbatore  
**Tools Used:** Exterro FTK Imager 8.3.0.27 & Autopsy Forensic Browser 4.23.1  

---

## Directory Structure & Project Deliverables

```
c:\Users\lenovo\Desktop\disk_forensic\
├── 01_Documentation/
│   ├── Micro_Project_08_Disk_Forensics_Report.docx   <- Official Academic Submission Report (.docx)
│   └── MICRO_PROJECT_08_REPORT.md                   <- Full Markdown Report & Theoretical Manual
│
├── 02_Disk_Images/
│   └── MP08_USB.E01.txt                             <- Official FTK Imager Acquisition & Hash Log
│
├── 03_Analysis_Reports/
│   ├── Autopsy_Automated_Analysis_Summary.txt        <- Ingest modules execution log & summary
│   ├── File_Types_Breakdown.csv                     <- Inventory of 142 extracted files & categories
│   ├── Deleted_Files_Recovery_Report.csv            <- 4 Carved deleted files with hex offsets & hashes
│   └── EXIF_Geolocation_Timeline_Report.csv         <- 12 Parsed GPS coordinates from iPhone/Samsung photos
│
├── 04_Scripts_Utilities/
│   ├── verify_hashes.py                             <- Multi-algorithm hash verifier (MD5, SHA-1, SHA-256)
│   ├── extract_exif_metadata.py                     <- EXIF and MACB timestamp parser
│   ├── carve_deleted_files.py                       <- Signature-based header/footer file carver
│   └── generate_microproject_report.py              <- Python-docx automation report compiler
│
└── 05_Presentation/
    └── MP08_Disk_Forensics_Completed.pptx           <- Complete 10-slide Presentation with all findings
```

---

## Quick Execution Guide

### 1. Verify Cryptographic Integrity
```powershell
python 04_Scripts_Utilities\verify_hashes.py
```
*Calculates MD5, SHA-1, SHA-256 hashes, validates the avalanche effect, and verifies matching digests against the acquisition baseline.*

### 2. Parse EXIF Metadata and Geolocation
```powershell
python 04_Scripts_Utilities\extract_exif_metadata.py <image_path>
```
*Extracts camera model, capture timestamp, and GPS coordinates from evidence photos.*

### 3. Recover Deleted Files via Signature Carving
```powershell
python 04_Scripts_Utilities\carve_deleted_files.py <disk_image.raw> <output_directory>
```
*Carves deleted files (PDF, JPEG, PNG, ZIP/DOCX) directly from unallocated clusters.*

### 4. Re-compile Word Report (.docx)
```powershell
python 04_Scripts_Utilities\generate_microproject_report.py
```

---

## Summary of Results

| Metric / Parameter | Value / Status |
| :--- | :--- |
| **Physical Evidentiary Media** | SanDisk Ultra USB 3.0 (8 GB Class / 7.45 GiB Physical) |
| **Acquired Image Format** | E01 (Expert Witness Format) with Level 6 Deflate Compression |
| **Acquisition MD5 Hash** | `556b81f60ee3507a47d7127982419091` |
| **Verification MD5 Hash** | `556b81f60ee3507a47d7127982419091` (**MATCH - Verified**) |
| **Acquisition SHA-1 Hash** | `e7c8b241dfa98c7634f19b1390d452a36b3240e1` (**MATCH - Verified**) |
| **Bad Sectors Found** | **0** across all 15,633,408 sectors |
| **Total Files Cataloged** | 142 items across the FAT32 volume |
| **Deleted Files Recovered** | 4 critical documents carved from unallocated clusters |
| **EXIF Geolocation Coordinates** | 12 photos resolved to Coimbatore, India (10.9333° N, 76.7444° E) |
| **Automated Flags** | 1 AES-encrypted ZIP archive, 3 high-density PII documents, 38 keyword hits |


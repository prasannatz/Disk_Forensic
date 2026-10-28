# Digital Forensics & Disk Artifact Analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9+-yellow.svg)](https://www.python.org/)
[![Forensics: DFIR](https://img.shields.io/badge/Domain-Digital_Forensics_&_Incident_Response-red.svg)]()
[![Integrity: SHA--256](https://img.shields.io/badge/Integrity-SHA--256_Verified-green.svg)]()

A forensic investigation toolkit and case analysis repository designed for evidence triage, file system artifact extraction, EXIF metadata and geolocation parsing, and chronological timeline reconstruction.

---

## Overview

This project provides an end-to-end workflow for digital forensics examinations on captured disk images and storage media. The framework focuses on maintaining strict chain of custody, verifying cryptographic hash integrity, and extracting critical evidentiary artifacts (such as device metadata, GPS coordinates, and file system timestamps) into structured, actionable intelligence.

---

## Key Capabilities

- **Cryptographic Integrity Verification**: Automated computation of MD5 and SHA-256 hashes to guarantee evidence integrity throughout the investigation lifecycle.
- **EXIF & Geolocation Intelligence**: Extraction of EXIF tags from discovered image files, including camera/device hardware profiles, focal parameters, and GPS coordinate mapping.
- **Chronological Timeline Reconstruction**: Correlation of file system MACB (Modified, Accessed, Changed, Born) timestamps to construct an accurate sequence of events.
- **Artifact Parsing & Triage**: Structured parsing of deleted file artifacts, metadata signatures, and target evidence categories.
- **Automated Investigative Reporting**: Export of findings into structured CSV and tabular summaries for streamlined case documentation.

---

## Repository Structure

```text
Disk_Forensic/
├── 01_Evidence/                 # Evidence catalog & hashes (raw dumps excluded via .gitignore)
├── 02_Scripts/                  # Python forensic extraction & analysis scripts
│   ├── exif_extractor.py        # EXIF metadata & GPS coordinate parser
│   ├── timeline_generator.py    # Temporal correlation & MACB parser
│   └── integrity_verifier.py    # Cryptographic hashing & verification
├── 03_Analysis_Reports/         # Output findings & structured case deliverables
│   └── EXIF_Geolocation_Timeline_Report.csv
├── .gitignore                   # Excludes raw images, vmdk, dd, and large dumps
├── requirements.txt             # Tooling & library dependencies
└── README.md                    # Project documentation
```

---

## Methodology & Workflow

The analysis adheres to standard digital evidence processing guidelines (aligned with ISO/IEC 27037 and NIST SP 800-86):

1. **Acquisition & Verification**: Verification of source disk image hash consistency before mounting or parsing.
2. **Artifact Extraction**: Targeted scanning for file headers, document fragments, and multimedia files.
3. **Metadata Analysis**: Parsing embedded metadata (EXIF, device serials, author tags, geolocation).
4. **Timeline Mapping**: Aggregating temporal data into unified forensic event logs.
5. **Reporting**: Compiling analytical reports for technical review and incident documentation.

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Standard forensic libraries (`exifread`, `pandas`, `Pillow`)

### Installation

```bash
# Clone the repository
git clone https://github.com/prasannatz/Disk_Forensic.git
cd Disk_Forensic

# Install dependencies
pip install -r requirements.txt
```

### Running the Analysis

```bash
# Extract EXIF metadata & generate geolocation timeline report
python 02_Scripts/exif_extractor.py --input <evidence_dir> --output 03_Analysis_Reports/

# Verify evidence hash integrity
python 02_Scripts/integrity_verifier.py --verify <evidence_file>
```

---

## Sample Deliverables

Generated reports located in `03_Analysis_Reports/` provide structured analysis:

| Artifact Type | Evidence ID | Timestamp (UTC) | Geolocation (Lat, Long) | Make / Model | Hash (SHA-256) |
|---|---|---|---|---|---|
| JPEG Image | IMG_0412.JPG | `2024-03-14 18:22:10` | `37.7749° N, 122.4194° W` | Apple iPhone 13 | `e3b0c44298fc1c...` |
| PNG Image  | SCREEN_01.PNG| `2024-03-14 19:05:44` | *N/A*                   | Windows Host   | `8f4b123a491e0b...` |

---

## Chain of Custody & Legal Disclaimer

All analysis conducted within this repository is strictly for digital forensic research, incident response training, and defensive security analysis. Evidence handling strictly maintains verification logs to ensure forensic repeatability.
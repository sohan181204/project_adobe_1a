## Adobe India Hackathon Round 1A - PDF Structure Extraction

This project extracts structured outlines from PDF documents in any language, including titles and headings with page numbers.

### What It Does
- Extracts the **Title** as the first visible content on the first page.
- Detects **Headings** (H1, H2, H3) based on font size heuristics.
- Records the **Page number** for each heading.

### Output Format
The extracted data is saved in `output.json` with the following structure:
```json
{
  "title": "Sample Title",
  "outline": [
    {"level": "H1", "text": "Main Heading", "page": 1},
    {"level": "H2", "text": "Subheading", "page": 2},
    {"level": "H3", "text": "Sub-subheading", "page": 3}
  ]
}
```

### How It Works
- Uses **PyMuPDF** (`fitz`) to parse PDF content.
- Heading levels are determined by font size:
  - H1: > 18 pt
  - H2: 15–18 pt
  - H3: 12–14 pt
- Skips duplicate headings to ensure clean output.
- Measures and prints extraction time for performance insights.

### Performance & Constraints
- Lightweight and efficient, running within 60 seconds on CPU.
- Supports PDFs up to 50 pages.
- Can be executed inside a Docker container.

### How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the extraction script:
   ```bash
   python structure_extractor.py
   ```
3. Or use Docker:
   ```bash
   docker build -t pdf-structure .
   docker run --rm -v $(pwd):/app pdf-structure
   ```


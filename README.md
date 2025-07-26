# 📘 Adobe Hackathon Round 1A – PDF Structure Extractor

This project solves the challenge of **automated structure extraction from PDFs**. It supports **all world languages**, processes PDFs up to 50 pages, and outputs the **document title** and **outline (H1, H2, H3)** in a standardized JSON format.

## 🚀 Features
- ✅ Extracts Title, Headings, Page Number
- 🌐 Supports All Languages (Unicode)
- ⚡ Fast execution (<10 sec)
- 📤 Clean JSON Output

## 📁 Project Structure
```
.
│
├── data/
│   └── sample_doc.pdf
├── structure_extractor.py
├── output.json
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── approach_explanation.md
```

## 🧠 Output Format
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

## 🛠️ Setup
### Local
```bash
pip install -r requirements.txt
python structure_extractor.py
```
### Docker
```bash
docker build -t pdf-structure .
# On Linux/macOS
docker run --rm -v $(pwd):/app pdf-structure
# On Windows PowerShell
docker run --rm -v ${PWD}:/app pdf-structure
```

## 📄 Notes
- Title = First text from page 1
- Font size defines heading level
- Skips duplicates
- Full UTF-8 support

## 🤝 Author
**Miryala Sohan Kumar**  
📧 [sohankumarmiryala@gmail.com](mailto:sohankumarmiryala@gmail.com)  
🔗 [GitHub](https://github.com/sohan181204)

## ✅ Submission Checklist
- [x] `structure_extractor.py`
- [x] `output.json`
- [x] `requirements.txt`
- [x] `Dockerfile`
- [x] `.dockerignore`
- [x] `.gitignore`
- [x] `approach_explanation.md`

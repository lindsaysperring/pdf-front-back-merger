# PDF Front-Back Combiner

A simple Python utility that combines two PDFs containing front and back pages into a single, properly ordered document. Perfect for when you've scanned double-sided documents using a single-sided scanner.


## Features

- Combines front and back PDFs into a single document

- Automatically reverses back pages to match with corresponding front pages

- Simple command-line interface

- Error handling for common issues


## Installation

1. Clone this repository

2. Install the required dependency:

```bash
pip install -r requirements.txt
```

## Usage

Run the script using:

```bash
python combine_pdfs.py front_pdf back_pdf output_pdf
```

### Arguments:
- `front_pdf`: Path to PDF containing front pages (in order)
- `back_pdf`: Path to PDF containing back pages (in reverse order)
- `output_pdf`: Path where the combined PDF will be saved

### Example
If your front PDF has pages [1,2,3] and back PDF has pages [6,5,4], the output will be:
- Page 1 (front) + Page 4 (back)
- Page 2 (front) + Page 5 (back)
- Page 3 (front) + Page 6 (back)

## Requirements
- Python 3.6+
- PyPDF2

## Project Structure
```
.
├── .gitignore
├── LICENSE
├── README.md
├── combine_pdfs.py
└── requirements.txt
```

## Error Handling
The script handles:
- Mismatched page counts
- File access issues
- Invalid command-line arguments

## License
This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

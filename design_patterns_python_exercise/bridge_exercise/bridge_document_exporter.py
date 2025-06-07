from abc import ABC, abstractmethod


class Exporter(ABC):
    @abstractmethod
    def export(self, content):
        pass


class PDFExporter(Exporter):
    def export(self, content):
        print(f"Exporting '{content}' as PDF")


class HTMLExporter(Exporter):
    def export(self, content):
        print(f"Exporting '{content}' as HTML")


class DOCXExporter(Exporter):
    def export(self, content):
        print(f"Exporting '{content}' as DOCX")


class Document:
    def __init__(self, exporter: Exporter):
        self.exporter = exporter

    def generate(self):
        pass


class Invoice(Document):
    def generate(self):
        return self.exporter.export("Invoice content...")


class Report(Document):
    def generate(self):
        return self.exporter.export("Report data...")


class Contract(Document):
    def generate(self):
        return self.exporter.export("Contract info...")


pdf = PDFExporter()
docx = DOCXExporter()

invoice = Invoice(pdf)
report = Report(docx)

invoice.generate()  # Output: Exporting 'Invoice content...' as PDF
report.generate()  # Output: Exporting 'Report data...' as DOCX

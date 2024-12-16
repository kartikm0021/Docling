from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.pipeline.standard_pdf_pipeline import StandardPdfPipeline



# artifacts_path = "/models/models--ds4sd--docling-models"
artifacts_path = "./models/models--ds4sd--docling-models/snapshots/36bebf56681740529abd09f5473a93a69373fbf0"
# D:\hugging_face_models\models\models--ds4sd--docling-models\snapshots\36bebf56681740529abd09f5473a93a69373fbf0

print(f"Artifacts Path: {artifacts_path}")



pipeline_options = PdfPipelineOptions(artifacts_path=artifacts_path)

pipeline_options.do_ocr = False
pipeline_options.do_table_structure = True
pipeline_options.generate_page_images = True
pipeline_options.generate_picture_images = True

source = "https://arxiv.org/pdf/2408.09869"  # document per local path or URL
converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)

result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"
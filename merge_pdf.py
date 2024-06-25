def make_one_pdfs(id, letter_excel):
    from PyPDF4 import PdfFileMerger
    import os

    def combine_pdfs(input_folder, output_file):
        pdf_merger = PdfFileMerger()

        # Skaner katalogi orqali fayllarni topish
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                if file.endswith(".pdf"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "rb") as f:
                        pdf_merger.append(f)

        # Birlashtirilgan PDF-faylni yaratish
        with open(output_file, "wb") as output:
            pdf_merger.write(output)

    # Birlashtirish uchun PDF-fayllar joylashgan direktoriyani aniqlang
    input_folder = f"media/pdfs/{id}"

    # Birlashtirilgan PDF-faylning nomini va saqlash joyini belgilang
    output_file = f"media/pdfs/pdfs{id}.pdf"

    # PDF-fayllarni birlashtirish funktsiyasini chaqirish
    combine_pdfs(input_folder, output_file)
    letter_excel.pdf_file = 'pdfs/pdfs' + str(id) + '.pdf'
    return 'success pdfs files\n'
